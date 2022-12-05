#import RSA
import random as r
#Le chiffrement RSA est asymétrique : il utilise une paire de clés (des nombres entiers)
#  composée d'une clé publique pour chiffrer et d'une clé privée pour déchiffrer des données confidentielles.
#Une condition indispensable est qu'il soit « calculatoirement impossible » de déchiffrer à l'aide de la seule clé publique


#tentative de faire le chiffrement RSA à la main

def entierhasard(ficher):
    random = r.randint(40000)
    with open(ficher,'r') as f:
        for (i,line) in enumerate(f):
            if i == random:
                return line
def pgcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a

def chiffrementRSA(ficher):
    #(n,e) la clé publique
    #(n,d) la clé privée généré ici
    p = entierhasard(ficher)
    q = entierhasard(ficher)
    n = p * q
    phin = (p-1)*(q-1)
    #e doit etre inferieur a phin et premier entre eux
    e = int(input("Donnez un chiffre e, premier avec phin, s'il ne l'ai pas on trouvera un chiffre proche de e premier avec phin"))
    while pgcd(e,phin) != 1:
        e += 1
    
        
        

def main():
    '''
    key = RSA.generate(2048) # key contient la clé pivée
    # key.publickey() donne la clé public
    print(key)
    '''

    ficher = "328000000.txt"
    chiffrementRSA(ficher)
main()



