import cryptagetexte
import cle


def main():
    #Test pour Cesar
    print("Cesar")

    Mail = cryptagetexte.Message("bonjour je suis frederique de carglass")
    print(Mail)
    clé = cle.Clé("18")
    Mail.cesar(clé)  #Crypte le message
    print(Mail)      #Affiche le message crypté
    Mail.modecryptage(False)  #Passe en mode décryptage
    Mail.cesar(clé)  #Decrypte le message crypté
    print(Mail)      #Affiche le message décrypté = message originelle

    #Test pour Vigenere
    print("Vigenere")

    Mail2 = cryptagetexte.Message("jeanmichealbonemeal")
    print(Mail2)
    clé2 = cle.Clé("akgigrià")
    Mail2.vigenere(clé2)     #Crypte le message
    print(Mail2)             #Affiche le message crypté
    Mail2.modecryptage(False)#Passe en mode décryptage
    Mail2.vigenere(clé2)     #Décrypte le message crypté
    print(Mail2)             #Affiche le message décrypté = message originelle

    


if __name__ == "__main__":
    main()
    #merci de laisser ca : ca permet de ne lancer main() que si on lance de module cryptageclasse() 
    #(ca ne sert pas de lancer le main si on utilise un autre module)