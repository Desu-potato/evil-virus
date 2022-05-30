class bigFile:
    def __init__(self):
        self.goal = 4
        self.cell = 5
        self.files = 0
        self.raw = b''

    def create(self, name):
        self.file = open(ascii(name)+"dead" + ascii(self.files) + ".txt", "wb+")
        self.files = self.files + 1

    def generate(self):
        bufor = b'a'
        b = self.cell*self.goal
        for x in range(0, b):
            bufor =  (bufor*2 )+ bufor

        return bufor


    def fill(self, name, big):
        beta = True
        i = 0
        while beta:
            i = i+1
            if i == big:
                beta = False
            self.create(name)
            self.file.write(self.raw)


def init():
    interface = bigFile()
    base = interface.generate()
    interface.raw = base
    interface.fill("", 2)



if __name__ == '__main__':
    init()

