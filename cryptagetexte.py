import sys
import cle
import convertisseur

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

    def __repr__(self):
        return 'Message : ' + self.texte

    def modecryptage(self,on):
        """fixe le mode en cryptage ou en décryptage"""
        if on:
            self.cryptage = 1
        else:
            self.cryptage = -1

    def cesar(self,clé):
        """crypte/décrypte en césar, la clé est de type cle.Clé"""
        print("")
        mescrypte = ""
        for caractere in self.texte:
                n_ord = (ord(caractere)-VAI+int(clé.texte)*self.cryptage)%(lenASCII-VAI) + VAI #on souhaite faire que les caracteres entre 31 et 126 du code ascii
                #donc on decale de -31 (VAI) puis on fait notre decalage, et on sassure que la valeur reste entre 0 et 126-31=95, puis on refait +31 ravoir les caracteres en 31 et 126
                mescrypte += chr(n_ord) 
        self.texte = mescrypte
    
    def vigenere(self,clé):
        """crypte/décrypte en Vigenere, la clé est de type cle.Clé"""
        mescrypte = ""
        iclé = 0  #Ou l'on se situe dans le parcours de la clé (pour le décalage, d'ou iclé += 1)
        lclé = clé.longueur
        for caractere in self.texte:
            decalage = ord(clé.texte[iclé%lclé])  #decalage = poids du caractere regardé dans la clé
            #contrairement à césar, le décalage est different à chaque caractere, sinon même principe
            n_ord = (ord(caractere)-VAI+decalage*self.cryptage)%(lenASCII-VAI) + VAI
            mescrypte += chr(n_ord)  #on souhaite pas avoir les caracteres 0 à 31 et au dessus de 126 en ascii
            iclé += 1
        self.texte = mescrypte

    def chififfrementRSA(self,cle):
        textecryp = ""
        for caractere in self.texte:
            nombre = ord(caractere)
            nombrecryp = (int(nombre)**int(cle.texte))%cle.modulo #C = M**e [n] si c'est une clé public, M = C**d [n] si privée 
            textecryp += chr(nombrecryp)
        self.texte = textecryp
        return self.texte

"""
normalement le chiffrement RSA n'a pas besoins de chiffrer caractere par caractere mais les calculs pouvant être tres long et on a besoin de grand nombre premier pour crypter un long message
on a décidé ici d'adapter pour un soucis de rapidité (car on doit demontrer que notre chiffrement fonctionne en présentation)
mais voici le code du chiffrement RSA pour un texte complet si on avait une grande puissance de calcul pour de trés grande clé et cryptage.

def chififfrementRSA(texte,cle):
    nombre = convertisseur.textnumero(texte,False)
    nombrecryp = str((int(nombre)**int(cle.texte))%cle.modulo) #C = M**e [n] si c'est une clé public, M = C**d [n] si privée 
    texte = convertisseur.textnumero(nombrecryp,True)
    return texte
"""

           

