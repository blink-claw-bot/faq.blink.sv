import os
import logging
import sys
from dotenv import load_dotenv
from llama_index.core import Settings, StorageContext, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone
from llama_index.readers.github import GithubRepositoryReader, GithubClient
import nest_asyncio
from pyairtable import Api
from llama_index.core.schema import TextNode

# Configure basic logging to the console with an informational level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Loading environment variables")
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
AIRTABLE_ACCESS_TOKEN = os.getenv("AIRTABLE_ACCESS_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Define the required environment variables with descriptive names for error messages
required_env_vars = {
    "OPENAI_API_KEY": OPENAI_API_KEY,
    "PINECONE_API_KEY": PINECONE_API_KEY,
    "AIRTABLE_ACCESS_TOKEN": AIRTABLE_ACCESS_TOKEN,
    "GITHUB_TOKEN": GITHUB_TOKEN
}

# Check for missing environment variables
missing_vars = [var for var, value in required_env_vars.items() if value is None]
if missing_vars:
    logging.error("Missing environment variables: " + ", ".join(missing_vars))
    sys.exit(1)  # Exit the program with an error code

# Proceed if all environment variables are set
logging.info("All required environment variables are set. Continuing with script...")

# Create RAG Index
logging.info("Create RAG Index")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-large", api_key=OPENAI_API_KEY, organization="CYGcqVcCcbCam01D1FDINCTk")
vector_store = PineconeVectorStore(index_name="blink-3072")
storage_context = StorageContext.from_defaults(vector_store=vector_store)
pc = Pinecone(api_key=PINECONE_API_KEY)
INDEX = "blink-3072"
pc.describe_index(INDEX)

# Load FAQ
logging.info("Load FAQ")
github_client = GithubClient(GITHUB_TOKEN)
repo_owner = "GaloyMoney"
repo_name = "faq.blink.sv"
repo_branch = "main"
loader = GithubRepositoryReader(
    github_client,
    owner=repo_owner,
    repo=repo_name,
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_directories=(["i18n", ".github", ".gitbook"], GithubRepositoryReader.FilterType.EXCLUDE),
    verbose=False
)
nest_asyncio.apply()
md_docs = loader.load_data(branch=repo_branch)
logging.info(f"Loaded {len(md_docs)} documents from GitHub.")

# Filter documents
for d in md_docs:
    if d.metadata["file_path"] == "SUMMARY.md":
        md_docs.remove(d)
        continue
    d.id_ = d.metadata["file_path"]
    d.metadata["source"] = "FAQ"
    d.metadata["language"] = "EN"
    d.metadata["extension"] = ".md"
    d.excluded_embed_metadata_keys = ["url", "source", "language", "file_name", "extension"]
    d.excluded_llm_metadata_keys = ["url", "source", "language", "file_name", "extension"]
logging.info(f"Remaining documents after filtering: {len(md_docs)}")

# Load AirTable
logging.info("Load AirTable")
api = Api(AIRTABLE_ACCESS_TOKEN)
table = api.table('appHWT7d7zX6k0gXo', 'tblDSw7q7gjH7CAHo')
records = table.all()
logging.info(f"Fetched {len(records)} records from Airtable.")

# Prepare QA nodes for indexing
qa_nodes = []
for record in records:
    text = f"- User: {record['fields']['Question']}\n- Assistant: {record['fields']['Answer']}"
    metadata = {
        'language': record['fields']['Language'],
        'source': "Support QAs"
    }
    node = TextNode(text=text, id_=record['id'], metadata=metadata, excluded_embed_metadata_keys=['language', 'source'])
    qa_nodes.append(node)
logging.info(f"Prepared {len(qa_nodes)} QA nodes for indexing.")

assert len(qa_nodes) == len(records)

# Review / delete existing
logging.info("Review / delete existing index")
index = pc.Index(INDEX)
index.describe_index_stats()
index.delete(delete_all=True)
logging.info(f"Deleted the contents of {INDEX}.")

# Upload indexes from the FAQs
logging.info(f"Initializing upload from FAQs with {len(md_docs)} documents.")
index = VectorStoreIndex.from_documents(
    md_docs,
    storage_context=storage_context
)
logging.info("Uploading from the FAQs is completed.")

# Upload indexes from the AirTable
logging.info(f"Initializing upload from the Airtable with {len(qa_nodes)} documents.")
index = VectorStoreIndex(
    qa_nodes,
    storage_context=storage_context
)
logging.info("Uploading from the AirTable is completed.")
