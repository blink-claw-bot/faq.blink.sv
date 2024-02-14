# What are the transaction fees for using Blink wallet?

Blink's transaction fees are designed to be dynamic and adapt to the current market conditions to provide the best possible pricing for our users. Below is a table that shows the average fees for both the on-chain and Lightning Network transactions, as well as the lowest and highest fees observed. Please note that fees may vary depending on factors such as network congestion and user preferences.

|                      | Deposits                                               | Withdrawals                                                                                          |
|----------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Intraledger**      | 0% service fee                                         | 0% service fee                                                                                      |
| **Lightning**        | 0% service fee<br>+ The sender pays the LN routing fees| 0% service fee<br>+ Routing fees (~0.02% historical routing fees to external wallets)              |
| **On-chain**         | **For deposits higher than 1,000,000 sats:**<br>0% service fee<br><br>**For deposits lower than 1,000,000 sats:**<br>5,000 sats fixed fee | 10,000 sats fixed fee<br>+ Mining fees (varies depending on the market)<br>+ For an imbalance of more than 10M sats LN/on-chain per month: additional 0.5% fees |
| **BTC <-> Dollar Conversion** | $0 fixed fee<br>+ 0.2% spread                                | $0 fixed fee<br>+ 0.2% spread                                                                      |

Note: For clarity, the fees listed under each transaction type are cumulative. For instance, if you're withdrawing to an on-chain address, you will incur the 10,000 sats fixed fee + plus the mining fee (applicable to that current market) + if the wallet has an [imbalance of more than 10M sats LN/on-chain](why-does-blink-have-a-lightning-onchain-imbalance-threshold.md) in a rolling month: additional 0.5% fees
