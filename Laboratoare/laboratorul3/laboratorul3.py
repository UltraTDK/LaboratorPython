# Write a function to return a list of the first n numbers in the Fibonacci string

def fibonnaci(n):
    nr1 = 0
    nr2 = 1
    lista_fib = [0, 1]
    for i in range(2, n) :
        element_lista = nr1 + nr2
        nr1 = nr2
        nr2 = element_lista
        lista_fib.append(element_lista)

    return lista_fib


# Write a function that receives a list of numbers and returns a list of the prime numbers found in it

def estePrim(lista_mea):
    lista_elem_prime = []
    for i in lista_mea :
        counter = 0
        for j in range (1, i) :
            if i % j == 0:
                counter+=1
        if counter == 1 :
            lista_elem_prime.append(i)

    return lista_elem_prime


# Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def exercitiul3(lista1, lista2):
    lista_intersectie = []
    lista_reuniune = []
    lista_a_minus_b = []
    lista_b_minus_a = []
    for a in lista1:
        if a in lista2 and a not in lista_intersectie:
            lista_intersectie.append(a)
    for a in lista1:
        if a not in lista_reuniune:
            lista_reuniune.append(a)
    for b in lista2:
        if b not in lista_reuniune:
            lista_reuniune.append(b)
    for a in lista1:
        if a not in lista2:
            lista_a_minus_b.append(a)
    for b in lista2:
        if b not in lista1:
            lista_b_minus_a.append(b)

    print("Intersectie:", lista_intersectie)
    print("Reuniune:", lista_reuniune)
    print("a - b:", lista_a_minus_b)
    print("b - a:", lista_b_minus_a)


# Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer). The function will return
# the song composed by going through the musical notes beginning with the start
# position and following the moves given as parameter
# Example: compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return
# ["mi", "fa", "do", "sol", "re"]

def noteMuzicale(note_muzicale, lista_mutari, pozitie_de_start):
    lista_finala = [note_muzicale[pozitie_de_start]]

    for mutare in lista_mutari:
        if mutare < 0:
            pozitie_de_start -= (mutare + 1)
            pozitie_de_start = pozitie_de_start % len(note_muzicale)
        else:
            pozitie_de_start = pozitie_de_start + mutare
            pozitie_de_start = pozitie_de_start % len(note_muzicale)
        lista_finala.append(note_muzicale[pozitie_de_start])
    return lista_finala


# Write a function that receives as parameter a matrix and will return the matrix obtained
# by replacing all the elements under the main diagonal with 0 (zero)

def exercitiul5(matrice):
    for i in range (len(matrice)):
        for j in range(i):
            matrice[i][j] = 0

    return matrice


# Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists

def exercitiul6(*liste, count):
    toate_listele = []
    lista_finala = []

    for lista in liste:
        toate_listele = toate_listele + lista
    for item in toate_listele:
        if toate_listele.count(item) == count and item not in lista_finala:
            lista_finala.append(item)

    return lista_finala