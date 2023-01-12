from PIL import Image
import ascii
import numpy as np

###Class du programme
class texteinpicture():
    def __init__(self,phrase,M):
        self.M = M
        self.phrase = phrase

    def camouflage(self,chemin_acces='Users\remim\Downloads\test3.png'):
        H,L = self.M.shape[0],self.M.shape[1]
        C = np.copy(self.M)
        code = ascii.codage_binaire(self.phrase)
        N = len(code)
        i,k = 0,0
        while i<=H-1 and k<=N-1:
            j = 0
            while j<= L-1 and k<= N-1:
                C[i,j,0] = ascii.transfo(self.M[i,j,0], int(code[k]))
                j += 1
                k += 1
            i += 1
        image_C = Image.fromarray(C)
        image_C.save(chemin_acces,'png')
        return chemin_acces



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
        Noctets = ascii.nombre(binaire)*8
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
        return ascii.convertir_en_chaine(binaire+phrase_binaire)

class pictureinpicture():
    def __init__(self,matriceimg,imageacacher):
        self.matriceimg = matriceimg
        self.imageacacher = imageacacher
    #Camouflage/Extraction d'une image dans une autre image
    #Extraction d'une image en noir et blanc d'une image support
    def extraction_image(self,chemin_acces='Users\remim\Downloads\test3.png'):
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
        HM,LM = self.matriceimg.shape[0], self.matriceimg.shape[1]
        HI, LI = self.imageacacher.shape[0], self.imageacacher.shape[1]
        C = np.copy(self.matriceimg)
        for i in range(HM):
            for j in range(LM):
                if i in range(HI) and j in range(LI):
                    bit = self.imageacacher[i,j]//255
                    C[i,j,1] = ascii.transfo(self.matriceimg[i,j,1], bit)
                else:
                    C[i,j,1] = ascii.transfo(self.matriceimg[i,j,1],1)
        image_C = Image.fromarray(C)
        #image_C.show()
        image_C.save(chemin_acces,'png')
        return chemin_acces

if __name__ == "__main__":
    class main(texteinpicture, pictureinpicture):
        message = input("Veuillez choisir si vous voulez coder/décoder un texte dans une image(taper t) ou une image(taper i) ")
        if message == 'i':
            message2 = input("Veuillez choisir si vous voulez cacher une image dans l'image support(taper c) ou bien reveler une image cacher(taper r)")
            if message2 == 'c': #cryptage
                matrice = input("Entrez le chemin de votre image en noir et blanc à cacher")
                mon_image = Image.open(matrice)
                Mat = np.array(mon_image)
                matrice2 = input("Entrez le chemin de votre image support")
                mon_image2 = Image.open(matrice2)
                Mat2 = np.array(mon_image2)
                camoufimg = pictureinpicture(Mat2,Mat)
                #camoufimg.save('Desktop\image_m.png','png')
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


