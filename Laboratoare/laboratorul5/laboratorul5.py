import os
import sys

# Exercitiul 1
# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
def functie1(direc):
    out = []
    # parametrii de care are nevoie os.walk
    # by default imi cauta topdown in folder
    for radacina, foldere, fisiere in os.walk(direc):
        for fisier in fisiere:
            # am divizat calea fisierului in doua parti, nume si extensie
            extensie = os.path.splitext(fisier)
            if extensie[1] != "":
                out.append(extensie[1])
    return sorted(out)
print("1.", functie1("../Laborator"))


# Exercitiul 2
# Să se scrie o funcție ce primește ca argumente două căi: director si fișier
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul directorului de la calea folder, care incepe cu litera A. 
def functie2(director, fisier):
    with open(fisier, "w") as my_file:
        for file in os.listdir(director):
            # obtin calea absoluta a unui fisier
            cale_fisier = os.path.abspath(file)
            # verific daca este fisier si daca incepe cu litera A
            if os.path.isfile(cale_fisier) and file.startswith("A"):
                my_file.write(cale_fisier + "\n")
print("2.", functie2(".", "cale_absoluta.txt"))
            

# Exercitiul 3
# Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. 
def functie3(my_path):
    count = 0
    if os.path.isfile(my_path):
        with open(my_path, "r") as my_file:
            if os.path.getsize(my_path) >= 20:
                # returneaza ultimele 20 de caractere dintr-un fisier
                # -20: - parcurge 20 de caractere de la coada la cap
                return my_file.read()[-20:]
            else:
                return "Fisierul nu are mai mult de 20 de caractere."
    elif os.path.isdir(my_path):
        lista_tuple = {}
        for radacina, foldere, fisiere in os.walk(my_path):
            for fisier in fisiere:
                # am creat un dictionar cu extensii + countul fiecarei extensii
                extensie = os.path.splitext(fisier)
                if extensie[1] in lista_tuple:
                    lista_tuple[extensie[1]] += 1
                # initializez fiecare extensie
                else:
                    lista_tuple[extensie[1]] = 1
    
    lista_recursiv = sorted(lista_tuple, key = lambda x: lista_tuple[x], reverse = True)
    out = []
    for elem in lista_recursiv:
        pereche = (elem, lista_tuple[elem])
        out.append(pereche)
    return out
# Verificare pt director
# print("3.", functie3("../Laborator"))
# Verificare pt fisier
print("3.", functie3("exemplu.txt"))

# Exercitiul 4
# Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală. 
def functie4():
    # trebuie sa apelez fisierul de la linia de comanda
    # de exemplu: py laboratorul5/laboratorul5.py .  --> cu "." imi cauta in tot folderul Laborator   
    cale_dir = sys.argv[1]
    lista_tuple = {}
    out = []
    for radacina, foldere, fisiere in os.walk(cale_dir):
        for fisier in fisiere:
            extensie = os.path.splitext(fisier)
            if extensie[1] in lista_tuple:
                lista_tuple[extensie[1]] += 1
            else:
                lista_tuple[extensie[1]] = 1
    for elem in lista_tuple.keys():
        # caut elementele unice
        if lista_tuple[elem] == 1:
            out.append(elem)
    return sorted(out)
# print("4.", functie4())

# Exercitiul 5
# Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
def functie5(target, to_search):
    content = ""
    target_dir = []
    if os.path.isfile(target):
        with open(target, "r") as my_file:
            content = my_file.read()
            if to_search in content:
                return [target]
            else:
                return []
    elif os.path.isdir(target):
        for radacina, foldere, fisiere in os.walk(target):
            for fisier in fisiere:
                if os.path.isfile(fisier):
                    with open(fisier, "r") as my_file:
                        content = my_file.read()
                        if to_search in content:
                            target_dir.append(fisier)
        return target_dir
    else:
        # conform cerintei am aruncat o exceptie
        raise ValueError("Nu este nici fisier nici director.")
    
# print("5.", functie5("laboratorul5/laboratorul5.py", "exemplu.txt"))
print("5.", functie5("../Laborator", "exemplu.txt"))

# Exercitiul 6
# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
def exceptie(except_):
    print(except_)

def functie6(target, to_search, callback_func):
    try:
        return functie5(target, to_search)
    except Exception as exception:
        return callback_func(exception)
print("6.", functie6("../Laborator", "exemplu.txt", exceptie))

# Exercitiul 7
# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
def functie7(path):
    file_ext = ""
    if os.path.splitext(path)[1] != "":
        file_ext = os.path.splitext(path)[1]
    else:
        file_ext = ""
    path_info = {
        "full_path": os.path.abspath(path),
        # getsize - ia dimensiunea fisierului in octeti/bytes
        "file_size": os.path.getsize(path),
        "file_extension": file_ext,
        # verific daca am dreptul sa citesc
        "can_read": os.access(path, os.R_OK),
        # verific daca am dreptul sa scriu
        "can_write": os.access(path, os.W_OK)
    }
    return path_info
print("7.", functie7("laboratorul5/laboratorul5.py"))

# Exercitiul 8
# Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

# Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
def functie8(dir_path):
    out = []
    for fisier in os.listdir(dir_path):
        if os.path.isfile(fisier):
            out.append(os.path.abspath(fisier))
    return out
print("8.", functie8("../Laborator"))