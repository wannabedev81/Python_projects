def uzenet(szoveg):
    """
    Uzenetet mutatunk a felhasznalonak. 
    """
    print(szoveg)

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
    nev = input("Add meg a neved! ")
    f = open("nev.txt", 'w')
    f.write(nev)
    f.close()
    return nev



def utvalasztas(maximum = 3):
    """
    Ez a f�ggv�ny bek�r egy sz�mot a j�t�kost�l.
    Ha a j�t�kos nem eg�sz, �zenetet ad, �s �jra k�ri.
    Ha az nem 1 �s 'maximum' k�z�tt van, �jra k�ri.
    A f�ggv�ny visszat�r�si �rt�ke a megadott sz�m lesz int t�pusk�nt.
    """

    # Kezd��rt�k. Helytelent adunk meg, hogy els� alkalommal mindenk�pp bel�pj�nk a while-ba
    valasztott_ut_szammal = 0
    
    # A ciklus addig ism�tl�dik, am�g rossz �rt�keket adunk meg
    while valasztott_ut_szammal < 1 or valasztott_ut_szammal > maximum:
        # Bek�r�s
        valasztott_ut_szoveggel = input("1-tol " + str(maximum) + "-ig v�laszthatsz: ")

        # Megpr�b�ljuk konvert�lni
        try:
            valasztott_ut_szammal = int(valasztott_ut_szoveggel)
        except:
            # Ha nem konvert�lhat� int-t�, �zenetet adunk �s �jrakezdj�k a ciklust
            print("K�rlek, eg�sz sz�mot adj meg!")
            continue

        # Ha int, de nem a megfelel� hat�rok k�z�tt van
        if valasztott_ut_szammal < 1:
            print("A v�lasztott �tnak 0 f�l�tt kell lennie!")
        elif valasztott_ut_szammal > maximum:
            print("A v�lasztott �tnak " + str(maximum + 1) + " alatt kell lennie!")
            
            
    # Visszat�r�s a kiv�lasztott �ttal
    return valasztott_ut_szammal


def utvalasztas_uzenettel():
    """
    Ez a f�ggv�ny csak megh�vja az �tv�laszt� f�ggv�nyt, �s el�tte,
    ut�na sz�vegets �zeneteket �r a j�t�kosnak.
    Visszat�r�si �rt�ke a v�lasztott �t sz�ma.
    """
    print(
"""
�tel�gaz�shoz �rt�l. H�rom �t van el�tted...
De tudod, hogy az egyik csapd�t rejt!
Merre indulsz?")

    - 1 balra
    - 2 egyenesen
    - 3 jobbra
    - 4 tárgylista

""")
    
    valasztott_ut = utvalasztas(4)
    
    print("")

    return valasztott_ut
