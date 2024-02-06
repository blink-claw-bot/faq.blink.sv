# ¿Cómo obtener un comprobante de pago de Blink?

As discussed in the answer to the question [How to prove that a lightning invoice was paid? ](../blink-and-other-wallets/how-to-prove-that-a-lightning-invoice-was-paid.md) the information needed to prove a payment of a Lightning invoice is:\
&#x20; 1\.   The original **Lightning Invoice** provided by the payee node\
&#x20; 2\.   The **payment pre-image** received by the payer on the successful payment\
\
This information is exposed in the Blink Transaction History when clicking \`All transactions\` then choose the sent payment in question.\


Copie los campos `Preimagen / Prueba de Pago` y `Solicitud de Pago` que juntos pueden servir como Prueba de Pago para cualquier persona que pueda verificar criptográficamente.

Actualmente, la Preimagen solo se comparte para pagos en la red Lightning, pero pronto también se mostrará para pagos realizados a otros usuarios de Blink.

En caso de una transacción on-chain el pago se transmite públicamente a la red de Bitcoin y es confirmado por los mineros en la cadena de bloques. Saber el ID de Transacción (txid) permite a todos verificar que la transacción ha tenido lugar (la cantidad ha sido pagada a la dirección de Bitcoin) en un explorador de bloques público como [mempool.space](https://mempool.space). Para demostrar una transacción on-chain, comparta la dirección de destino y el txid y tenga en cuenta que estos (a diferencia de la factura y la preimagen de Lightning) son visibles para cualquier persona que lea la cadena de bloques de Bitcoin.
