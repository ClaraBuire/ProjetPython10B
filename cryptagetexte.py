import sys
import cle

lenASCII = 126  #nombre de caractere en ascii
VAI = 31 #valeur indésirable de 0 à 31 en ascii

class Message:
    #classe pour les messages
    #self.texte, l'information du message
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
                n_ord = (self.cryptage*int(clé.texte) + ord(caractere))%lenASCII
                if 0<=n_ord<=VAI :
                    n_ord = (n_ord+self.cryptage*VAI)%lenASCII  #on souhaite pas avoir les caracteres 0 à 31 en ascii 
                #on cherche la lettre associé au poids (+- clé + poids associé au caractère) (moduloc126, le nombre de caractere ASCII°
                mescrypte += chr(n_ord)
        self.texte = mescrypte
    
    def vigenere(self,clé):
        mescrypte = ""
        iclé = 0  #Ou l'on se situe dans le parcours de la clé (pour le décalage, d'ou iclé += 1)
        lclé = clé.longueur
        for caractere in self.texte:
            decalage = ord(clé.texte[iclé%lclé])  #decalage = poids du caractere regardé dans la clé
            #contrairement à césar, le décalage est different à chaque caractere, sinon même principe
            n_ord = (self.cryptage*decalage + ord(caractere))%lenASCII
            if 0<=n_ord<=VAI :
                n_ord = (n_ord+self.cryptage*VAI)%lenASCII  #on souhaite pas avoir les caracteres 0 à 31 en ascii
            mescrypte += chr(n_ord)
            iclé += 1
        self.texte = mescrypte
        
    def __repr__(self):
        return 'Message : ' + self.texte

    def chififfrementRSA(self,cle):
        nombre = convertisseurtextnumero(self.texte,False)
        nombrecryp = str((int(nombre)**int(cle.texte))%cle.modulo) #C = M**e [n] si c'est une clé public, M = C**d [n] si privée 
        self.texte = convertisseurtextnumero(nombrecryp,True)
        return self.texte

def convertisseurtextnumero(texte, num=True):
    """Converti un texte en un nombre en base 10 et inversement pour le chiffrage RSA"""
    if num:
        #nombre au texte
        charactere = []
        nombre = int(texte)
        while nombre > 0:
            charactere.append(chr(nombre % 256))
            nombre = nombre // 256
        return "".join(reversed(charactere))
    else:
        #texte au nombre
        mesnum = 0
        for charactere in texte:
            mesnum = mesnum * 256 + ord(charactere)
        return mesnum



           

