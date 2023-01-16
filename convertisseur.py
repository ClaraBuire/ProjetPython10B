###Fonction pour texte
#Conversion entier binaire
#fonction pour coder binaire d'un entier
N = 8

def binaire(nombre):
    code = ''
    for k in range(8):
        bit = nombre%2
        code = str(bit)+code
        nombre //=2
    return(code)

def nombre(binaire):
    n = 0
    for b in binaire:
        n = 2 * n + int(b)
    return n
#Codes ASCII
#liste des codes ASCII des caracteres d'une chaine de caractere
def liste_codes_ascii(chaine):
    L=[]
    for elt in chaine:
        L+=[ord(elt)]
    return(L)

#print(liste_codes_ascii("abc"))

def codage_binaire(phrase):
    k = len(phrase)
    code = binaire(k)
    for elt in liste_codes_ascii(phrase):
        code += binaire(elt)
    return code

def transfo(n,bit):
    if bit == 0 and n%2 == 1:
        if n == 255:
            return(254)
        else:
            return(n+1)
    if bit == 1 and n%2 == 0:
        return n+1
    else:
        return n

###Fonction pour Image
#concatene tous les caracteres correspondant aux entiers de la liste de codes ASCII
def convertir(liste_codes_ascii):
    a = ''
    for elt in liste_codes_ascii:
        a += chr(elt)
    return a

def convertir_en_chaine(phrase_binaire):
    n = len(phrase_binaire)
    liste_codes_ascii=[]
    for k in range(1,n+1):
        liste_codes_ascii+=[nombre(phrase_binaire[N*k:N*(k+1)])]
    return convertir(liste_codes_ascii)

def textnumero(texte, num=True):
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

