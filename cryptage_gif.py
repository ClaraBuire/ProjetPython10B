from PIL import Image
import convertisseur as ascii
import numpy as np
import imageio.v2 as iio
import matplotlib.pyplot as plt


###Class du programme
class texteinpicture():
    def __init__(self,phrase,M):
        self.M = M
        self.phrase = phrase

    def camouflage(self, chemin_enregistrement='/Users/xuzenli/Desktop/images/GIF_modifie/message_pour_clara.jpg'):
        """camoufle le texte dans une image. Penser à modifier le chemin d'enregristrement"""
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
        image_C.save(chemin_enregistrement,'png')



    def extraction(self):
        """extrait le texte caché dans une image"""
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





def cree_gif(nom='coeur.gif'):
    """cree un GIF coeur - ATTENTION  lire les avertissement du readme.txt avant de lancer cette fonction"""
    # Implémentation de l'équation paramétrique
    t = np.linspace(0,2*np.pi, 50) # Je choisis 50 points entre 0 et 2pi
    x = 16*(np.sin(t))**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

    # Enregistrement des images
    for i in range(len(t)):
       plt.scatter(x[i], y[i]) # Tracé
       plt.savefig(f"GIF/{i}.jpg") # Enregistrement dans le dossier "GIF"

    frames = np.stack([iio.imread(f"GIF/{i}.jpg") for i in range(len(t))], axis = 0)
    iio.mimwrite(nom, frames) # creer un gif avec le nom coeur.gif
    




def main_emetteur(nom_enregistrement='coeur_modifie.gif'):
    """ entrée : dossier gif(50 images) et un texte, sortie : un texte caché dans le gif  modifié"""
    
    ### cacher le texte dans l'image
    matrice = input("Entrez le chemin de votre première image du gif : ")
    mon_image = Image.open(matrice)
    Mat = np.array(mon_image)
    txt = input("Entrez le texte que vous voulez cacher : ")
    cachimg = texteinpicture(txt,Mat)
    print(cachimg.camouflage())
    import imageio.v2 as iio
    frames = np.stack([iio.imread(f"GIF_modifie/{i}.jpg") for i in range(len(t))], axis = 0)
    iio.mimwrite(nom_enregistrement, frames)

       

def main_recepeteur():
       
    ### réveler le texte
    matrice = input("Entrez le chemin de votre dossier GIF_modifie : ")+'/message_pour_clara.jpg'
    mon_image = Image.open(matrice)
    Mat = np.array(mon_image)
    revelimg = texteinpicture('',Mat)
    print(revelimg.extraction())
    
    


