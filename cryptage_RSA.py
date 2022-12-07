import random as r
#Le chiffrement RSA est asymétrique : il utilise une paire de clés (des nombres entiers)
#  composée d'une clé publique pour chiffrer et d'une clé privée pour déchiffrer des données confidentielles.
#Une condition indispensable est qu'il soit « calculatoirement impossible » de déchiffrer à l'aide de la seule clé publique


#tentative de faire le chiffrement RSA à la main

def entierhasard(ficher):
    ligne = r.randint(0,40000)
    with open(ficher,'r') as f:
        for (i,line) in enumerate(f):
            if i == ligne:
                return int(line)
def pgcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a

def mod_inverse1(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n

def euclideetendu(b,n):
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

    
    
def chiffrementRSA(ficher):
    #(n,e) la clé publique
    #(n,d) la clé privée généré ici
    p = entierhasard(ficher)
    q = entierhasard(ficher)
    n = p * q
    phin = (p-1)*(q-1)
    #e doit etre inferieur a phin et premier entre eux
    e = int(input("Donnez un chiffre e, premier avec phin, s'il ne l'est pas on trouvera un chiffre proche de e premier avec phin"))
    while pgcd(e,phin) != 1:
        e += 1 
    print(f"Voici votre clé publique : n = {n} et e = {e}")
    d = euclideetendu(e,phin)
    print(f"Voici votre clé privée : n = {n} et d = {d}")

def main():
    '''
    key = RSA.generate(2048) # key contient la clé pivée
    # key.publickey() donne la clé public
    print(key)
    '''

    ficher = "328000000.txt"
    chiffrementRSA(ficher)
main()



