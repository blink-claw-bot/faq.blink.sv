# How to obtain a Proof of Payment from Blink?

As discussed in the answer to the question [How to prove that a lightning invoice was paid? ](../blink-and-other-wallets/how-to-prove-that-a-lightning-invoice-was-paid.md) the information needed to prove a payment of a Lightning invoice is:
  1. The original **Lightning Invoice** provided by the payee node
  2. The **payment pre-image** received by the payer on the successful payment

This information is exposed in the Blink Transaction History when clicking \`All transactions\` then choose the sent payment in question.


Copy the `Preimage / Proof of Payment` and the  `Payment Request` fields which together can serve as a Proof of Payment to anyone who is able to verify cryptographically.

Currently the Preimage is only shared for Lightning network payments, but soon it will be displayed for payments made to other Blink users as well.

In case of an on-chain transaction the payment is publicly broadcasted to the bitcoin network and confirmed by miners in the blockchain. Knowing the Transaction ID (txid) makes everyone able to verify that the the transaction has taken place (the amount has been paid to the bitcoin address) in a public block explorer like [mempool.space](https://mempool.space).
To prove an onchain transaction share the destination address and the txid and be aware that these (unlike the lightning invoice and preimage) are visible to anyone reading the bitcoin blockchain.
