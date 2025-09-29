import csv
import os


class Imovel:
    def __init__(self, preco_base, quartos=1, possui_criancas = True):
        self.preco_base = preco_base
        self.quartos = quartos
        self.possui_criancas = possui_criancas


    def calcular_aluguel(self):
        return self.preco_base


    def detalhes(self):

        return {
            "Tipo": self.__class__.__name__,
            "Quartos": self.quartos,
            "Preço base": self.preco_base
        }

class Apartamento(Imovel):
    def __init__(self, quartos = 1, garagem = False, possui_criancas = True):
        super().__init__(preco_base=700, quartos = quartos, possui_criancas= possui_criancas)
        self.garagem = garagem


    def calcular_aluguel(self):
        valor = self.preco_base

        if self.quartos == 2:
            valor += 200
        if self.garagem:
            valor += 300
        if not self.possui_criancas:
            valor *= 0.95

        return valor

class Casa(Imovel):
    def __init__(self, garagem = False, quartos = 1):
        super().__init__(preco_base= 900, quartos= quartos)
        self.garagem = garagem


    def calcular_aluguel(self):
        valor = self.preco_base
        if self.quartos == 2:
            valor += 250
        if self.garagem:
            valor += 300
        return valor

class Estudio(Imovel):
    def __init__(self, vagas = 0, vagas_extras = 0):
        super().__init__(preco_base= 1200)
        self.vagas = vagas
        self.vagas_extras = vagas_extras

    def calcular_aluguel(self):
        valor = self.preco_base
        if self.vagas >= 2:
            valor += 250
        if self.vagas_extras >= 0:
            valor += self.vagas_extras * 60

        return valor

class Orcamento:
    def __init__(self, imovel):
        self.imovel = imovel
        try:
            self.valor_mensal = imovel.calcular_aluguel()
        except Exception as e:
            print(f"Erro ao calcular valor do imóvel: {e}")
            self.valor_mensal = 0
        self.valor_contrato = 2000

    def gerar_resumo(self):
        try:
            return {
                "Imóvel": self.imovel.__class__.__name__,
                "Valor mensal": self.valor_mensal,
                "Valor contrato": self.valor_contrato
            }
        except Exception as e:
            print(f"Erro ao gerar resumo: {e}")
            # 🚨 retorna um dicionário seguro, nunca vazio
            return {
                "Imóvel": "Indefinido",
                "Valor mensal": 0,
                "Valor contrato": 0
            }

    def gerar_csv(self, caminho="orcamentos/orcamento.csv"):
        try:
            # garante que a pasta existe
            os.makedirs(os.path.dirname(caminho), exist_ok=True)

            with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["Mês", "Parcela (R$)"])
                for mes in range(1, 13):
                    escritor.writerow([mes, self.valor_mensal])
            print(f"✅ Arquivo CSV gerado com sucesso em {caminho}")
        except Exception as e:
            print(f"Erro ao gerar CSV: {e}")