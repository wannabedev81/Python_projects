def jelszofilenyito():
    try:
        with open("jelszo.txt", "r") as file:
            tartalom = file.read()
            print(tartalom)
    except:
        print("A file nem találhato")
        

    
    
jelszofilenyito()