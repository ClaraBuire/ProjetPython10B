def dictionaire(Lalphabet,Lpoids):
    #on crée un dictionnaire qui lie n'importe quelle alphabet à une liste de poids
    #pour césar, on utilise des poids de 0 pour "a" à 24 pour "z" ...
    dic = {}
    for (i,lettre) in enumerate(Lalphabet):
        dic[lettre]= Lpoids[i]
    return dic 

def cryptagecesar(n,message,alphabet,cryptage=True):
    l = len(alphabet)
    dic = dictionaire(alphabet,[i for i in range(0,l)])
    dicinv = {i: j for j, i in dic.items()}
    mescrypte = ""
    if cryptage == True:
        m = 1
    else:
        m = -1
    for caractere in message.lower():
        #pour chaque caractere on teste si c'est une lettre pour ensuite calculer la valeur du nouveau poids avec le decalage et l'inscrire dans le messages crypté
        if caractere.isalpha():
            mescrypte += dicinv.get((m*n + dic[caractere])%l)
        else:
            mescrypte += caractere
    return mescrypte 

def vigenerecryptage(clé,message,alphabet,cryptage=True):
    #si cryptage = True on crypte un message, si False on décrypte le message
    l = len(alphabet)
    lclé = len(clé)
    dic = dictionaire(alphabet,[i for i in range(0,l)])
    dicinv = {i: j for j, i in dic.items()}
    mescrypte = ""
    iclé = 0
    if cryptage == True:
        m = 1
    else:
        m = -1
    for caractere in message.lower():
        if caractere.isalpha():
            decalage = dic[clé[iclé%lclé]]
            mescrypte += dicinv.get((m*decalage + dic[caractere])%l)
        else:
            mescrypte += caractere
        iclé += 1
    return mescrypte

def analysefrequentielle(mescrypte,alphabet):
    l = len(alphabet)
    dic = dictionaire(alphabet,[i for i in range(0,l)])
    Lfrequence = [0]*l
    for caractere in mescrypte.lower():
        if caractere.isalpha():
            Lfrequence[dic[caractere]] += 1   #on compte les itérations de chaque caractere
    for elt in Lfrequence:
        elt = elt/l #on passe en frequence
    return Lfrequence
    

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
    


def main():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","é","è","ê","ù"]
    message = "Généralement, les dauphins chassent en groupes serrés. On parle de coopération. Ils peuvent vivre en moyenne une quarantaine d'années. Lorsqu'un dauphin marin repère un banc de poissons, il avertit le reste du groupe qui se rapproche alors jusqu'à encercler les proies tout en les contraignant à se rassembler vers la surface. Une fois les poissons pris au piège et affolés, les dauphins n'ont plus qu'à traverser le banc l'un après l'autre en ouvrant une large gueule. On sait aussi que certains dauphins poursuivent les bancs de sardines jusqu'à les faire échouer sur le sable pour les attraper ensuite en s'échouant eux-mêmes à demi. Dans quelques cas, les dauphins peuvent s'associer aux thons et même aux requins pour des séances de chasse commune. Le dauphin a une excellente vision et possède également un sonar."
    #Cesar
    n = 18
    mescrypte = cryptagecesar(n,message,alphabet,True)
    print(mescrypte)
    print(cryptagecesar(n,mescrypte,alphabet,False))
    print(craquagecesar(mescrypte,alphabet))




    #Vigenere
    '''
    clé = "abc"
    mescrypte2 = vigenerecryptage(clé,message,alphabet,True)
    print(mescrypte2)
    print(vigenerecryptage(clé,mescrypte2,alphabet,False))
    '''
main()