import translator as tr
import networkx as nx
t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("\n selezione un'opzione")
    if not txtIn.isnumeric():
        print("inserisci un numero valido")

    scelta = int(txtIn)

    if scelta == 1:
        entry=input("inserisci<parola aliena><traduzione italiana> :").lower()
        t.handleAdd(entry)
    elif scelta == 2:
        query = input("quale parola vuoi tradurre ? :").lower()
        t.handleTranslate(query)
    elif scelta == 3:
        query = input("quale parola vuoi tradurre con il simbolo '?' :").lower()
        t.handleWildCard(query)
    elif scelta == 4:
        for chiave,valore in t._dict._dict.items():
            print(f"{chiave} ---> {valore}")

    elif scelta == 5:
        break
    else:
        print("opzione non valida")


    # Add input control here!

