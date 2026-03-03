class Dictionary:
    def __init__(self):
        self._dict={}

        pass

    def addWord(self,parolaAliena,traduzione):
        parolaAliena=parolaAliena.lower()
        if parolaAliena in self._dict:
            for t in traduzione:
                if t.lower in self._dict[parolaAliena]:
                    self._dict[parolaAliena].append(t.lower())
        else :
            self._dict[parolaAliena]=[t.lower for t in traduzione]


    def translate(self,parolaAliena):
        return self._dict.get(parolaAliena.lower(),None)




    def translateWordWildCard(self):

        pass