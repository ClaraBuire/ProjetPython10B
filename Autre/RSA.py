import convertisseur 
import cle
#CE CODE EST TEMPORAIRE POUR DEBUGER LE RSA

def chififfrementRSA(texte,cle):
    textecryp = ""
    for caractere in texte:
        nombre = ord(caractere)
        nombrecryp = (int(nombre)**int(cle.texte))%cle.modulo #C = M**e [n] si c'est une clé public, M = C**d [n] si privée 
        textecryp += chr(nombrecryp)
    return textecryp

if __name__ == "__main__":
    message = "coucou"
    clepublic, cleprive = cle.RSA("premier.txt",2)
    print(clepublic,cleprive)
    mescry = chififfrementRSA(message,clepublic)
    print(mescry)
    messagesortie = chififfrementRSA(mescry,cleprive)
    print(messagesortie)


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