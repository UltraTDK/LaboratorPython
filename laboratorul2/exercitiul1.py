# Find The greatest common divisor of multiple numbers read from the console

print("Cate numere vrei sa introduci?")
lungimeSir= int(input())
# numerele trebuie scrise pe un rand separat apasand tasta enter
print("Introdu numerele: ")
numar1 = int(input())
cmmdc = numar1
for i in range(1, lungimeSir):
    numar2 = int(input())
    # functie cmmdc
    while numar2 != cmmdc:
        if numar2 > cmmdc:
            numar2 = numar2 - cmmdc
        else:
            cmmdc -= numar2
print(cmmdc)