from easygui import msgbox, enterbox, codebox, buttonbox
import sys


def uzenet(szoveg):
    """
    Uzenetet mutatunk a felhasznalonak. 
    """
    msgbox(szoveg)


def nevolvasas():
    """
    Megnyitja a 'nev.txt' nev� file-t ovlas�sra, �s a tartalm�val t�r vissza.
    """
    f = open("nev.txt", 'r')
    nev = f.read()
    f.close()
    return nev


def pontszamok(targyak_listaja):
    """
    Ez a f�ggv�ny egy t�rgylist�t kap param�terk�nt, �s a bel�l defini�lt
    pontsz�mok alapj�n kisz�m�tja, hogy a kapott lista h�ny pontot �r.
    Ez a pont�rt�k lesz a f�ggv�ny visszat�r�si �rt�ke.
    """
    pontertekek = {
        "balta": 1,
        "pancel": 5,
        "pajzs": 3,
        "lada": 3,
        "kard": 4,
        "sisak": 2
        }

    osszpontszam = 0

    for targy in targyak_listaja:
        osszpontszam += pontertekek[targy]

    return osszpontszam


def nevvalasztas():
    nev = enterbox("Add meg a neved! ", title="játékos neve")
    with open("nev.txt", "w") as f:
        f.write(nev)
    return nev


def utvalasztas_uzenettel():
    """
    Ez a f�ggv�ny csak megh�vja az �tv�laszt� f�ggv�nyt, �s el�tte,
    ut�na sz�vegets �zeneteket �r a j�t�kosnak.
    Visszat�r�si �rt�ke a v�lasztott �t sz�ma.
    """
    
    uzenet = """
Útelágazáshoz értél. Három út van előtted...
De tudod, hogy az egyik csapdát rejt!
Merre indulsz?"""
    
    valasztott_ut = buttonbox(uzenet, "Merre indulsz?", ("Balra", "Egyenesen", "Jobbra", "Kilépés", "Tárgylista"))

    if valasztott_ut == "Balra":
        return 1
    elif valasztott_ut == "Egyenesen":
        return 2
    elif valasztott_ut == "Jobbra":
        return 3
    elif valasztott_ut == "Kilépés":
        sys.exit(0)
    elif valasztott_ut == "Tárgylista":
        return 4
    

