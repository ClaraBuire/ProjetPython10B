from PIL import Image

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
      #print(indice)
      pixel[i,j] = (ord(text[indice]),ord(text[indice + 1]),ord(text[indice + 2]))
      indice += 3
  img.save(chemin_acces)

if __name__ == "main":
  text = imagetotexte("paysage.jpg")
  print(text)
  texttoimage(text)
