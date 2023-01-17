from PIL import Image
import cryptagetexte
import cle
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


def texttoimage(text,chemin_acces):
  """programme qui à partir d'un texte construit une image en utilisant le principe inverse et l'enregistre à chemin_acces"""
  print(text[0:4],text[4:8])
  img = Image.new("RGB",(int(text[0:4]),int(text[4:8])))
  pixel = img.load()
  indice = 8
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      #print(indice)
      pixel[i,j] = (ord(text[indice]),ord(text[indice + 1]),ord(text[indice + 2]))
      indice += 3
  img.save(chemin_acces)

text = imagetotexte("paysage.jpg")
print(text)
mes = cryptagetexte.Message(text[8:])
mes.cesar(cle.Clé(5))
texttoimage(text[:8]+mes.texte,"image.png")

"""
import cle
import cryptagetexte

mail2 = cryptagetexte.Message("coucou")
key2 = cle.Clé("5")
mail2.cesar(key2)
print(mail2)
mail2.modecryptage(False)
mail2.cesar(key2)
print(mail2)


mail = cryptagetexte.Message(imagetotexte("couleur.jpg"))
key = cle.Clé("5")
dimension = mail.texte[:8]
mail.texte = mail.texte[8:]
mail.cesar(key)
mail.texte = dimension + mail.texte
texttoimage(mail)
print("69")
mail.modecryptage(False)
mail.texte = mail.texte[8:]
mail.cesar(key)
mail.texte = dimension + mail.texte
texttoimage(mail,"sortie.jpg")


if __name__ == "__main__":
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
"""