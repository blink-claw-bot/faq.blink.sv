# What is a fee reimbursement in Blink, and when does it happen?

When you send a Bitcoin payment using the Lightning Network through Blink, the app attempts to determine the most accurate routing fee by probing different payment paths. This process is indicated by a spinning circle on the send screen.

However, sometimes the probing may fail due to certain nodes not responding, or you might choose to send the payment before the probing completes. In such cases, Blink charges an estimated fee, which might be higher than the actual fee incurred once the payment is settled.

To ensure fairness, Blink automatically reimburses the difference between the estimated fee charged and the actual fee paid. This reimbursement is credited back to your balance and appears as a transaction labeled "Fee Reimbursement."

**Example:**

• You send a payment, and Blink estimates the fee to be 100 sats due to incomplete probing.

• After the payment is settled, the actual fee turns out to be 20 sats.

• Blink reimburses you 80 sats, which is the difference between the estimated and actual fees.

**Tips to Minimize Overestimated Fees:**

• Wait for the spinning circle to stop before confirming your payment. This allows Blink to complete the probing process and calculate a more accurate fee.

• Ensure a stable internet connection to facilitate successful probing.

By following these tips, you can help Blink determine the most accurate fees and reduce the likelihood of overestimated charges.
