#### utiliser la methode du test de millier-rabin pour génerer une grande nombre premier
n=353
def cal_puissance(n):
    ### ce fonction calcul le nombre de fois que n peut diviser par 2
    s = -1
    while n//2 == n/2:
        n = n/2
        s += 1
    return s

cal_puissance(n)d
        

#### utiliser la methode du test de millier-rabin pour génerer une grande nombre premier
#### une seule test miller rabin donne la resultat avec une fiabilité grande mais pas cent pour cent
### Donc, il faut faire le test en variant les bases



def cal_puissance(n):
    ### ce fonction calcul le nombre de fois que n peut diviser par 2
    s = 0
    while n//2 == n/2:
        n = n/2
        s += 1
    return s



def miller_rabin_base(n,b): 
    #### miller_rabin_base prend en parametre un nombre n et une base b  et renvoie True si n est premier
    s = cal_puissance(n-1) ### étape: n-1 = 2^^s * d
    d=  (n-1)/ 2**s
    r = (b**d) % 353  ## initialise l'itération
    if r == 1 or r == -1 or r== n-1:
        return True
    for i in range(1,s):  ## itérations en 1 à s-1 inclus
        r= (r**2 )% 353
        print(r)
        if r == 1:
            return False
        elif r ==-1 or r== n-1:
            return True
    return False

def miller_rabin(n):
    ### test de milier_rabin avec plusieurs bases si n est un très grand nombre
    premier = True
    Lplafond = [1373653,25326001,25000000000,2152302898747,3474749660383,341550071728321]
    Lpremier = [2,3,5,7,11,13,17]
    i = 0
    while n > Lplafond[i]:
        i += 1
    base = 2
    s = 0
    while s < i and premier == True:
        premier = miller_rabin_base(n,Lpremier[s])
        s += 1
    return premier    
    
    
print(miller_rabin_base(654672,2))

        