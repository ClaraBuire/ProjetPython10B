import sys
import cle

lenASCII = 126  #nombre de caractere en ascii
VAI = 31 #valeur indésirable de 0 à 31 en ascii

class Message:
    #classe pour les messages
    #self.texte, l'information du message
    #self.dico, le dictionaire du message, dans notre cas c'est l'alphabet latin + caractère @!...
    #self.cryptage, 1 si on crypte, -1 si on décrypte
    #ps : j'ai enlever self.clé étant donné que l'on a une classe clé
    def __init__(self,texte):
        self.texte = texte
        self.cryptage = 1

    def modecryptage(self,on):  #ps : c'est clairement pas optimisé comme truc
        if on == True:
            self.cryptage = 1
        else:
            self.cryptage = -1

    def cesar(self,clé):
        mescrypte = ""
        for caractere in self.texte:
                n_ord = self.cryptage*int(clé.texte) + ord(caractere)%lenASCII
                if 0<=n_ord<=VAI :
                    n_ord += self.cryptage*VAI  #on souhaite pas avoir les caracteres 0 à 31 en ascii 
                #on cherche la lettre associé au poids (+- clé + poids associé au caractère) (moduloc126, le nombre de caractere ASCII°
                mescrypte += chr()
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

    def chiffrementRSA(self,cle):
        if cle.type == "public":
            pass
        elif cle.type == "prive":
            pass


