# -*- coding: ISO-8859-2 -*-

# Importok
from random import randint
from kilences_lecke_easyguiUI import *
###from kilences_lecke_konzolUI import *

# -----------------------------------------------------------------
# F�ggv�ny defin�ci�k
# -----------------------------------------------------------------

def udvozlet():
    """
    Ez a f�ggv�ny j�t�k eleji �dv�zl� sz�veget �r ki.
    """
    
    szoveg = """
------------------------
Üdvözöllek a játékomban!
------------------------
Juss messzebb az erdőben!
"""
    uzenet(szoveg)


def sorsol():
    """
    Ez a f�ggv�ny egy v�letlenszer� t�rgyat sorsol ki
    egy benne defini�lt list�b�l, �s azzal t�r vissza.
    """
    targyak = ["balta", "pancel", "pajzs", "lada", "kard", "sisak"]
    index = randint(0, len(targyak) - 1)
    return targyak[index]


def kiir_fejlett(targyak):
    """
    Ez a f�ggv�ny param�terk�nt megkapja a j�t�kos �ltal gy�jt�tt t�rgyak
    list�j�t, �s mindegyiket ki�rja a pontsz�mokkal egy�tt, valamint az
    �sszesen gy�jt�tt pontok sz�m�t, �s egy�b �zeneteket.
    """
    pontertekek = {
        "balta": 1,
        "pancel": 5,
        "pajzs": 3,
        "lada": 3,
        "kard": 4,
        "sisak": 2
        }
    
    targylista_szoveg = ""

    for targy in targyak: 
        targylista_szoveg += "    - " + targy + ": " + str(pontertekek[targy]) + "\n"
    
    szoveg = """
Ezeket a targyakat szerezted:
{}

Összpontszám: {}
""".format(targylista_szoveg, pontszamok(targyak))

    uzenet(szoveg)
    

def aranyat_talaltal(uj_arany, osszes_arany):
    """
    Ezt a f�ggv�nyt akkor kell h�vni, ha a j�t�kos aranyat tal�l.
    Meg kell neki adni a kapott arany �rt�k�t (int), �s a jelenleg
    n�la l�v� aranymennyis�get (int) ilyen sorrendben.
    A f�ggv�ny kisz�molja az �j aranymennyis�get. Ki�rja a kapott,
    �s az �sses arany �rt�k�t. Visszat�r�si �rt�ke az �j
    aranymennyis�g.
    """
    
    # Sz�mol�s
    osszes_arany += uj_arany
    
    # Ki�r�sok
    szoveg = """
    Megbotlasz valamiben...
    Lenézel a lábad elé...
    Találtál """ + str(uj_arany) + """ aranyat.
    Most """ + str(osszes_arany) + """aranyad van.
    """
    uzenet(szoveg)
    
    # Visszat�r�s
    return osszes_arany

    
def csapdara_leptel(osszes_elet):
    """
    Doc komment
    """

    # �let levon�sa
    osszes_elet -= 1

    # Kiir�s
    if osszes_elet == 0:
        uzenet("Sajnos meghalt�l!")
    else:
        uzenet("Csapda! M�r csak " + str(osszes_elet) + " �leted van!")

    # Visszat�r�s
    return osszes_elet


def viszlat(megtett_tavolsag, gyujtott_arany):
    """
    Ez a f�ggv�ny elk�sz�n a j�t�k v�g�n, �s ki�rja az el�rt eredm�nyeket. 
    """

    nev = nevolvasas()

    szoveg = """
-------------------------------------------------
Sajnos vége a játéknak, {}...
-------------------------------------------------
Megtett távolság: {}
Gyújtött arany: {}
""".format(nev, megtett_tavolsag, gyujtott_arany)
    
    uzenet(szoveg)



# -----------------------------------------------------------------
# Itt kezd�dik a f� program
# -----------------------------------------------------------------

# V�ltoz�k kezdeti be�ll�t�sa
eletek = 2      # Ennyi �lettel kezd a j�t�kos
tavolsag = 0    # Ebben fogjuk sz�molni a megtett utat (vagyis hogy h�ny el�gaz�st �lt t�l)
arany = 0       # A j�t�kos mindenkori aranyk�szlete
targylista = [] # Ez a lista tartalmazza majd 

nev = nevvalasztas() # A j�t�kos neve, file-ba is kimentve

# Kezdeti �zenetek ki�r�sa
udvozlet()

# Fixen 5 aranyat tal�lunk a j�t�k elej�n
talalt_arany = 5
arany = aranyat_talaltal(talalt_arany, arany)

# F� ciklus
while eletek > 0: # Addig ism�telj�k, am�g 0-n�l t�bb �let�nk van
    
    # �t kiv�laszt�sa �zenetekkel
    valasztott_ut = utvalasztas_uzenettel()
    
    # Csapda kisorsol�sa
    csapda_ut = randint(1, 3)
    targy_ut = randint(1, 3)

    targylista_valasztas = 4

    # Adatok feldolgoz�sa
    if valasztott_ut == targylista_valasztas:
        kiir_fejlett(targylista)
    elif csapda_ut == valasztott_ut: # Ha a j�t�kos csapd�ra l�pett
        eletek = csapdara_leptel(eletek)
    elif targy_ut == valasztott_ut:
        uj_targy = sorsol()
        uzenet("Tal�lt�l egy " + uj_targy + " t�rgyat")
        targylista.append(uj_targy)
    else: # Ha a j�t�kos nem l�pett csapd�ra
        uzenet("Biztons�gos �t! Most tov�bb mehetsz.")
        tavolsag = tavolsag + 1
        
        # Aranyat tal�ltunk
        talalt_arany = randint(1, 10)
        arany = aranyat_talaltal(talalt_arany, arany)
        
# Ha v�ge a j�t�knak
viszlat(tavolsag, arany)
kiir_fejlett(targylista)
