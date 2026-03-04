from dictionary import Dictionary
class Translator:

    def __init__(self):
        self._dict = Dictionary()


    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("-" * 30)
        print("  Traduttore italiano-alieno")
        print("-" * 30)
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("-" * 30)


    def loadDictionary(self, fileName):
        # dict is a string with the filename of the dictionary
        with open(fileName,"r",encoding="utf-8") as f:
            for line in f:
                campi=line.strip().split(" ")
                if len(campi)>=2:
                    self._dict.addWord(campi[0],campi[1:])


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi= entry.split(" ")
        parolaAliena=campi[0]
        traduzione=campi[1]
        if not parolaAliena.isalpha():
            print("Errore: la parola deve contenere solo lettere")
            return

        self._dict.addWord(parolaAliena,traduzione)
        print("parola aggiunta")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if not query.isalpha():
            print("Errore: la query deve contenere solo lettere")
            return
        risultato=self._dict.translate(query)
        print(risultato if risultato else "non trovata")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        if query.count("?")!=1:
            print("può contenere solo un carattere ?")
            return
        risultato=self._dict.translateWordWildCard(query)
        print(risultato if risultato else "non trovata")


        pass