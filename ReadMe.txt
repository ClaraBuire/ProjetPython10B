Crée par LA DREAM TEAM : Antony LOMBARDO, Wenli XU, Lucie VIAL, Rémi MICHAUX

EXECUTION DU CODE:
Pour lancer l'interface : lancer le fichier main.py
Pour lancer le cryptage lié aux Gifs : reportez vous à la section 'CRYPTAGE GIF' ci-dessous

AVERTISSEMENTS:
- Certaines fonctionnalitées liées aux images peuvent ne pas fonctionner sous windows, notamment à cause de la fonction save du module PIL
- Pour (dé)crypter une image dans une image, il faut que les deux images aient exactement les mêmes dimensions. Cela peut néamoins fonctionner dans d'autres cas mais il n'y a aucune garantie
- L'échange des clés nécessite le fichier premier.txt 
- Le cryptage dans les GIFs est indépendant de l'interface et doit être lancé à part
- Le cryptage RSA (page 1) peut utiliser les clés générées en page 3 : dans ce cas, générer les clés (page 3), 
  ne PAS appuyer sur clear et continuer le cryptage (page 1) en entrant la clé et en laissant le champ Modulo à 0.
  Pour crypter en RSA : entrer la clé publique / pour décrypter : entrer la clé privée
- Le cryptage GIF est un prototype, indépendant du reste du code


Pour utiliser les fonctionaliées sans l'interface :
- Cryptage texte dans une image : utiliser la class texteinpicture du module cryptageimage.py
- Cryptage image dans une image : utiliser la class pictureinpicture du module cryptageimage.py
- Echanges de clés : utiliser les fonctions DiffieHellman et RSA du module cle.py
- Cryptage RSA : utiliser la fonction chiffrementRSA du module cryptagetexte.py
- Cryptages César et Vigenere : appeller les fonctions cesar ou vigenere du module cryptagetexte.py
- Pour crypter une image : lancer les fonctions texttoimage ou imagetotext du module cryptageimage.py


STRUCTURE DU CODE:
- Module cle.py:
Classe Clé pour tout type de cryptage nécessitant une clé
Fonctions utiles pour toutes opérations liées aux clés, voir directement dans le module
Les clés RSA utilisent le fichier premier.txt au lieu de les générer aléatoirement
A noter que le ficher premier.txt ici fourni n'est que des petits nombres entiers pour des soucis de performances (sinon les calculs prenent plusieurs minutes)

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
Généré avec QtDesigner jusqu'à la ligne 1049, relié à partir de la ligne 1050 par nos soins
les fonctions dont le nom commence par "clear_" servent à remettre l'interface dans sa position initialeen utilisant les boutons CLEAR
les fonctions dont le nom commence par "copie_" servent à copier dans le presse papier les sorties texte et sont reliées aux boutons COPIE
les autres fonctions servent à relier les fonctionnalitées des modules ci-dessus à l'interface. Elles sont appelées par les boutons de l'interface.


CRYPTAGE GIF
Ce module n'est qu'une ébauche pour montrer qu'il est possible de cacher un message dans un GIF
Ce n'est qu'un prototype et c'est pour cette raison qu'il n'est pas executable depuis l'interface

Attention, ce module est prévu pour fonctionner sous linux
Pour faire le faire fonctionner sous windows : changer les / par des \ aux lignes 77, 79, 97, 105

Pour creer un GIF : (on peut aussi en utiliser un déjà fait. Dans ce cas, le mettre image par image dans un dossier GIF)
- Creer un dossier GIF dans le dossier actuel, il stockera le gif image par image
- Lancer la fonction cree_gif() qui prend en parametre le nom du gif que vous voulez enregistrer
Par défaut, cette fonction cree un GIF coeur en 50 images. Pour en creer un autre, changer les équations paramétriques lignes 71 et 72

Pour cacher un texte dans un GIF :
- Creer un dossier GIF_modifie dans le dossier actuel
- Lancer la fonction main_emetteur
Attention : Il vous sera alors demandé de rentrer le chemin d'accès de votre PREMIERE IMAGE du GIF, ne pas passer en paramètre le fichier coeur.gif

Pour sortir un texte d'un GIF, lancer la fonction main_recepeteur