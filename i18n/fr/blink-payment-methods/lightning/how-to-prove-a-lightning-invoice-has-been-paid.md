# Comment prouver qu'une facture Lightning a été payée?

Dans le domaine du Lightning Network (LN), une preuve de paiement (Proof of Payment ou PoP) constitue une reconnaissance vérifiable qu’une transaction spécifique a bien eu lieu. Les paiements Lightning sont atomiques, ce qui signifie que si le payeur reçoit un pré-image, cela garantit que le paiement a bien été reçu par le nœud de destination.

**Comment fonctionne la preuve de paiement dans le Lightning Network?**

1. **Génération de la facture par le nœud du bénéficiaire**:
  - Le processus commence par la création d’une facture Lightning Network par le nœud du bénéficiaire. Cette facture n’est pas une simple demande de paiement, mais une structure complexe contenant plusieurs éléments essentiels à la transaction. L’un des composants clés de cette facture est un hachage cryptographique d’un secret, appelé le «pré-image de paiement».
2. **Signature de la facture**
  - Pour garantir l’authenticité et éviter toute falsification, le nœud du bénéficiaire signe numériquement la facture. Cette signature constitue une preuve cryptographique que la facture a bien été générée par le véritable propriétaire du nœud et non par un imposteur.
3. **Paiement et divulgation de la pré-image**:
  - Une fois que le payeur décide de régler la facture, le paiement est acheminé à travers le Lightning Network jusqu’au bénéficiaire. Lors de la réception réussie du paiement, le nœud du bénéficiaire divulgue la «pré-image de paiement» au payeur. Cette pré-image est essentiellement le secret dont le hachage figurait dans la facture.
4. **Combinaison de la facture et de la pré-image comme preuve de paiement**:
  - La dernière étape pour établir une preuve de paiement consiste à combiner la facture LN originale avec la pré-image de paiement. Le payeur peut utiliser ces deux éléments pour prouver qu’un paiement a bien été effectué au bénéficiaire. En effet, avec ces deux informations, toute personne peut vérifier que le hachage contenu dans la facture correspond à la pré-image fournie lors du paiement, ce qui prouve que la transaction a bien eu lieu comme indiqué.

**Pourquoi la preuve de paiement est-elle importante?**

1. **Vérification du paiement**:
  - La preuve de paiement est essentielle pour permettre aux parties de confirmer que la transaction a été traitée correctement, sans avoir à dépendre d’un tiers.
2. **Non-répudiation**:
  - Grâce aux preuves cryptographiques fournies par la preuve de paiement, le bénéficiaire ne peut pas nier avoir reçu le paiement, et de même, le payeur ne peut pas nier l’avoir effectué. Cela est essentiel pour la résolution des litiges et l’établissement de la confiance dans les transactions numériques.
3. **Sécurité**:
  - La nature cryptographique de la facture et de la pré-image garantit que la transaction est sécurisée et résistante à la falsification ou à la fraude.

**En résumé, pour prouver qu’une facture Lightning a été payée, deux éléments sont nécessaires**:

1.  La **facture Lightning** originale fournie par le nœud
2. La **pré-image de paiement** reçue par le payeur après le paiement réussi

Veuillez, s’il vous plaît, avoir ces informations à portée de main si vous contactez l’équipe d’assistance de Blink ou les opérateurs d’autres nœuds Lightning.
