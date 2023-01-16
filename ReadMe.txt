Ce fichier contient les informations nécessaires à l'execution du code.
Merci de lire à minima les avertissements avant execution.

AVERTISSEMENTS:
- Certaines fonctionnalitées liées aux images peuvent ne pas fonctionner sous windows
  En cas de problème de chemin d'accès ou d'erreur venant de la fonction save du module PIL, réessayer sous linux
- L'échange des clés nécessite le fichier 328000000.txt qui contient plein de grands nombres
- Le cryptage dans les GIFs est indépendant de l'interface et doit être lancé à part
- Le cryptage RSA (page 1) peut utiliser les clés générées en page 3 : dans ce cas, générer les clés (page 3), 
  ne PAS appuyer sur clear et continuer le cryptage (page 1) en entrant la clé et en laissant le champ Modulo à 0.

EXECUTION DU CODE:
Pour lancer l'interface : lancer le fichier main.py
Pour lancer le cryptage lié aux Gifs : lancer gif.py

Pour utiliser les fonctionaliées sans l'interface :
- Cryptage texte dans une image : utiliser la class texteinpicture du module cryptageimage.py
- Cryptage image dans une image : utiliser la class pictureinpicture du module cryptageimage.py
- Echanges de clés : utiliser les fonctions DiffieHellman et RSA du module cle.py
- Cryptage RSA : utiliser le module RSA.py comme dans le test disponible en fin de module
- Cryptages César et Vigenere : appeller les fonctions cesar ou vigenere du module cryptagetexte.py
- Pour crypter une image : lancer les fonctions texttoimage ou imagetotext du module cryptageimage.py

STRUCTURE DU CODE:
- Module cle.py:
Classe Clé pour tout type de cryptage nécessitant une clé
Fonctions utiles pour toutes opérations liées aux clés, voir directement dans le module
Les clés RSA utilisent le fichier 328000000.txt au lieu de les générer aléatoirement

- Module convertisseur.py:
Ne contient pas de classe
Utile pour tout type de convertion, notamment en binaire, texte en ASCII, nombre en binaire, texte en nombre base 10

- Module cryptageimage.py:
Module principal pour les images
Classe texteinpicture sert à (dé)crypter un texte dans une image
Classe pictureinpicture sert à (dé)crypter une image NOIR ET BLANC dans une image
Fonctions imagetotext et texttoimage servent à convertir une image en texte et un texte en image

- Module cryptagetexte:
Module principal pour le texte
Classe Message contient toutes les fonctions nécessaires au (dé)cryptage en César, Vigenère, RSA
Ces fonctions prennent toutes un objet de type Message et une clé de type Clé (module cle.py) en entrée et changent l'attribut texte du Message

- Module main.py:
Interface PyQt5 
Généré via QtDesigner jusqu'à la ligne 1049
les fonctions dont le nom commence par "clear_" servent à remettre l'interface dans sa position initialeen utilisant les boutons CLEAR
les fonctions dont le nom commence par "copie_" servent à copier dans le presse papier les sorties texte et sont reliées aux boutons COPIE
les autres fonctions servent à relier les fonctionnalitées des modules ci-dessus à l'interface. Elles sont appelées par les boutons de l'interface.
