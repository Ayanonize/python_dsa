class MainClass():

    def __init__(self):
        self.data = {
            "a": "y",
            "b": "e",
            "c": "s",
        }

    def decode(self,input_):
        finalString = ""
        for x in input_:
            finalString += self.data[x]
        return finalString

main = MainClass()
print(main.decode("abc"))
# code
