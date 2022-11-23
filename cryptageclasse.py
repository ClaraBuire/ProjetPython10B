class Dictionnaire:
    def __init__(self):
        self.diclettre = {}
        self.dicpoids = {}
        self.longueur = 0

    def dic(self,Lalphabet,Lpoids):
        for (i,lettre) in enumerate(Lalphabet):
            self.diclettre[lettre]= Lpoids[i]
        self.dicpoids = {i: j for j, i in self.diclettre.items()}
        self.longueur = len(Lalphabet)

class Message:
    def __init__(self,texte,dicoalphapoids):
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
        self.clé = clé
        mescrypte = ""
        for caractere in self.texte.lower():
            if caractere.isalpha():
                mescrypte += self.dico.dicpoids.get((self.cryptage*int(self.clé) + self.dico.diclettre[caractere])%self.dico.longueur)
            else:
                mescrypte += caractere
        self.texte = mescrypte
    
    def vigenere(self,clé):
        self.clé = clé
        mescrypte = ""
        iclé = 0  #plus tard faire de la clé une classe
        lclé = len(clé)
        for caractere in self.texte.lower():
            if caractere.isalpha():
                decalage = self.dico.diclettre[clé[iclé%lclé]]
                mescrypte += self.dico.dicpoids.get((self.cryptage*decalage + self.dico.diclettre[caractere])%self.dico.longueur)
            else:
                mescrypte += caractere
            iclé += 1
        self.texte = mescrypte
        

    def __repr__(self):
        return 'Message : ' + self.texte

def main():
    Lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","é","è","ê","ù"]
    Lpoids = [i for i in range(0,len(Lalphabet))]
    dicoalphapoids = Dictionnaire()
    dicoalphapoids.dic(Lalphabet,Lpoids)
    Mail = Message("bonjour je suis frédérique de carglass",dicoalphapoids)
    print(Mail)
    #César
    print("César")
    clé = "18"
    Mail.cesar(clé)
    print(Mail)
    Mail.modecryptage(False)
    Mail.cesar("18")
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

main()

'''
Cryptage des espaces / caractère
Cryptage Asymétrique
Interface Asymetrique
'''

class Clé:
    def __init__(self,clé,longueur):
        self.clé = clé
        self.longueur = len(clé)

class Image:
    pass

class AttaqueMessage:
    pass


