# Write a function that validates if a number is a palindrome

def palindrom(numar):
    # Salvez numar in temp, deoarece isi pierde valoarea in bucla while dupa un numar de iteratii
    temp = numar
    inv = 0
    while(numar > 0):
    # Prin intermediul variabilei inv reusesc sa formez in numarul in sens invers
        cifra = numar % 10
        inv = inv * 10 + cifra
        numar = numar // 10
    # Verific daca numarul este egal cu inversul sau
    if(temp == inv):
        print("Numarul este un palindrom")
    else:
        print("Numarul nu este un palindrom")

# Write a function that extract a number from a text (for example if the text is
# "An apple is 123 USD", this function will return 123, or if the text is "abc123abc"
# the function will extract 123). The function will extract only the first number that is found

def gasesteNumarul(text):
    numar = ""
    for i in range(len(text)):
        # Daca caracterul de care am dat este cifra, le caut in continuare pe restul, daca este cazul
        if text[i].isdigit():
            while i < len(text) and text[i].isdigit():
                numar += text[i]
                i += 1
            break
    # Daca numar nu are nicio valoare, ne returneaza un mesaj, similar pt cazul contrar
    if not numar:
        print("Nu este niciun numar")
    else:
        print("Numarul este: ", numar)

palindrom(7)
gasesteNumarul("abc123abc")
