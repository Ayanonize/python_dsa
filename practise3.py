class MainClass():
    def __init__(self):
        self.data = {
            "a": "y",
            "b": "e",
            "c": "s",
        }

    def decode(self,_input):
        finalString = ""
        for x in _input:
            finalString += self.data[x]
        return finalString

main = MainClass()
print(main.decode("abc"))
