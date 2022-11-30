#De base dans cryptage classe mais ça n'a rien à voir donc création de attaque.py
#mais tout est à faire
import cryptageclasse

def craquagecesar(mescrypte,alphabet):
    # E étant de loin la lettre la plus utilisée en français on cherche le decalage par rapport à E
    l = len(alphabet)
    Lf = analysefrequentielle(mescrypte,alphabet)
    imaxf = 0
    maxf = 0
    for (i,f) in enumerate(Lf):
        if f > maxf:
            imaxf = i 
            maxf = f
    return (imaxf-4)%l  #indice de la lettre la plus recurente - l'indice de e (modulu la longueur de la liste)
    

def analysefrequentielle(mescrypte,alphabet):
    l = len(alphabet)
    dic = cryptageclasse.dictionaire(alphabet,[i for i in range(0,l)])
    Lfrequence = [0]*l
    for caractere in mescrypte.lower():
        if caractere.isalpha():
            Lfrequence[dic[caractere]] += 1   #on compte les itérations de chaque caractere
    for elt in Lfrequence:
        elt = elt/l #on passe en frequence
    return Lfrequence