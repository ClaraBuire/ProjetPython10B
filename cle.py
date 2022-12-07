import RSAcle
class Clé:
    #classe pour les clés avec pour information, leur texte (un nombre pour cesar "8" qui sera converti en int dans le code, un mot pour vignere ...)
    #leurs longueur, et leur type (jsp pourquoi type, ça fait stylé)
    def __init__(self,clé):
        self.texte = str(clé)
        self.type = ""
        self.longueur = len(clé)

    def __repr__(self):
        return "clé" + self.texte



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

def cleRSA(ficher):
    n,e,d = RSAcle.RSA(ficher)
    clepublic = Clé(e)
    clepublic.type = "public"
    cleprive = Clé(d)
    cleprive.type = "privé"
    return clepublic,cleprive
    