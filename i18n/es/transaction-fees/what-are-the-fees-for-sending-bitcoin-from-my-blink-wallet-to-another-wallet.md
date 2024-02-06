# ¿Cuáles son las tarifas para enviar Bitcoin desde mi billetera Blink a otra billetera?

Las tarifas de transacción varían dependiendo del tipo de transacción, ya sea una transacción on-chain o una transacción Lightning.

Para enviar pagos de Lightning, el usuario paga una tarifa de enrutamiento, pero no se aplican tarifas adicionales.

Por otro lado, las tarifas de transacción on-chain de Blink están compuestas por tres factores.

1. [**Tarifa de minero**](what-are-mining-fees.md) - Esta tarifa se paga de acuerdo al estado actual del mempool.
2. Tarifa fija - Esta es una cantidad fija de 10,000 sats.
3. Tarifa adicional: se cobra una tarifa extra del 0,5% por transacciones por encima de la asignación de 10 millones de sats de desequilibrio LN-onchain.

Tenga en cuenta que el monto exacto de las tarifas de transacción puede variar según las condiciones actuales del mercado y la congestión de la red.
