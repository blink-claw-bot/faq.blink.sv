# ¿Cómo demostrar que se pagó una factura de rayo?

En el ámbito de la Lightning Network (LN), una Prueba de Pago (PoP) sirve como una confirmación verificable de que una transacción específica ha ocurrido exitosamente. Los pagos de Lightning son atómicos, lo que significa que si el pagador recibe una preimagen, el pago fue recibido con seguridad por el nodo de destino.

**¿Cómo funciona la Prueba de Pago en la Lightning Network?**

1. **Generación de factura por el nodo del beneficiario**:
   * El proceso comienza con la creación de una factura de la Red Lightning por parte del nodo del beneficiario. Esta factura no es solo una simple solicitud de pago, sino una estructura compleja que comprende varios elementos cruciales para la transacción. Uno de los componentes críticos de esta factura es un hash criptográfico de un secreto, conocido como 'preimagen de pago'.
2. **Firma de factura**:
   * Para garantizar la autenticidad y prevenir la manipulación, el nodo del beneficiario firma digitalmente la factura. Esta firma es una prueba criptográfica de que la factura fue generada por el verdadero propietario del nodo y no por un impostor.
3. **Pago y divulgación de la preimagen**:
   * Una vez que el pagador decide cumplir con la factura, el pago se dirige a través de la Red Lightning para llegar al beneficiario. Al recibir con éxito el pago, el nodo del beneficiario libera la 'preimagen del pago' al pagador. Esta preimagen es esencialmente el secreto cuyo hash se incluyó en la factura.
4. **Combinación de Factura y Pre-Imagen como Prueba de Pago**:
   * El último paso para establecer una Prueba de Pago es la combinación de la factura original de LN y la preimagen del pago. El pagador puede utilizar estas dos piezas para demostrar que se realizó un pago al beneficiario. Esencialmente, con estas dos piezas de información, cualquier persona puede verificar que el hash en la factura corresponde a la preimagen proporcionada al realizar el pago, demostrando que la transacción realmente ocurrió según se afirma.

**¿Por qué es importante la prueba de pago?**

1. **Verificación de Pago**:
   * PoP es crucial para que las partes confirmen que la transacción se procesó correctamente sin necesidad de depender de un tercero.
2. **No repudio**.
   * Con la evidencia criptográfica proporcionada por el PoP, el beneficiario no puede negar haber recibido el pago, y de manera similar, el pagador no puede negar haber realizado el pago. Esto es crucial para la resolución de disputas y la generación de confianza en las transacciones digitales.
3. **Seguridad**
   * La naturaleza criptográfica de la factura y la preimagen asegura que la transacción sea segura y resistente a manipulaciones o fraudes.

**En resumen, para demostrar que se pagó una factura de relámpago se necesitan dos piezas de información:**

1. La **Factura Lightning** original proporcionada por el nodo
2. La **preimagen de pago** recibida por el pagador en el pago exitoso

Por favor, si estás contactando al equipo de soporte de Blink o a los operadores de otros nodos Lightning, ten esta información a mano.
