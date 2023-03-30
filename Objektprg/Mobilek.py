class Mobil:
    def __init__(self, znacka, pamet, audio_out):
        self.znacka = znacka
        self.pamet = pamet
        self.os = "Android"
        self.a_out = audio_out
    def add5G(self, je5G):
        self.je5G = je5G

mobilek = Mobil("Samsung", "64GB", True)
print(mobilek.znacka)
print(mobilek.os)
print(mobilek.a_out, end="\n\n")
mobil2 = Mobil("Moto", "128GB", False)
print(mobil2.znacka)
print(mobil2.os)
print(mobil2.a_out)
