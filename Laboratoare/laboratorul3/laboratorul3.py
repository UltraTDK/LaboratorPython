import re


# Exercitiul 1
#   Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def exercitiul1(a, b):
    # set() - este utilizat pentru a stoca colecții de date
    # intr-o singura variabila
    a_intersectat_b = set(a) & set(b)
    a_reunit_b = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)
    return [a_intersectat_b, a_reunit_b, a_minus_b, b_minus_a]


print("1.", exercitiul1([1, 2, 3, 5], [4, 5, 2, 1]))


# Exercitiul 2
#   Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character
# string and the values are the number of occurrences of that character in the given text
#   Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'a': 3, 's': 2, '.': 1, 'e': 1,
# 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
def functie2(text):
    dictionar = {}
    for litera in text:
        contor = text.count(litera)
        # formatul: dictionary[key] = value
        # setez/caut cheia unui dictionar
        dictionar[litera] = contor
    return dictionar


print("2.", functie2("Ana has apples."))


# Exercitiul 4
# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a
# string that represents the corresponding XML element.


#  Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link
# ", id= " someid ") returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def functie4(tag, content, **key_val):
    format_procesat = ""
    for key in key_val:
        # f-string: se evalueaza parametrii pusi intre {}
        # este alternativa functiei format()
        format_procesat += f'{key}="{key_val[key]}"'
    format_final = (
        "<" + tag + " " + format_procesat + "> " + content + " </" + tag + ">"
    )
    return format_final


print(
    "4.",
    functie4(
        "a",
        "Hello there",
        href=" http://python.org ",
        _class=" my-link ",
        id=" someid ",
    ),
)


# Exercitiul 5
#   The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that
#  has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is
# considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
#   The function will return True if the given dictionary matches all the rules, False otherwise.
def validate_dict(tuple, dictionar):
    format = {}
    for cheie in dictionar:
        for tuplu in tuple:
            if cheie == tuplu[0]:
                # f-string: este o reprezentare a unui text care nu se afla in textul original
                # \w - caractere alfanumerice + caracterul underscore '_'
                # * - cel putin 0 repetetii, cauta subsirul cel mai lung
                # \\ - ca sa pot folosi \w trebuie sa dau escape la backslash, astfel previn comportamentul
                # normal al unui grup de caractere
                # match - cauta caracterele care dau match cu pattern-ul
                if re.match(f"tuplu[1]\\w*tuplu[2]\\w*tuplu[3]", dictionar[cheie]):
                    return True
                else:
                    return False
    return False


print(
    "5.",
    validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        {"key1": "come inside, it's too cold out", "key3": "this is not valid"},
    ),
)


# Exercitiul 6
#   Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in
# the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).
def functie6(lista):
    lista_unic = []
    lista_duplicat = []
    for elem in lista:
        if elem not in lista_unic:
            lista_unic.append(elem)
        elif elem not in lista_duplicat and elem in lista_unic:
            lista_duplicat.append(elem)
    multime = (len(lista_unic), len(lista_duplicat))
    return multime


print("6.", functie6([1, 2, 3, 3, 4, 5, 1]))


# Exercitiul 7
#   Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two
# by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the
# applied operator: |, &, -.
def operatii(multime1, multime2):
    dictionar = {
        # am folosit str, deoarece cheie unui dictionar trebuie sa fie imutable
        # concret: cheia nu poate fi modificata (cel putin asa am inteles din curs)
        str(multime1) + "&" + str(multime2): multime1 & multime2,
        str(multime1) + "|" + str(multime2): multime1 | multime2,
        str(multime1) + "-" + str(multime2): multime1 - multime2,
        str(multime2) + "-" + str(multime1): multime2 - multime1,
    }
    return dictionar


def functie7(*multimi):
    dictionar = {}
    # asemanator ca la Bubble Sort, am procedat astfel pentru a nu verifica o pereche de doua ori
    # (a,b) si (b,a)
    for i in range(0, len(multimi) - 1):
        for j in range(i + 1, len(multimi)):
            rezultat = operatii(multimi[i], multimi[j])
            # concatenare intre dictionarul cu operatii si dictionarul final
            for elem in rezultat:
                dictionar[elem] = rezultat[elem]
    return dictionar


print("7.", functie7({1, 2}, {2, 3}))


# Exercitiul 8
#   Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting
# with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current
# key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects
# obtained as previously described.
def functie8(mapping):
    lista = []
    lista_finala = []
    elem = "start"
    while elem not in lista:
        lista.append(elem)
        elem = mapping[elem]
    # am creat acest for pentru a evita stringul "start" aflat la inceputul listei
    for i in range(1, len(lista)):
        lista_finala.append(lista[i])
    return lista_finala


print(
    "8.",
    functie8(
        {
            "start": "a",
            "b": "a",
            "a": "6",
            "6": "z",
            "x": "2",
            "z": "2",
            "2": "2",
            "y": "start",
        }
    ),
)


# Exercitiul 9
#  Write a function that receives a variable number of positional arguments and a variable number of keyword arguments and will
# return the number of positional arguments whose values can be found among keyword arguments values.
def functie9(*arguments, **kwarguments):
    counter = 0
    for argument in arguments:
        if argument in kwarguments.values():
            counter += 1
    return counter


print("9.", functie9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
