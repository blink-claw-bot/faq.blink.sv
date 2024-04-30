{
  description = "Python environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachSystem ["x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin"] (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
      pythonEnv = pkgs.python3.withPackages (ps: with ps; [
        ipykernel
        ipython
        ipywidgets
        llama-index-core
        llama-index-cli
        openai
        pandas
        python-dotenv
        requests
        (ps.buildPythonPackage rec {
          pname = "llama-index-vector-stores-pinecone";
          version = "0.1.4";
          format = "pyproject";
          src = pkgs.fetchurl {
            url = "https://files.pythonhosted.org/packages/15/7a/772a2ee448c0d8e199ab21ceec71abee2e956b702eca9fbec867478b6e4f/llama_index_vector_stores_pinecone-0.1.4.tar.gz";
            sha256 = "ab5f2141d44404c9ad36611c11e8b6afb35b6f0a80959726f8eab5b65a157549";
          };
          nativeBuildInputs = [ poetry-core ];
          propagatedBuildInputs = [
            llama-index-core
            pinecone-client
          ];
        })
        (ps.buildPythonPackage rec {
          pname = "llama-index-readers-github";
          version = "0.1.7";
          format = "pyproject";
          src = pkgs.fetchurl {
            url = "https://files.pythonhosted.org/packages/b5/11/afae7d3dc8e03144ae318a8be713a44f184b53a63414ed13a8c62311ecc1/llama_index_readers_github-0.1.7.tar.gz";
            sha256 = "5dc8d2d10615640da75e0bea03147795a5e752556e9dc701852c1a6b182b869d";
          };
          nativeBuildInputs = [ poetry-core ];
          propagatedBuildInputs = [
            httpx
            llama-index-core
            llama-index-readers-file
          ];
        })
        (ps.buildPythonPackage rec {
          pname = "pyairtable";
          version = "2.3.3";
          src = pkgs.fetchPypi {
            inherit pname version;
            sha256 = "6f52bd270d28ba6459b7cc473588e517085a737d70c68e855e6d104972e1121e";
          };
        propagatedBuildInputs = with pkgs.python3Packages; [
          requests
          typing-extensions
          inflection
          pydantic
        ];
        checkInputs = with pkgs.python3Packages; [
          pytest
          requests-mock
          mock
          responses
        ];
        doCheck = false;
      })
      ]);
    in {
      packages.default = pythonEnv;
      devShells.default = pkgs.mkShell {
        buildInputs = [ pythonEnv ];
        TIKTOKEN_CACHE_DIR = ".cache/.tiktoken";
        shellHook = "echo 'The Python environment is ready.'";
      };
    });
}
