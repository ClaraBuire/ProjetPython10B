from PIL import Image
import convertisseur
import numpy as np

###Class du programme
class texteinpicture():
    def __init__(self,phrase,M):
        self.M = M
        self.phrase = phrase

    def camouflage(self,chemin_acces='Users\remim\Downloads\test3.png'):
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
                    C[i,j,1] = convertisseur.transfo(self.matriceimg[i,j,1], bit)
                else:
                    C[i,j,1] = convertisseur.transfo(self.matriceimg[i,j,1],1)
        image_C = Image.fromarray(C)
        #image_C.show()
        image_C.save(chemin_acces,'png')
        return chemin_acces

def imagetotexte(image):
  """programme qui transforme une image en texte (pour etre ensuite crypté)"""
  img = Image.open(image)
  pixel = img.load()
  text = f"{img.size[0]}".rjust(4, '0') + f"{img.size[1]}".rjust(4, '0') #les 8 premiers caracteres code la resolution de l'image 
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      #pour chaque pixel je recupere la valeur r, b ,b et on les traduits en caractere ascii
      r, g, b = pixel[i, j]
      text = text + chr(r) + chr(g) + chr(b)
  return text


def texttoimage(text,chemin_acces="image.png"):
  """programme qui à partir d'un texte construit une image en utilisant le principe inverse et l'enregistre à chemin_acces"""
  print(text[0:4],text[4:8])
  img = Image.new("RGB",(int(text[0:4]),int(text[4:8])))
  pixel = img.load()
  indice = 8
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      pixel[i,j] = (ord(text[indice]),ord(text[indice + 1]),ord(text[indice + 2]))
      indice += 3 
  img.save(chemin_acces)
  return chemin_acces
