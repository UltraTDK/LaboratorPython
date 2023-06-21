# Exercitiul 1
# a) Write a module named utils.py that contains one function called
# process_item. The function will have one parameter, x, and will
# return the least prime number greater than x. When run, the module
#  will request an input from the user, convert it to a number and
# it will display the output of the process_item function


def is_prime(prim):
    for i in range(2, prim):
        if (prim % i) == 0:
            return False
    return True


def process_item(x):
    # ma asigur ca il incrementez pe x pt a gasi un numar prim mai
    # mare decat el
    next_prime = x + 1
    oprit = True
    while oprit:
        next_prime += 1
        if is_prime(next_prime):
            oprit = False
            return next_prime
