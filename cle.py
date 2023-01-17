import random as r
#Le chiffrement RSA est asymétrique : il utilise une paire de clés (des nombres entiers)
#  composée d'une clé publique pour chiffrer et d'une clé privée pour déchiffrer des données confidentielles.
#Une condition indispensable est qu'il soit « calculatoirement impossible » de déchiffrer à l'aide de la seule clé publique


class Clé:
    #classe pour les clés avec pour information, leur texte (un nombre pour cesar "8" qui sera converti en int dans le code, un mot pour vignere ...)
    #leurs longueur, et pour les clés RSA leur modulo
    def __init__(self,clé):
        self.texte = str(clé)
        self.modulo = 1   #utile que pour RSA
        self.longueur = len(str(clé))

    def __repr__(self):
        return "clé : " + self.texte



def DiffieHellman():
    """echanger les clés publics privés"""
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

def entierhasard(ficher='328000000.txt'):
    """parmi un ficher de plusieurs millers nombre premiers, on selectionne un au hasard"""
    ligne = r.randint(0,len(ficher))
    with open(ficher,'r') as f:
        for (i,line) in enumerate(f):
            if i == ligne:
                return int(line)
def pgcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a

def euclideetendu(b,n):
    """permet de trouver l'inverse modulaire de b module n, (cad trouver x dans b*x = 1 [n])"""
    n0 = n
    b0 = b
    t0 = 0
    binv = 1
    q = n0 // b0
    r = n0 - q * b0
    while r > 0 :
        temp = t0 - q * binv
        if temp >= 0:
            temp = temp % n
        else:
            temp = n - (-temp%n)
        t0 = binv
        binv = temp
        n0 = b0
        b0 = r
        q = n0 // b0
        r = n0 - q * b0
    if b0 != 1:
        return None
    else :
        return binv
    
def RSA(ficher,e):
    #(n,e) la clé publique
    #(n,d) la clé privée généré ici
    #e doit etre inferieur a phin et premier entre eux
    p = entierhasard(ficher)
    q = entierhasard(ficher)
    n = p * q
    phin = (p-1)*(q-1)
    while pgcd(e,phin) != 1:
        e += 1 
    d = euclideetendu(e,phin)
    clepublic = Clé(e)
    clepublic.modulo = n
    cleprive = Clé(d)
    cleprive.modulo = n
    return clepublic,cleprive
