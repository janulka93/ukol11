class Ctverec:
    def __init__(self, strana):
        self.strana = strana
    def obvod(self):
        self.obvod = 4*self.strana
        return self.obvod
    def obsah(self):
        self.obsah = self.strana**2
        return self.obsah
    def rozdil_obsahu(self, jiny_ctverec):
        return self.obsah - jiny_ctverec.obsah
