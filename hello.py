"""
    Algorithm #0.0.1
    Declare var
    Store some arithmetics into var
    Display result
    Operands and Operators, functions

    @version 0.0.2
    Add two operands and replace compute method
"""

""""
Function setting
"""
def addition(operande1, operande2):
    return operande1 + operande2

resultat = 0 # Définition de la variable
operande1 = -3
operande2 = 2
resultat = addition(5, 3) #Call addition function with 5 and 3 as params
print(resultat)
print(addition(operande1, operande2))
if resultat > 0:
     print('le résultat est positif')
if resultat == 0:
    print("le résultat est nul")
else :
    print('le résultat est négatif')

"""
Fin de l'algorithme
"""