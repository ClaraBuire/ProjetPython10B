import convertisseur 
import cle
#CE CODE EST TEMPORAIRE POUR DEBUGER LE RSA

def chififfrementRSA(texte,cle):
    nombre = convertisseur.textnumero(texte,False)
    nombrecryp = str((int(nombre)**int(cle.texte))%cle.modulo) #C = M**e [n] si c'est une clé public, M = C**d [n] si privée 
    print(nombrecryp) 
    texte = convertisseur.textnumero(nombrecryp,True)
    return texte

if __name__ == "main":
    message = "bonjour"
    clepublic, cleprive = cle.RSA("328000000.txt",2)
    mescry = chififfrementRSA(message,clepublic)
    print(mescry)
    messagesortie = chififfrementRSA(mescry,cleprive)
    print(messagesortie)