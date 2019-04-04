"""
@name manip_tableau.py
@author Aélion
@version 1.0.0
    Algorithme spécifique sur collection
"""
"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal
"""
getGreaterOf function
returns the greater value of two params
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else:
        return secondVal

"""
compare function
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of the two depends on howTo params
"""
def compare(firstVal, secondVal, desc="True"):
    if (desc):
        return(getLowerOf(firstVal, secondVal))
    
    return(getGreaterOf(firstVal, secondVal))

"""
min function
@param anArray The array from which i want to get the min value
@return the min value of anArray
"""
def min(anArray):
    theMin = anArray[0]
    for value in anArray[1:]:
        theMin = compare(theMin, value)
    
    return theMin

"""
max function
@param anArray The array from whiwh i want to get the max value
@return the max value of anArray
"""
def max(anArray):
    theMax = anArray[0]
    for value in anArray[1:]:
        theMax = compare(theMax, value, False)
    
    return theMax

"""

"""
def average(anArray):
    total = 0
    nbItems = 0
    for val in anArray:
        total = total + val
        nbItems = nbItems + 1
    return total / nbItems

def factorial(anArray):
    facto = 1
    for val in anArray:
        facto = facto * val
    return facto


# Déclaration du tableau de démonstration
monTablo = [15, 3, 25, 12, 7, -15]

#
#simple poor loop
#
for indice, val in enumerate(monTablo):
    print(monTablo[indice]*2)

# More complex loop with condition
for indice, val in enumerate(monTablo):
    if indice%2 == 0:
        print(monTablo[indice] * 2)

print (list(monTablo))

# Bit more complex loop : find a min
print("And the min is : ",min(monTablo))
print("And the max is :",max(monTablo))
print("Valeur moyenne :", average(monTablo))
print("Factorielle :", factorial(monTablo))