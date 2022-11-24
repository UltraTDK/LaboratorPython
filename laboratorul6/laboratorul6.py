# Exercitiul 2
#  Create a function and an anonymous function that receive a 
# variable number of arguments. Both will return the sum of 
# the values of the keyword arguments
def functie2(*args, **kwargs):
    sum = 0
    for kw_argument in kwargs.keys():
        sum += int(kwargs[kw_argument])
    return sum


# Functii anonime = lambda expressions
# exemplu 
# suma = lambda a, b: a + b
# print(suma(2, 3))
anonymous_function = lambda *args, **kwargs: sum([kw_args for kw_args in kwargs.values()])
print("2. Functie anonima:", anonymous_function(1, 2, c=3, d=4))
print("2. Functie normala:", functie2(1, 2, c=3, d=4))


# Exercitiul 3
# Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with all the vowels in a given string.
# For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].
def functie3(sir):
    out = []
    for litera in sir:
        if litera.lower() in "aeiou":
            out.append(litera.lower()) 
    return out
anon_func_string = lambda sir: [litera for litera in sir if litera.lower() in "aeiou"]
def filtru(ch):
    if ch.lower() in "aeiou":
        return True
    return False
filtered_list = list(filter(filtru, "Programming in python is fun"))
print("3. Functie:", functie3("Programming in Python is fun"))
print("3. Functie anonima:", anon_func_string("Programming in Python is fun"))
print("3. Filtered list:", filtered_list)


# Exercitiul4
# Write a function that receives a variable number of arguments and keyword arguments. The function returns a list containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with minimum 3 characters.
def parcurge_argumente(args):
    out = []
    for argument in args:
        if type(argument) == dict and len(argument.keys()) >= 2:
            for key in argument.keys():
                if type(key) == str and len(key) >= 3:
                    out.append(argument)
                    break
    return out
def functie4(*args, **kwargs):
    return parcurge_argumente(args) + parcurge_argumente(kwargs.values())
# Pana la "dictionar=.." am arguments, dupa keyword_arguments. Format "key=...". Dupa ce am kw_args, pot sa pun doar kw_args
print("4:", functie4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))


# Exercitiul 5
#  Write a function with one parameter which represents a list. 
#  The function will return a new list containing all the numbers
# found in the given list
def number_list(list):
    # Python are trei tipuri de date numerice : int, float si complex
    lista_numere = []
    lista = (int, float, complex)
    for elem in list:
        if isinstance(elem, lista):
            lista_numere.append(elem)
    return lista_numere
print("5.", number_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


# Exercitiul 6
# Write a function that receives a list with integers as parameter that contains an equal number of even and odd numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
def functie6(lista):
    lista_pare = []
    lista_impare = []  
    lista_finala = []
    for elem in lista:
        if(elem % 2 == 0):
            lista_pare.append(elem)
        elif (elem % 2 == 1):
            lista_impare.append(elem)
    # zip creeaza tuple cu cele doua liste pe care i le-am dat ca parametru
    tuplu_zip = list(zip(lista_pare, lista_impare))

    for i in range(0, len(lista_pare)):
        tuplu = lista_pare[i], lista_impare[i]
        lista_finala.append(tuplu)
    print("6. zip: ", tuplu_zip)
    print("6. Fara zip:", lista_finala)
functie6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])


# Exercitiul 7
def Fib1000():
    # Fib: adun ultimele doua valori care o preceda pe urmatoarea pana ajung la 1000 de numere
    nr1 = 0
    nr2 = 1
    lista_fib = [0, 1]
    for i in range(2, 1000) :
        element_lista = nr1 + nr2
        nr1 = nr2
        nr2 = element_lista
        lista_fib.append(element_lista)
    return lista_fib
# Daca filter_func are macar un False atunci functia trebuie sa returneze False
def filtru(filtre, x):
    for filter_func in filtre:
        if filter_func(x) == False:
            return False
    return True
def process(**kwargs):
    filters = []
    limit = 1000
    offset = 0
    out = []
    lista_finala = []
    lista_fib = Fib1000()
    for kw_arg in kwargs.keys():
        if kw_arg == "filters":
            filters = kwargs["filters"]
        elif kw_arg == "limit":
            limit = kwargs["limit"]
        elif kw_arg == "offset":
            offset = kwargs["offset"]
    for elem in lista_fib:
        if filtru(filters, elem) == True:
            out.append(elem)
    for elem in range(offset, offset + limit):
        lista_finala.append(out[elem])
    return lista_finala
def sum_digits(x):
    return sum(map(int, str(x)))
def functie7():
    return process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2)
print("7.", functie7())

# Exercitiul 8
# Write a function called print_arguments with one parameter named function. The function will return one new function which prints the arguments and the keyword arguments received and will return the output of the function receives as a parameter.
def print_arguments(function):
    def afisare_param(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)
    return afisare_param
# Decoratorul este de regula o functie care primeste ca parametru o alta functie
# Am folosit decorator pentru usurinta rezolvarii problemei
@print_arguments
def multiply_by_two(x):
    return x * 2
@print_arguments
def add_numbers(a, b):
    return a + b
print("8. a)", multiply_by_two(2))
print("8. a)", add_numbers(3, 4))


def multiply_output(function):
    def afisare_param(*args, **kwargs):
        return 2 * function(*args, **kwargs)
    return afisare_param
@multiply_output
def multiply_by_three(x):
    return x * 3
print("8. b)", multiply_by_three(10))

# Exercitiul 9
# Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs). The function should return a list of dictionaries for each pair (in the same order as in the input list) that contain the following keys (as strings): sum (the value should be sum of the 2 numbers), prod (the value should be product of the two numbers), pow (the value should be the first number raised to the power of the second number)
def functie9(pairs):
    out = []
    for tuplu in pairs:
        pereche = {
            "sum": tuplu[0] + tuplu[1],
            "prod": tuplu[0] * tuplu[1],
            "pow": tuplu[0] ** tuplu[1]
            # alta metoda de ridicare la putere:
            # pow(tuplu[0], tuplu[1])
        }
        out.append(pereche)
    return out

print("9.", functie9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))
