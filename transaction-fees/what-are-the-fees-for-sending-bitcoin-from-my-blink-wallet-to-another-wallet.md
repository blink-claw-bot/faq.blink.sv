# What are the fees for sending Bitcoin from my Blink wallet to another wallet?

The transaction fees vary depending on the type of transaction, whether it's an on-chain transaction or a Lightning transaction.

For sending Lightning payments, a routing fee is paid by the user, but there are no extra fees applied by Blink.

On the other hand, Blink's on-chain transaction fees are composed of three factors:

1. [**Miner fee**](what-are-mining-fees.md) - This fee is paid according to the current mempool state.
2. **Tiered fixed fee** - For withdrawals lower than 1,000,000 sats: 5,000 sats. For withdrawals of 1,000,000 sats or higher: 10,000 sats.
3. **Additional fee** - A 0.2% extra fee is charged for transactions above the allowance of 10 million sats LN-onchain imbalance in a 30-day rolling window.

Please note that the exact amount of transaction fees may vary depending on the current market conditions and network congestion.
