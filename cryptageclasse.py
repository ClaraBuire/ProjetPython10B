import sys
sys.set_int_max_str_digits(1000000)


class Dictionnaire:
    def __init__(self):
        self.diclettre = {}
        self.dicpoids = {}
        self.longueur = 0

    def dic(self, Lalphabet, Lpoids):
        for (i,lettre) in enumerate(Lalphabet):
            self.diclettre[lettre]= Lpoids[i]
        self.dicpoids = {i: j for j, i in self.diclettre.items()}
        self.longueur = len(Lalphabet)

    def __repr__(self):
        return "dico lettre : " + self.diclettre + "et dico poids : " + self.dicpoids

def info_dico():
    Lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","é","è","ê","ù"," ","@",".",",",";","?","!","+","-","/","*","0","1","2","3","4","5","6","7","8","9","10"]
    n=len(Lalphabet)
    Lpoids = [i for i in range(n)]
    dicoalphapoids = Dictionnaire()
    dicoalphapoids.dic(Lalphabet,Lpoids)
    return dicoalphapoids

class Message:
    def __init__(self,texte,dicoalphapoids=info_dico()):
        self.texte = texte
        self.dico = dicoalphapoids
        self.clé = ""
        self.cryptage = 1

    def modecryptage(self,on):
        if on == True:
            self.cryptage = 1
        else:
            self.cryptage = -1

    def cesar(self,clé):
        self.clé = clé.texte
        mescrypte = ""
        for caractere in self.texte.lower():
            if caractere in self.dico.diclettre:
                mescrypte += self.dico.dicpoids.get((self.cryptage*int(self.clé) + self.dico.diclettre[caractere])%self.dico.longueur)
            else:
                mescrypte += caractere
        self.texte = mescrypte
    
    def vigenere(self,clé):
        self.clé = clé.texte
        mescrypte = ""
        iclé = 0 
        lclé = clé.longueur
        for caractere in self.texte.lower():
            if caractere in self.dico.diclettre:
                decalage = self.dico.diclettre[clé[iclé%lclé]]
                mescrypte += self.dico.dicpoids.get((self.cryptage*decalage + self.dico.diclettre[caractere])%self.dico.longueur)
            else:
                mescrypte += caractere
            iclé += 1
        self.texte = mescrypte
        
    def __repr__(self):
        return 'Message : ' + self.texte

class Clé:
    def __init__(self,clé):
        self.texte = clé
        self.type = ""
        self.longueur = len(clé)

    def __repr__(self):
        return self.texte

def DiffieHellman():
    #Programme pour echanger les clés publics privés
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
    DiffieHellman()
    '''
    Lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","é","è","ê","ù"," ","@",".",",",";","?","!","+","-","/","*","0","1","2","3","4","5","6","7","8","9","10"]
    Lpoids = [i for i in range(0,len(Lalphabet))]
    dicoalphapoids = Dictionnaire()
    dicoalphapoids.dic(Lalphabet,Lpoids)
    Mail = Message("bonjour je suis frédérique de carglass",dicoalphapoids)
    print(Mail)
    #César
    print("César")
    clé = Clé("18")
    Mail.cesar(clé)
    print(Mail)
    Mail.modecryptage(False)
    Mail.cesar(clé)
    print(Mail)
    #Vigenere
    print("Vigenere")
    Mail2 = Message("Andreas.Clara@donnenousunebonnenote.com",dicoalphapoids)
    print(Mail2)
    Mail2.vigenere("niouininon")
    print(Mail2)
    Mail2.modecryptage(False)
    Mail2.vigenere("niouininon")
    print(Mail2)
    '''
main()


class Image:
    pass

class AttaqueMessage:
    def __init__(self,dico):
        self.typecraquage = ""
        self.mescrypte = ""
        self.dico = dico
    '''
    def craquagecesar(self,mescrypte,alphabet):
        # E étant de loin la lettre la plus utilisée en français on cherche le decalage par rapport à E
        l = len(alphabet)
        Lf = analysefrequentielle(mescrypte,alphabet)
        imaxf = 0
        maxf = 0
        for (i,f) in enumerate(Lf):
            if f > maxf:
                imaxf = i 
                maxf = f
        return (imaxf-4)%l  #indice de la lettre la plus recurente - l'indice de e (modulu la longueur de la liste)
        

    def analysefrequentielle(self,mescrypte,alphabet):
    l = len(alphabet)
    dic = dictionaire(alphabet,[i for i in range(0,l)])
    Lfrequence = [0]*l
    for caractere in mescrypte.lower():
        if caractere.isalpha():
            Lfrequence[dic[caractere]] += 1   #on compte les itérations de chaque caractere
    for elt in Lfrequence:
        elt = elt/l #on passe en frequence
    return Lfrequence
    '''




