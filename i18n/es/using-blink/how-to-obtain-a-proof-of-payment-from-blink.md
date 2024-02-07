# ¿Cómo obtener un comprobante de pago de Blink?

Como se discutió en la respuesta a la pregunta [Cómo demostrar que se pagó una factura de Lightning](../blink-and-other-wallets/how-to-prove-that-a-lightning-invoice-was-paid.md), la información necesaria para demostrar el pago de una factura de Lightning es:
&#x20; 1\.   La **Factura de Lightning** original proporcionada por el nodo del beneficiario
&#x20; 2\.   La **preimagen de pago** recibida por el pagador en el pago exitoso

Esta información se muestra en el Historial de Transacciones de Blink al hacer clic en `Todas las transacciones` y luego elegir el pago enviado en cuestión.


Copie los campos `Preimagen / Prueba de Pago` y `Solicitud de Pago` que juntos pueden servir como Prueba de Pago para cualquier persona que pueda verificar criptográficamente.

Actualmente, la Preimagen solo se comparte para pagos en la red Lightning, pero pronto también se mostrará para pagos realizados a otros usuarios de Blink.

En caso de una transacción on-chain el pago se transmite públicamente a la red de Bitcoin y es confirmado por los mineros en la cadena de bloques. Saber el ID de Transacción (txid) permite a todos verificar que la transacción ha tenido lugar (la cantidad ha sido pagada a la dirección de Bitcoin) en un explorador de bloques público como [mempool.space](https://mempool.space). Para demostrar una transacción on-chain, comparta la dirección de destino y el txid y tenga en cuenta que estos (a diferencia de la factura y la preimagen de Lightning) son visibles para cualquier persona que lea la cadena de bloques de Bitcoin.
