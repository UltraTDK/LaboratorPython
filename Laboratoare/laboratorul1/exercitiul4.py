# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores

print("Introdu un string de la tastatura: ")
stringUpperC = str(input())
stringLowerU = ""

for i in range(len(stringUpperC)):
    if stringUpperC[i].isupper():
        if i == 0:
            stringLowerU += stringUpperC[i].lower()
        else:
            stringLowerU += "_" + stringUpperC[i].lower()
    else:
        stringLowerU += stringUpperC[i]

print("Stringul modificat: ", stringLowerU)
