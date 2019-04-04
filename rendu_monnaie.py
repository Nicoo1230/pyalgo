"""
@name rendu_monnaie.py
@autor Aélion
@version 0.0.1
A poor coins counter
Use // to get an integer division
Use % to get rest of int div
Use input() function to get a user entry
"""
prixObjet = 75
sommeInitiale = 751
sommeApresAchat = sommeInitiale - prixObjet
nbreBillet100 = sommeApresAchat//100
reste100 = sommeApresAchat % 100
nbreBillet50 = reste100 // 50
reste50 = reste100 % 50
nbreBillet20 = reste50//20
reste20 = reste50%20
nbreBillet10 = reste20//10
reste10 = reste20%10
nbrePiece2 = reste10//2
reste2 = reste10%2

print("Vous avez payé avec", sommeInitiale, "€ pour un achat de ", prixObjet,"€ et nous vous rendons ", sommeApresAchat, "€ sous la forme de : ")
if nbreBillet100 >0:
    print(nbreBillet100, "billets de 100€, ")
if nbreBillet50 >0:
    print(nbreBillet50, "billets de 50€, ")
if nbreBillet20 >0:
    print(nbreBillet20, "billets de 20€, ")
if nbreBillet10 >0:
    print(nbreBillet10, "billets de 10€ ")
if nbrePiece2 >0:
    print(nbrePiece2, " pièces de 2€.")
#print("La machine vous rend actuellement :", nbreBillet100, "billets de 100€, ", nbreBillet50, "billets de 50€, ", nbreBillet20, "billets de 20€, ", nbreBillet10, "billets de 10€ et ", nbrePiece2, "pièces de 2€.")

