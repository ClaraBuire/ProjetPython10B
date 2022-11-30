from PIL import Image
import matplotlib.image as mpimg
import numpy as np

###Fonction pour texte
#Conversion entier binaire
#fonction pour coder binaire d'un entier
def binaire(nombre):
    code = ''
    for k in range(8):
        bit = nombre%2
        code = str(bit)+code
        nombre //=2
    return(code)
N = 8
# def binaire(nombre):
#     bin = ''
#     for _ in range(N):
#         bin = str(nombre%2)+bin
#         nombre = nombre // 2
#     return(bin)
#fonction pour coder en entier un binaire
# def nombre(binaire):
#     n = 0
#     for k in range(8):
#         n+=2**k**int(binaire[7-k])
#     return n
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
# def liste_codes_ascii(chaine):
#     L = []
#     for k in chaine :
#         L.append(ord(str(k)))
#     return(L)
#renvoie le code binaire de la phrase convertie en ascii
def codage_binaire(phrase):
    k = len(phrase)
    code = binaire(k)
    for elt in liste_codes_ascii(phrase):
        code += binaire(elt)
    return code
# def codage_binaire(phrase):
#     c = binaire(2)
#     L = liste_codes_ascii(phrase)
#     for n in L:
#         c+= binaire(n)
#     return(c)

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
# def transfo(n,bit):
#     if bit == 0 and n%2 != 0 :
#         n+=1
#     if bit == 1 and n%2 == 0 :
#         n+=1
#     return(n)
###Fonction pour Image
#concatene tous les caracteres correspondant aux entiers de la liste de codes ASCII
def convertir(liste_codes_ascii):
    a = ''
    for elt in liste_codes_ascii:
        a += chr(elt)
    return a
# def convertir(liste_codes_ascii):
#     C=''
#     for k in liste_codes_ascii:
#         C+= chr(k)
#     return C
#convertit une chaine binaire en chaine de caractere
# def convertir_en_chaine(phrase_binaire):
#     k = nombre(phrase_binaire[:8])
#     liste_codes_ascii = []
#     for i in range(1,k+1):
#         code_ascii = nombre(phrase_binaire[9*i:8*i+8])
#         liste_codes_ascii += [code_ascii]
#     return convertir(liste_codes_ascii)
def convertir_en_chaine(phrase_binaire):
    n = len(phrase_binaire)
    liste_codes_ascii=[]
    for k in range(1,n+1):
        liste_codes_ascii+=[nombre(phrase_binaire[N*k:N*(k+1)])]
    return convertir(liste_codes_ascii)

###Class du programme
class texteinpicture():
    def __init__(self,phrase,M):
        self.M = M
        self.phrase = phrase

    def camouflage(self):
        H,L = self.M.shape[0],self.M.shape[1]
        C = np.copy(self.M)
        code = codage_binaire(self.phrase)
        N = len(code)
        i,k = 0,0
        while i<=H-1 and k<=N-1:
            j = 0
            while j<= L-1 and k<= N-1:
                C[i,j,0] = transfo(self.M[i,j,0], int(code[k]))
                j += 1
                k += 1
            i += 1
        image_C = Image.fromarray(C)
        image_C.show()
        #return C

    # def extraction(self):
    #     codebin = ''
    #     (H,L,P) = self.M.shape
    #     for i in range(H):
    #         for j in range(L):
    #             if self.M[i,j,0]%2==0:
    #                 codebin += '0'
    #             else:
    #                 codebin += '1'
    #     phrase = convertir_en_chaine(codebin)
    #     return(phrase)


    def extraction(self):
        H,L = self.M.shape[0],self.M.shape[1]
        i,k = 0,0
        binaire = ''
        while i<= H-1 and k<=7:
            j = 0
            while j<= L-1 and k <= 7:
                if self.M[i,j,0]%2 == 0:
                    binaire += '0'
                else:
                    binaire += '1'
                j += 1
                k += 1
            i += 1
        Noctets = nombre(binaire)*8
        i,j,k = 8//L,8-(8//L)*L,0
        phrase_binaire = ''
        while i <= H-1 and k<= Noctets-1:
            while j<= L-1 and k<=Noctets-1:
                if self.M[i,j,0]%2 == 0:
                    phrase_binaire += '0'
                else:
                    phrase_binaire += '1'
                j += 1
                k += 1
            i += 1
            j = 0
        return convertir_en_chaine(binaire+phrase_binaire)

