import RSA
#Le chiffrement RSA est asymétrique : il utilise une paire de clés (des nombres entiers)
#  composée d'une clé publique pour chiffrer et d'une clé privée pour déchiffrer des données confidentielles.
#Une condition indispensable est qu'il soit « calculatoirement impossible » de déchiffrer à l'aide de la seule clé publique

key = RSA.generate(2048) # key contient la clé pivée
# key.publickey() donne la clé public
print(key)