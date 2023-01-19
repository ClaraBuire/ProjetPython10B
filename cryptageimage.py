from PIL import Image
import convertisseur
import numpy as np

VAI = 31 #valeur indésirable de 0 à 31 en ascii
MAXVPIXEL = 256 #la valeur maxi d'un pixel

class texteinpicture():
    def __init__(self,phrase,M):
        self.M = M
        self.phrase = phrase

    def camouflage(self,chemin_acces='Users\remim\Downloads\test3.png'):
        """cache un texte dans une image"""
        H,L = self.M.shape[0],self.M.shape[1]
        C = np.copy(self.M)
        code = convertisseur.codage_binaire(self.phrase)
        N = len(code)
        i,k = 0,0
        while i<=H-1 and k<=N-1:
            j = 0
            while j<= L-1 and k<= N-1:
                C[i,j,0] = convertisseur.transfo(self.M[i,j,0], int(code[k]))
                j += 1
                k += 1
            i += 1
        image_C = Image.fromarray(C)
        image_C.save(chemin_acces,'png')
        return chemin_acces



    def extraction(self):
        """extrait un texte dans une image"""
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
        Noctets = convertisseur.nombre(binaire)*8
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
        return convertisseur.convertir_en_chaine(binaire+phrase_binaire)

class pictureinpicture():
    def __init__(self,matriceimg,imageacacher):
        self.matriceimg = matriceimg
        self.imageacacher = imageacacher
    #Camouflage/Extraction d'une image dans une autre image
    #Extraction d'une image en noir et blanc d'une image support

    def extraction_image(self,chemin_acces='Users\remim\Downloads\test3.png'):
        """extrait une image camouflée dans une autre"""
        H,L = self.matriceimg.shape[0],self.matriceimg.shape[1]
        C = np.zeros((H,L))
        for i in range(H):
            for j in range(L):
                if self.matriceimg[i,j,1] %2 == 0:
                    C[i,j] = 0
                else:
                    C[i,j] = 255
        image_C = Image.fromarray(C)
        image_C=image_C.convert('L')
        #image_C.show()
        image_C.save(chemin_acces,'png')
        return chemin_acces
    
    #camoufle la matrice I d'une image en noir et blanc
    
    def camouflage_image(self, chemin_acces='Users\remim\Downloads\test3.png'):
        """camoufle une image NOIR et BLANC, format png dans une image png"""
        HM,LM = self.matriceimg.shape[0], self.matriceimg.shape[1]
        HI, LI = self.imageacacher.shape[0], self.imageacacher.shape[1]
        C = np.copy(self.matriceimg)
        for i in range(HM):
            for j in range(LM):
                if i in range(HI) and j in range(LI):
                    bit = self.imageacacher[i,j]//255
                    C[i,j,1] = convertisseur.transfo(self.matriceimg[i,j,1], bit)
                else:
                    C[i,j,1] = convertisseur.transfo(self.matriceimg[i,j,1],1)
        image_C = Image.fromarray(C)
        image_C.save(chemin_acces,'png')
        return chemin_acces


class imagecryptage():
    def __init__(self,chemin):
        self.dimension = (0,0)
        self.pixel = []
        self.cryptage = 1
        self.chemin = chemin

    def cesarimage(self,cle):
        Lpixel = []
        for (i,pixel) in enumerate(self.pixel):
            [r,g,b] = pixel
            r = (r + (int(cle.texte)+i)*(self.cryptage))%MAXVPIXEL
            g = (g + (int(cle.texte)+i)*(self.cryptage))%MAXVPIXEL
            b = (b + (int(cle.texte)+i)*(self.cryptage))%MAXVPIXEL
            Lpixel += [[r,g,b]]
        self.pixel = Lpixel

    def vigenereimage(self,cle):
            Lpixel = []
            iclé = 0
            lclé = cle.longueur
            for (i,pixel) in enumerate(self.pixel):
                decalage = ord(cle.texte[iclé%lclé])
                d = decalage//3
                pixel[d%3] = (pixel[d%3] + (decalage+i)*(self.cryptage))%MAXVPIXEL
                pixel[(d+1)%3] = (pixel[(d+1)%3] + (decalage+i)*(self.cryptage))%MAXVPIXEL
                pixel[(d+2)%3] = (pixel[(d+2)%3] + (decalage+i)*(self.cryptage))%MAXVPIXEL
                Lpixel += [pixel]
                iclé += 1
            self.pixel = Lpixel

    

    def listepixel(self):
        """transforme une image en liste de pixel (pour etre ensuite crypté)"""
        img = Image.open(self.chemin)
        self.dimension = (img.size[0],img.size[1])
        pixel = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
            #pour chaque pixel je recupere la valeur r, g,b et on les traduits en caractere ascii
                r, g, b = pixel[i, j]
                self.pixel += [[r,g,b]]


    def reconstruction(self,chemin_acces="image.png"):
        """construit une image à partir d'une liste de pixel en utilisant le principe inverse et l'enregistre à chemin_acces"""
        img = Image.new("RGB",(self.dimension[0],self.dimension[1]))
        pixel = img.load()
        indice = 0
        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                (r,g,b) = self.pixel[indice]
                pixel[i,j] = r, g, b 
                indice += 1
        img.save(chemin_acces)
        return chemin_acces