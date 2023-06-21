import socket

# Lungimea mesajului trimis catre server (respectiv 256 bits)
HEADER = 256
# Formatul in care vreau sa fie decodat
FORMAT = "utf-8"
PORT = 5500
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(mesaj):
    # Cand trimit un mesaj trebuie sa fie de tip byte object
    client.send(bytes(mesaj, encoding=FORMAT))


def read():
    # Astept informatii de la client
    mesaj_primit = client.recv(HEADER).decode(FORMAT)
    # verific daca mesajul nu este gol
    if mesaj_primit != None:
        print(mesaj_primit)


def client_gives_word():
    word = input("[server]: Scrie un cuvant: ")
    hint = input("[server]: Ofera un hint: ")
    return word, hint


read()

cuvant, hint = client_gives_word()

send(cuvant)
send(hint)
read()