class pictureinpicture():
    def __init__(self,matriceimg,imageacacher):
        self.matriceimg = matriceimg
        self.imageacacher = imageacacher
    #Camouflage/Extraction d'une image dans une autre image
    #Extraction d'une image en noir et blanc d'une image support
    def extraction_image(self):
        H,L = self.matriceimg.shape[0],self.matriceimg.shape[1]
        C = np.zeros((H,L))
        for i in range(H):
            for j in range(L):
                if self.matriceimg[i,j,1]%2 == 0:
                    C[i,j] = 0
                else:
                    C[i,j] = 255
        image_C = Image.fromarray(C)
        image_C.show()
    #camoufle la matrice I d'une image en noir et blanc
    def camouflage_image(self):
        HM,LM = self.matriceimg.shape[0], self.matriceimg.shape[1]
        HI, LI = self.imageacacher.shape[0], self.imageacacher.shape[1]
        C = np.copy(self.matriceimg)
        for i in range(HM):
            for j in range(LM):
                if i in range(HI) and j in range(LI):
                    bit = self.imageacacher[i,j]//255
                    C[i,j,1] = transfo(self.matriceimg[i,j,1], bit)
                else:
                    C[i,j,1] = transfo(self.matriceimg[i,j,1],1)
                image_C = Image.fromarray(C)
                image_C.show()
                return C

# class main(texteinpicture, pictureinpicture):
#     message = input("Veuillez choisir si vous voulez coder/décoder un texte dans une image(taper t) ou une image(taper i) ")
#     if message == 'i':
#         message2 = input("Veuillez choisir si vous voulez cacher une image dans l'image support(taper c) ou bien reveler une image cacher(taper r)")
#         if message2 == 'c':
#             matrice = input("Entrez le chemin de votre image en noir et blanc à cacher")
#             mon_image = Image.open(matrice)
#             Mat = np.array(mon_image)
#             matrice2 = input("Entrez le chemin de votre image support")
#             mon_image2 = Image.open(matrice2)
#             Mat2 = np.array(mon_image2)
#             camoufimg = pictureinpicture(Mat2,Mat)
#             print(camoufimg.camouflage_image())
#         elif message2 == 'r':
#             matrice = input("Entrez le chemin de votre image support")
#             mon_image = Image.open(matrice)
#             mat = np.array(mon_image)
#             revelimg = pictureinpicture(mat,np.zeros(5))
#             print(revelimg.extraction_image())
#         else:
#             raise ValueError("Vous n'avez pas tapé les bons caractères")
#     elif message == 't':
#         message2 = input("Veuillez choisir si vous voulez cacher un texte dans l'image support(taper c) ou bien reveler un texte caché dans une image (taper r)")
#         if message2 == 'r':
#             matrice = input("Entrez le chemin de votre image")
#             mon_image = Image.open(matrice)
#             Mat = np.array(mon_image)
#             revelimg = texteinpicture('',Mat)
#             print(revelimg.extraction())
#         elif message2 == 'c':
#             matrice = input("Entrez le chemin de votre image ou vous voulez cacher le texte")
#             mon_image = Image.open(matrice)
#             Mat = np.array(mon_image)
#             txt = input("Entrez le texte que vous voulez cacher")
#             cachimg = texteinpicture(txt,Mat)
#             #print(cachimg.camouflage())
#             Mat2 = cachimg.camouflage()
#             revelimg = texteinpicture('',Mat2)
#             print(revelimg.extraction())
#         else:
#             raise ValueError("Vous n'avez pas tapé les bons caractères")
#     else :
#         raise ValueError("Vous n'avez pas tapé les bons caractères")


class main(texteinpicture, pictureinpicture):
    message = input("Veuillez choisir si vous voulez coder/décoder un texte dans une image(taper t) ou une image(taper i) ")
    if message == 'i':
        message2 = input("Veuillez choisir si vous voulez cacher une image dans l'image support(taper c) ou bien reveler une image cacher(taper r)")
        if message2 == 'c':
            matrice = input("Entrez le chemin de votre image en noir et blanc à cacher")
            mon_image = Image.open(matrice)
            Mat = np.array(mon_image)
            matrice2 = input("Entrez le chemin de votre image support")
            mon_image2 = Image.open(matrice2)
            Mat2 = np.array(mon_image2)
            camoufimg = pictureinpicture(Mat2,Mat)
            print(camoufimg.camouflage_image())
        elif message2 == 'r':
            matrice = input("Entrez le chemin de votre image support")
            mon_image = Image.open(matrice)
            mat = np.array(mon_image)
            revelimg = pictureinpicture(mat,np.zeros(5))
            print(revelimg.extraction_image())
        else:
            raise ValueError("Vous n'avez pas tapé les bons caractères")
    elif message == 't':
        message2 = input("Veuillez choisir si vous voulez cacher un texte dans l'image support(taper c) ou bien reveler un texte caché dans une image (taper r)")
        if message2 == 'r':
            matrice = input("Entrez le chemin de votre image")
            mon_image = Image.open(matrice)
            Mat = np.array(mon_image)
            revelimg = texteinpicture('',Mat)
            print(revelimg.extraction())
        elif message2 == 'c':
            matrice = input("Entrez le chemin de votre image ou vous voulez cacher le texte")
            mon_image = Image.open(matrice)
            Mat = np.array(mon_image)
            txt = input("Entrez le texte que vous voulez cacher")
            cachimg = texteinpicture(txt,Mat)
            print(cachimg.camouflage())
        else:
            raise ValueError("Vous n'avez pas tapé les bons caractères")
    else :
        raise ValueError("Vous n'avez pas tapé les bons caractères")


