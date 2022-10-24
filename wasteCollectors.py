class WasteCollectors:
    def __init__(self,name,address,telephone,mail):
        self.name = name
        self.address=address
        self.telephone=telephone
        self.mail=mail


    def print(self):
        print(self.name)
        print(self.mail)
        print(self.address)
        print(self.telephone)


