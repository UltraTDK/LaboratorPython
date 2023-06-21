"""
      Se va crea o aplicatie de tip client server care va produce jocul de cuvinte "Spanzuratoarea".
      Vor exista 2 clienti, unul care va da cuvantul si o mica explicatie catre server, iar celalalt 
    care va raspunde cu cate o litera pana fie reuseste sa ghiceasca cuvantul, pana fie pierde.
    INPUT:  server.py (cuvant + definitie)
        client2.py (trimite cate o litera si va primi de la server o linie pe care va scrie:
    _ _ _ c _ _ 5 daca litera "c" este ok, _ _ _ _ _ _ 4 daca litera "c" nu este ok.
"""

import server

server.start()
