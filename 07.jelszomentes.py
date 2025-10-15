## jelszo bekérő egyszerübb - jelszo mentés a függvényben van
def jelszomegadas():
    megadott_jelszo = input("Adj meg egy jelszot:   ")

    while len(megadott_jelszo) < 6:
        print("Jelszónak min 6 karakter hosszúnak kell lennie. ")
        megadott_jelszo = input("Adj meg egy másik jelszót: ")

    with open("Jelszo2.txt", "w") as jelszo_file:
        jelszo_file.write(megadott_jelszo)



#Jelszó bekérő függvényes feladat
def jelszobekero():
    jelszo = 0
    
    while len(str(jelszo)) < 6:
        jelszo = input("Add meg a jelszot!  ")
        jelszo = jelszo.strip()
        jelszoellenorzo(jelszo)

def jelszoellenorzo(ellenorzendo_jelszo):
    if len(str(ellenorzendo_jelszo)) >= 6:
        jelszo_mentes(ellenorzendo_jelszo)
    else:
        print("jelszónak min. 6 karakter hosszúnak kell lennie")
        
def jelszo_mentes(mentendo_jelszo):
    with open ("jelszo.txt", "w") as file:
        file.write(mentendo_jelszo)
        print("jelszo sikeresen mentve")


jelszobekero()





