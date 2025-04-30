# Wie kann man beweisen, dass eine Lightning Invoice bezahlt wurde?

Im Bereich des Lightning Network (LN) dient ein Proof of Payment (PoP) als überprüfbare Bestätigung, dass eine bestimmte Transaktion erfolgreich stattgefunden hat. Lightning-Zahlungen sind atomar, d. h. wenn der Zahler ein Preimage erhält, wurde die Zahlung mit Sicherheit vom Zielknoten empfangen.

**Wie funktioniert der Zahlungsnachweis im Lightning Network?**

1. **Invoice Erstellung durch den Knotenpunkt des Zahlungsempfängers**:
   * Der Prozess beginnt mit der Erstellung einer Lightning Invoice durch die Node des Zahlungsempfängers. Bei dieser Invoice handelt es sich nicht nur um eine einfache Zahlungsanforderung, sondern um eine komplexe Struktur, die verschiedene für die Transaktion wichtige Elemente enthält. Eine der entscheidenden Komponenten dieser Rechnung ist ein kryptografischer Hash eines Geheimnisses, das so genannte „Zahlungs Preimage“.
2. **Rechnungsunterzeichnung**:
   * Um die Authentizität sicherzustellen und Manipulationen zu verhindern, signiert der Node des Zahlungsempfängers die Rechnung digital. Diese Signatur ist ein kryptografischer Beweis dafür, dass die Rechnung tatsächlich vom tatsächlichen Eigentümer des Nodes und nicht von einem Betrüger erstellt wurde.
3. **Zahlung und Offenlegung des Preimage**:
   * Sobald der Zahler beschließt, die Rechnung zu begleichen, wird die Zahlung über das Lightning Network an den Zahlungsempfänger weitergeleitet. Nach erfolgreichem Eingang der Zahlung gibt der Node des Zahlungsempfängers das „Zahlungs Preimage “ an den Zahler frei. Dieses Preimage ist im Wesentlichen das Geheimnis, dessen Hash in der Rechnung enthalten war.
4. **Kombination aus Rechnung und Preimage als Zahlungsnachweis**:
   * Der letzte Schritt bei der Erstellung eines Zahlungsnachweises ist die Kombination aus der Original-LN-Rechnung und dem Zahlungs Preimage. Mit diesen beiden Teilen kann der Zahler beweisen, dass eine Zahlung an den Zahlungsempfänger erfolgt ist. Mit diesen beiden Informationen kann jeder überprüfen, ob der Hash in der Rechnung mit dem bei der Zahlung übermittelten Pre-Image übereinstimmt, und damit beweisen, dass die Transaktion tatsächlich wie angegeben erfolgt ist.

**Warum ist der Zahlungsnachweis wichtig?**

1. **Zahlungsnachweis**:
   * Der Zahlungsnachweis ist für die Parteien von entscheidender Bedeutung, um zu bestätigen, dass die Transaktion korrekt abgewickelt wurde, ohne sich auf eine dritte Partei verlassen zu müssen.
2. **Nichtabstreitbarkeit**
   * Mit den kryptografischen Beweisen, die der Zahlungsnachweis liefert, kann der Zahlungsempfänger nicht bestreiten, die Zahlung erhalten zu haben, und ebenso kann der Zahler nicht bestreiten, die Zahlung geleistet zu haben. Dies ist von entscheidender Bedeutung für die Beilegung von Streitigkeiten und den Aufbau von Vertrauen in digitale Transaktionen.
3. **Sicherheit**:
   * Die kryptografische Natur der Invoice und des Preimage gewährleistet, dass die Transaktion sicher und vor Manipulationen oder Betrug geschützt ist.

**Zum Nachweis, dass eine Lightning Invoice bezahlt wurde, sind zwei Informationen erforderlich:**

Die vom Node bereitgestellte orginale **Lightning Rechnung** 

Das **Zahlungs Preimage**, dass der Zahler bei erfolgreicher Zahlung erhält
