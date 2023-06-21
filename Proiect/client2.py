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
        return mesaj_primit


# am tratat cazul in care clientul 2 poate trimite de la tastatura 2 sau mai multe caractere
def only_one_char(litera):
    if len(litera) > 1:
        return False
    return True


def client_gives_letter():
    while True:
        litera = input("[server]: Ghiceste o litera: ")
        if only_one_char(litera):
            return litera
        print("[server]: Trebuie sa introduci o singura litera.")


while True:
    text = read()
    print(text)
    # am tratat cazurile in care acel text este returnat de server pt a fi sigur ca programul se termina
    if (
        text == ""
        or "Invitatul 1 s-a deconectat" in text
        or "Felicitari" in text
        or "Cuvantul era: " in text
    ):
        exit(0)
    send(client_gives_letter())
    print(read())
