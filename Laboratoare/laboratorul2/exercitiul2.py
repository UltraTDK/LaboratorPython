# Write a script that calculates how many vowels are in a string

def counterVocale(str):
    counter = 0
    vocale = set("aeiouAEIOU")
    for litera in str:
        if litera in vocale:
            counter = counter + 1

    print("Numarul de vocale: ", counter)


print("Introdu un cuvant: ")
cuvant = str(input())

counterVocale(cuvant)
