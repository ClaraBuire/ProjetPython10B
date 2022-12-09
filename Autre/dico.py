class Dictionnaire:
    #classe qui permet de crée 2 dictionnaire, un premier donnant le poids pour chaque caractere (lettre) et un deuxième qui est l'inverse
    def __init__(self):
        #diclettre : {caractere : poids}
        #dicpoids : {poids : caractere}
        self.diclettre = {}
        self.dicpoids = {}
        self.longueur = 0

    def dic(self, Lalphabet, Lpoids):
        #creation des dictionnaires
        for (i,lettre) in enumerate(Lalphabet):
            self.diclettre[lettre]= Lpoids[i]
        self.dicpoids = {i: j for j, i in self.diclettre.items()}
        self.longueur = len(Lalphabet)

    def __repr__(self):
        return "dico lettre : " + self.diclettre + "et dico poids : " + self.dicpoids

def info_dico():
    #cette fonction crée directement tt les 
    Lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","é","è","ê","ù"," ","@",".",",",";","?","!","+","-","/","*","0","1","2","3","4","5","6","7","8","9","10"]
    n=len(Lalphabet)
    Lpoids = [i for i in range(n)]   
    dicoalphapoids = Dictionnaire()
    dicoalphapoids.dic(Lalphabet,Lpoids)
    return dicoalphapoids
