class TV:

    def __init__(self, marca, polegadas, smart):
        self.marca = marca
        self.largura = None
        self.altura = None
        self.profundidade = None
        self.cor = None
        self.polegadas = polegadas
        self.smart = smart
        self.canalatual = None
        self.status = None
        self.volume = None

    def trocar_canal(self):
        pass


tv_sala = TV('Philco', 58, 'SIM')
tv_quarto = TV('AOC', 42, 'NÃO')






    # cor = 'preta'

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        if (novo_canal == "Netflix"):
            self.canal = "Disney+"
        elif (novo_canal == "Disney+"):
            self.canal = "PrimeVideo"
        else:
            self.canal = "Netflix"


tv_sala = TV(75)
tv_quarto = TV(32)

TV.cor = 'branca'
tv_quarto.tamanho = 32

tv_sala.mudar_canal(tv_sala.canal)
tv_quarto.mudar_canal(tv_quarto.canal)
tv_sala.mudar_canal(tv_sala.canal)

print(tv_quarto.cor)
print(tv_quarto.tamanho)
print(tv_quarto.canal)

print()

print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.canal)





