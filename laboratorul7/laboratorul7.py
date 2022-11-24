import os
# Regular expressions
import re

# Exercitiul 1
# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
def functie1(param):
    # expresia '\w+' este folosita pentru a extrage caractere alpha numerice
    # problema cu '\w+' este ca ia si caracterul '_'
    alpha_numeric = re.findall(r"\w+", param)
    return alpha_numeric
print("1.", functie1("Am +#$ reusit !!! sa %^&* rezolv exercitiul 1."))


# Exercitiul 2
# Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those long-length x substrings that match the regular expression.
def functie2(reg_str, text, x):
    out = []
    # caut toate aparitiile stringului regex in text 
    match_x = re.findall(reg_str, text)
    for elem in match_x:
        # verific daca lungimea elementului gasit are lungimea x
        if len(elem) == x:
            out.append(elem)
    return out
print("2.", functie2("regex", "Un exemplu cu regex string si verific aparitia lui regex", 5))


# Exercitiul 3
# Write a function that receives as a parameter a string of text characters and a list of regular expressions and returns a list of strings that match on at least one regular expression given as a parameter.
def functie3(text, reg_list):
    out = []
    for elem in reg_list:
        if re.findall(elem, text):
            out.append(re.findall(elem, text))
    return out
print("3.", functie3("Ana are mere", ["Mihai are CNP valid", "Ana" , "are", "mere"]))


# Exercitiul 4
# Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags whose attributes are class="url" si name="url-form" si data-id="item".
def validare_atribute(linie, dict_attr):
    for key_attr in dict_attr:
        # f'..' - format: key = "atribut" (e.g. class = "url")
        curr_tag = f'{key_attr}\\s*=\\s*"{dict_attr[key_attr]}"'
        if not re.search(curr_tag, linie):
            return False
    return True
def functie4(path_xml, dict_attr):
    out = []
    # salvez fisierul intr-o variabila
    with open(path_xml) as file:
        for linie_xml in file.readlines():
            if validare_atribute(linie_xml, dict_attr):
                out.append(linie_xml)
    return out            
print("4.", functie4("laboratorul7/Lab7.xml", {"class": "my-class", "name": "Despre-somn"}))


# Exercitiul 5
# Write another variant of the function from the previous exercise that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary.
def validare_atribute5(linie, dict_attr):
    state = 0
    for key_attr in dict_attr:
        curr_tag = f'{key_attr}\\s*=\\s*"{dict_attr[key_attr]}"'
        if re.search(curr_tag, linie):
            state = 1
            break
    if state == 0:
        return False
    if state == 1:
        return True
def functie5(path_xml, dict_attr):
    out = []
    with open(path_xml) as file:
        for linie_xml in file.readlines():
            if validare_atribute5(linie_xml, dict_attr):
                out.append(linie_xml)
    return out            
print("5.", functie5("laboratorul7/Lab7.xml", {"class": "my-class", "name": "Despre-somn"}))


# Exercitiul 6
# Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship means replacing characters from odd positions with *.
def cenzor(cuvant):
    cuvant_cenzurat = ""
    for i in range(0, len(cuvant)):
        if i % 2 == 0:
            cuvant_cenzurat += cuvant[i]
        else:
            cuvant_cenzurat += "*"
    return cuvant_cenzurat
# Scenarii in care este posibil sa nu functioneze cum trebuie:
# - daca am mai multe spatii, afisarea se va face cu un singur spatiu
# - daca un cuvant este precedat de un caracter, nu este modificat
def functie6(text):
    prop_finala = ""
    for cuvant in str.split(text, " "):
        # verific daca incepe si se termina cu vocala
        # \b inceput ... final \b
        if re.match(r"\b[aeiou]\w*[aeiou]\b", cuvant):
            prop_finala += cenzor(cuvant)
        else:
            prop_finala += cuvant
        prop_finala += " "
    return prop_finala
print("6.", functie6("Daca incepe cu vocala si se termina cu vocala, atunci se va cenzura."))


# Exercitiul 7
# Verify using a regular expression whether a string is a valid CNP.
# Linkuri utile:
# https://ro.wikipedia.org/wiki/Cod_numeric_personal_(Rom%C3%A2nia)
# https://regex101.com/
def functie7(param):
    # Format: 6+12+04+05+228203
    cnp = re.match(r"^[0-8]\d\d((0[1-9])|(1[0-2]))((0[1-9])|([12]\d)|(3[01]))\d{6}$", param)
    if cnp != None:
        print("CNP-ul este valid.")
    else:
        print("CNP-ul nu este valid.")
functie7 = functie7("6120405228203")


# Exercitiul 8
# Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"
def functie8(direc, param):
    out = []
    # parametrii de care are nevoie os.walk
    for folder_param, foldere, fisiere in os.walk(direc):
        for fisier in fisiere:
            if fisier == param and re.search(param, fisier):
                out.append(">>" + fisier)
            elif fisier == param:
                out.append(fisier)
            elif re.search(param, fisier):
                out.append(fisier)
    return out
print("8.", functie8("../Laborator", "laboratorul7.py"))
