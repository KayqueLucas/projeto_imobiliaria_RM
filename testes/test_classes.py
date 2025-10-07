import unittest
from classes_imoveis import Apartamento, Casa, Estudio, Orcamento


class TestApartamento(unittest.TestCase):

    def test_apartamento_basico(self):
        ap = Apartamento(quartos=1, garagem=False, possui_criancas=True)
        self.assertEqual(ap.calcular_aluguel(), 700)

    def test_apartamento_completo_com_desconto(self):
        ap = Apartamento(quartos=2, garagem=True, possui_criancas=False)
        self.assertEqual(ap.calcular_aluguel(), 1140)  # (700 + 200 + 300) * 0.95


class TestCasa(unittest.TestCase):

    def test_casa_completa(self):
        casa = Casa(quartos=2, garagem=True)
        self.assertEqual(casa.calcular_aluguel(), 1450)


class TestEstudio(unittest.TestCase):

    def test_estudio_com_vagas(self):
        est = Estudio(vagas=2, vagas_extras=3)
        self.assertEqual(est.calcular_aluguel(), 1630)


class TestOrcamento(unittest.TestCase):

    def test_orcamento_gerado(self):
        ap = Apartamento(quartos=2, garagem=True, possui_criancas=False)
        orc = Orcamento(ap)
        resumo = orc.gerar_resumo()
        self.assertEqual(resumo["Imóvel"], "Apartamento")
        self.assertGreater(resumo["Valor mensal"], 0)
        self.assertEqual(resumo["Valor contrato"], 2000)


if __name__ == "__main__":
    unittest.main()
