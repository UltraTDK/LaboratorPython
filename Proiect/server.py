import socket
import string

# variabilele cu litere mari sunt constante python
# Lungimea mesajului trimis catre server (respectiv 256 de biti)
HEADER = 256
# Formatul in care sa fie decodat mesajul
FORMAT = "utf-8"
# Am ales un port care nu este folosit
PORT = 5500
# Pot folosi doua metode: 
#      una in care ip-ul este setat manual 
#      sau este preluat automat
# SERVER = "192.168.228.1" -> pt verificare
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# format: socket(family, type)
# AF_INET - pentru IPv4
# SOCK_STREAM - transmit un flux de date
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Am legat socketul de adresa
server_socket.bind(ADDR)

def send(mesaj, client):
    # Cand trimit un mesaj trebuie sa fie de tip byte object
    client.send(bytes(mesaj, encoding=FORMAT))

def read(client):
    # Astept informatii de la client
    mesaj_primit = client.recv(HEADER).decode()
    # verific daca mesajul nu este gol
    if mesaj_primit != None:
        return mesaj_primit
    
# server_socket.accept este o linie blocanta, pana cand serverul primeste feedback de la client
clienti = []
def start():
    print("[server]: a inceput petrecerea.")
    server_socket.listen()
    print(f"[server]: petrecerea este in camera: {SERVER}")
    while True:
        # Salvez adresa, iar mai apoi creez obiectul pe server
        conn, addr =  server_socket.accept()
        clienti.append(conn)

        if len(clienti) == 2:
            break
    invitat1 = clienti[0]
    invitat2 = clienti[1]
    send("[server]: ambii invitati au ajuns la petrecere.", invitat1)
    try:
        spanzuratoarea_func(invitat1, invitat2) 
    # am tratat cazul in care un client s-a deconectat de pe server
    except Exception as exceptie:
        print(exceptie)
    
def spanzuratoarea_func(client1, client2):
    player1 = [read(client1), read(client1)]
    cuvant = list(player1[0].upper())
    # am procedat asa, ca variabila cuvant_backup sa nu fie un alias
    # cuvant backup il folosesc pentru anumite verificari
    cuvant_backup = cuvant[:]
    hint = player1[1].upper()
    alfabet = list(string.ascii_uppercase)
    litere_folosite = []
    incercari = len(cuvant) - 1
    guess_word = []

    # cazul in care clientul 1 s-a deconectat, clientul 2 primeste un mesaj
    if player1[0] == "" and player1[0] == "":
        send("[server]: Invitatul 1 s-a deconectat.", client2)
        print("[server]: petrecerea s-a terminat.")
        exit(0)

    for i in range(0, len(cuvant)):
        guess_word.append('_')

    # o varianta care mi s-a parut accesebila este ca pe masura ce clientul 2 ghiceste o litera sa scad acea litera din cuvant
    # pana cand cuvantul este gol, moment in care executia se termina
    while len(cuvant) > 0 and incercari > 0:
        afisare_cuvant = (str(guess_word) + " incercari: " + str(incercari) + " Hint: " + str(hint))
        send(afisare_cuvant, client2)
        input_player2 = (read(client2)).upper()

        if input_player2 in cuvant and input_player2 in alfabet and input_player2 != "":
            send("[server]: am primit input de la client 2: " + input_player2, client2)
            pozitie = 0
            for litera_cuvant in cuvant_backup:
                if litera_cuvant == input_player2:
                    guess_word[pozitie] = input_player2
                    pozitie += 1
                else:
                    pozitie += 1
            litere_folosite.append(input_player2)
            if input_player2 in cuvant:
                cuvant.remove(input_player2)         
        elif input_player2 in litere_folosite:
            send("[server]: Ai folosit deja aceasta litera.", client2)
        elif input_player2 not in alfabet:
            send("[server]: Caracterul folosit nu face parte din alfabet.", client2)
        else:
            # Cazul in care litera nu este in cuvant
            incercari -= 1
            send("[server]: Litera nu face parte din cuvant", client2)
        if incercari == 0:
            send("[server]: Ai ramas fara incercari. Cuvantul era: " + str(cuvant_backup) + "\n", client2)
    if cuvant_backup == guess_word:
        send("[server:] Felicitari! Ai ghicit cuvantul: " + str(guess_word), client2)
    else:
        send("[server]: Incercarea ta: " + str(guess_word), client2)

    print("[server]: petrecerea s-a terminat.")
