# Exercitiul 2
#  Create a function and an anonymous function that receive a 
# variable number of arguments. Both will return the sum of 
# the values of the keyword arguments

def anonymous_function(*args, **kwargs):
    sum = 0
    for kw_argument in kwargs.keys():
        sum += int(kwargs[kw_argument])
    return sum

print(anonymous_function(1, 2, c=3, d=4))

# Exercitiul 5
#  Write a function with one parameter which represents a list. 
#  The function will return a new list containing all the numbers
# found in the given list

def number_list(list):
    lista_numere = []
    for elem in list:
        if type(elem) in [int, float]:
            lista_numere.append(elem)
    return lista_numere

print(number_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))