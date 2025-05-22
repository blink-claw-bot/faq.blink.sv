# Définissez votre compte Blink comme source de financement LNbits

Depuis la version LNbits v0.12.10, Blink peut être défini comme source de financement dans les paramètres du serveur LNbits.

Étapes de configuration :

\* obtenez une clé API Blink sur [dashboard.blink.sv] (https://dashboard.blink.sv). Trouvez plus de détails sur le tableau de bord et les clés API [ici] (https://dev.blink.sv/api/auth). 
\
\* connectez-vous en tant que [super utilisateur LNbits] (https://github.com/lnbits/lnbits/blob/dev/docs/guide/admin_ui.md)

\* ouvrez les paramètres `Serveur`

![] (<..../../.gitbook/assets/lnbits\_super\_user (1).png>)\


\* choisissez `Blink` dans le menu déroulant sous `Sources de financement` **-** `Financement actif (nécessite un redémarrage du serveur)` 
\* collez votre clé API dans le champ `Clé`

\
![] (..../../.gitbook/assets/lnbits\_funding\_sources.png)



\* redémarrez LNbits 
\
\* vous pouvez également modifier directement le fichier `.env` de LNbits si vous avez accès au terminal du serveur

