import random

"""
@name mot_de_passe.py
@autor Aélion
version 0.0.1
    Générateur de mot de passe
"""
# Déclaration de la liste de lettre:
listLetter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Déclaration de la liste de chiffre:
listNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

# Déclaration de la liste de ponctuation:
listPonctuation = [",", ";", "!", "/", "?", "[", "(",",","#","]",")"]

# Déclaration de la liste de majuscules:
listUppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Détermination de la longueur du MDP:
passwordLength = random.randint(8,12)
print(passwordLength)

# Détermination de la composition du MDP en éléments:
#while(nbLetter + nbNumber + nbPonctuation + nbUppercase) < passwordLength or (nbLetter + nbNumber + nbPonctuation + nbUppercase) > passwordLength:

nbLetter = random.randint(0,25)
lett = listLetter[nbLetter]
print(lett)
nbNumber = random.randint(0,8)
numb = listNumber[nbNumber]
print(numb)
nbPonctuation = random.randint(0,10)
ponc = listPonctuation[nbPonctuation]
print(ponc)
nbUppercase = random.randint(0,25)
upp = listUppercase[nbUppercase]
print(upp)

password = [lett, ponc, upp]
print("MDP = ", password)

while len(password) < passwordLength:
    choice = random.randint(0,3)
    if choice == 0:
        box = listLetter
    if choice == 1:
        box = listNumber
    if choice == 2:
        box = listPonctuation
    if choice == 3:
        box = listUppercase
    progAjout = random.randint(0,len(box)-1)
    password.append(box[progAjout])
print(password)
# Ajouter box dans password:






"""
    nbLetter = random.randint(0,passwordLength)
    nbNumber = random.randint(0,passwordLength)
    nbPonctuation = random.randint(0,passwordLength)
    nbUppercase = random.randint(0,passwordLength)
print(nbUppercase)
print(nbLetter)
print(nbNumber)
print(nbPonctuation)

# Convertir les quantités en données:
selectLetter = []
progChoix = random.randint(0,25)
choose = listLetter[progChoix]
compteur = len(selectLetter)
while compteur < nbLetter:
    selectLetter =  [selectLetter] + choose
print(selectLetter)

"""
"""

fLetter = random.randint(0,25)
stockLetter = listLetter[fLetter]
if nbLetter > len(stockLetter):
    stockLetter = random.choice(listLetter)
print(stockLetter)

while len(stockLetter) < nbLetter:
    fLetter.append(stockLetter)
print(stockLetter)
"""
# Tri aléatoire des éléments du MDP:


# Création du MDP:

"""
Charly = str(Charly)
while len(Charly) < nbLetter:
    Charly = letter[random.randint(0,25)]
print("Charly",Charly)
"""