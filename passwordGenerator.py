import random

# Déclaration de la liste de lettre:
listLetter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Déclaration de la liste de chiffre:
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

# Déclaration de la liste de ponctuation:
ponctuation = [",", ";", "!", "/", "?", "[", "(",",","#","]",")"]

# Déclaration de la liste de majuscules:
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

passwordLength =  random.randint(8,12)
print(passwordLength)

nbAIEntier = random.randint(0,25)
lett = listLetter[nbAIEntier]
print(lett)

nbAIEntier = random.randint(0,8)
numb = number[nbAIEntier]
print(numb)

nbAIEntier = random.randint(0,10)
ponct = ponctuation[nbAIEntier]
print(ponct)

nbAIEntier = random.randint(0,25)
upper = uppercase[nbAIEntier]
print(upper)

password = [lett, ponct, upper]

while len (password) < passwordLength:
    stock = random.randint(0,3)
    if stock == 0:
        bigBox = listLetter
    if stock == 1:
        bigBox = number
    if stock == 2:
        bigBox = ponctuation
    if stock == 3:
        bigBox = uppercase
    nbAIEntier = random.randint(0,len(bigBox)-1)
    password.append(bigBox[nbAIEntier])
print(password)
random.shuffle(password)
print(password)

0