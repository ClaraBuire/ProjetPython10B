
class Crypte:
    def __init__(self,mot='',decalage=0,code_cesar=''):
        self.mot=mot
        self.chiffres=None                                       #mot en chiffres
        self.decalage=decalage                                   #nb de cases à decaler
        self.code=None                                           #mot decalé (cesar) en chiffres
        self.code_cesar=code_cesar                               #code cesar du mot en lettres
        self.length=max(len(self.mot),len(self.code_cesar))      #longueur du mot
                                              
        
    def nombre(self):
        """transforme un mot en chiffres"""
        nb=[]
        if self.code_cesar=='':
            mot=self.mot
        else:
            mot=self.code_cesar
        alphabet='abcdefghijklmnopqrstuvwxyz'
        for j in range(self.length):
            for i in range(26):
                if mot[j]==alphabet[i]:
                    nb.append(i)
                    break
        if self.code_cesar=='':
            self.chiffres=nb
        else:
            self.code=nb

    def decale(self, sens=1):       #pour coder : sens 1, pour décoder : sens -1
        """decale de self.decalage cases le self.nombre"""
        self.nombre()
        if sens==1:
            nb=self.chiffres
        else:
            nb=self.code
        for k in range(self.length):
            nb[k]+=sens*self.decalage
            if nb[k]<0:
                nb[k]=26+nb[k]
            else:
                nb[k]%=26
        if sens==1:
            self.code=nb
        else:
            self.chiffres=nb

    def cesar(self):
        """code en cesar"""
        alphabet='abcdefghijklmnopqrstuvwxyz'
        self.decale()
        for k in range(self.length):
            self.code_cesar+=alphabet[self.code[k]]

    def decode(self):
        """decode un mot encrypté en cesar dans self.code_cesar"""
        alphabet='abcdefghijklmnopqrstuvwxyz'
        self.decale(-1)
        for k in range(self.length):
            self.mot+=alphabet[self.code[k]]



a=Crypte('lucie',3)
a.cesar()
print(a.code_cesar)

b=Crypte(code_cesar='oxflh',decalage=3)
b.decode()
print(b.mot)