# Write a script that receives two strings and prints the number of occurrences of the first string in the second

def counterAparitii(str1, str2):
    counter = 0
    for aparitie in range(len(str2) - len(str1) + 1):
        if str2[aparitie:aparitie+len(str1)] == str1:
            counter += 1
    print("Numarul de aparitii: ", counter)

print("Introdu primul cuvant: ")
string1 = str(input())
print("Introdu al doilea cuvant: ")
string2 = str(input())
print(counterAparitii(string1, string2))
