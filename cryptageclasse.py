import sys
sys.set_int_max_str_digits(1000000) #permet l'affichage de trés grand str, utile pour les clés de Diffie Hellman


class Dictionnaire:
    #classe qui permet de crée 2 dictionnaire, un premier donnant le poids pour chaque caractere (lettre) et un deuxième qui est l'inverse
    def __init__(self):
        #diclettre : {caractere : poids}
        #dicpoids : {poids : caractere}
        self.diclettre = {}
        self.dicpoids = {}
        self.longueur = 0

    def dic(self, Lalphabet, Lpoids):
        #creation des dictionnaires
        for (i,lettre) in enumerate(Lalphabet):
            self.diclettre[lettre]= Lpoids[i]
        self.dicpoids = {i: j for j, i in self.diclettre.items()}
        self.longueur = len(Lalphabet)

    def __repr__(self):
        return "dico lettre : " + self.diclettre + "et dico poids : " + self.dicpoids

def info_dico():
    #cette fonction crée directement tt les 
    Lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","é","è","ê","ù"," ","@",".",",",";","?","!","+","-","/","*","0","1","2","3","4","5","6","7","8","9","10"]
    n=len(Lalphabet)
    Lpoids = [i for i in range(n)]   
    dicoalphapoids = Dictionnaire()
    dicoalphapoids.dic(Lalphabet,Lpoids)
    return dicoalphapoids

class Message:
    #classe pour les messages
    #self.texte, l'information du message
    #self.dico, le dictionaire du message, dans notre cas c'est l'alphabet latin + caractère @!...
    #self.cryptage, 1 si on crypte, -1 si on décrypte
    #ps : j'ai enlever self.clé étant donné que l'on a une classe clé
    def __init__(self,texte,dicoalphapoids=info_dico()):
        self.texte = texte
        self.dico = dicoalphapoids
        self.cryptage = 1

    def modecryptage(self,on):  #ps : c'est clairement pas optimisé comme truc
        if on == True:
            self.cryptage = 1
        else:
            self.cryptage = -1

    def cesar(self,clé):
        mescrypte = ""
        for caractere in self.texte.lower():
            if caractere in self.dico.diclettre:
                #on cherche la lettre associé au poids (+- clé + poids associé au caractère) (modulo la longueur de l'alphabet pour passer de z à a par exemple)
                mescrypte += self.dico.dicpoids.get((self.cryptage*int(clé.texte) + self.dico.diclettre[caractere])%self.dico.longueur)
            else:
                #si le caractere n'est pas dans la liste des caracteres pris en compte, on le crypte pas
                mescrypte += caractere
        self.texte = mescrypte
    
    def vigenere(self,clé):
        mescrypte = ""
        iclé = 0  #Ou l'on se situe dans le parcours de la clé (pour le décalage, d'ou iclé += 1)
        lclé = clé.longueur
        for caractere in self.texte.lower():
            if caractere in self.dico.diclettre:
                decalage = self.dico.diclettre[clé.texte[iclé%lclé]]  #decalage = poids du caractere regardé dans la clé
                #contrairement à césar, le décalage est different à chaque caractere, sinon même principe
                mescrypte += self.dico.dicpoids.get((self.cryptage*decalage + self.dico.diclettre[caractere])%self.dico.longueur)
            else:
                mescrypte += caractere
            iclé += 1
        self.texte = mescrypte
        
    def __repr__(self):
        return 'Message : ' + self.texte

class Clé:
    #classe pour les clés avec pour information, leur texte (un nombre pour cesar "8" qui sera converti en int dans le code, un mot pour vignere ...)
    #leurs longueur, et leur type (jsp pourquoi type, ça fait stylé)
    def __init__(self,clé):
        self.texte = clé
        self.type = ""
        self.longueur = len(clé)

    def __repr__(self):
        return self.texte

def DiffieHellman():
    #Programme pour echanger les clés publics privés
    #Utilisation du calcul d'expondentielle trés élévee, rendant quasi impossible le chemin inverse avec le log
    try:
        g = int(input("User1 : Veuillez entrez un entier g (entre 2 et 9 :) "))
        a = int(input("User1 : Veuillez entrez un entier a, qui sera votre clé privé (entre 1 et 999): "))
        A = g**a   #clé public de user1
        print("User2 : Voici la clé public de User1 : ",A,"et l'entier g choisi (entre 1 et 999) : ",g)
        b = int(input("User2 : Veuillez entrez un entier b, qui sera votre clé privé :"))
        B = g**b
        print("User1 : Voici la clé public de User2 : B = ",B)
        Xuser1 = Clé(str(B**a))
        print("User1 : Voici la clé secrete partagé avec User2 :",Xuser1)
        Xuser2 = Clé(str(A**b))
        print("User2 : Voici la clé secrete partagé avec User1 :",Xuser2)
        #Xuser1 = Xuser2 mais chaqu'un fait son propre calcul avec ces infos
        return Xuser1,Xuser2
    except TypeError:
        print("Erreur : Veuillez recommencez le programme d'échanges de clé")



def main():
    #Test pour Cesar
    print("Cesar")

    Mail = Message("bonjour je suis frédérique de carglass")
    print(Mail)
    clé = Clé("18")
    Mail.cesar(clé)  #Crypte le message
    print(Mail)      #Affiche le message crypté
    Mail.modecryptage(False)  #Passe en mode décryptage
    Mail.cesar(clé)  #Decrypte le message crypté
    print(Mail)      #Affiche le message décrypté = message originelle

    #Test pour Vigenere
    print("Vigenere")

    Mail2 = Message("Andreas.Clara@donnenousunebonnenote.com")
    print(Mail2)
    clé2 = Clé("abracadabra")
    Mail2.vigenere(clé2)     #Crypte le message
    print(Mail2)             #Affiche le message crypté
    Mail2.modecryptage(False)#Passe en mode décryptage
    Mail2.vigenere(clé2)     #Décrypte le message crypté
    print(Mail2)             #Affiche le message décrypté = message originelle

if __name__ == "__main__":
    main()
    #merci de laisser ca : ca permet de ne lancer main() que si on lance de module cryptageclasse() 
    #(ca ne sert pas de lancer le main si on utilise un autre module)
