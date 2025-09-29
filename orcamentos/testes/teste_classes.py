import unittest
from classes_imoveis import Apartamento, Casa, Estudio, Orcamento


class TestApartamento(unittest.TestCase):

    def test_apartamento_1_quarto_sem_garagem(self):
        ap = Apartamento(quartos=1, garagem=False, possui_criancas=True)
        self.assertEqual(ap.calcular_aluguel(), 700)

    def test_apartamento_2_quartos_com_garagem(self):
        ap = Apartamento(quartos=2, garagem=True, possui_criancas=True)
        self.assertEqual(ap.calcular_aluguel(), 700 + 200 + 300)

    def test_apartamento_desconto_sem_criancas(self):
        ap = Apartamento(quartos=1, garagem=False, possui_criancas=False)
        self.assertEqual(ap.calcular_aluguel(), 700 * 0.95)


class TestCasa(unittest.TestCase):

    def test_casa_1_quarto_sem_garagem(self):
        casa = Casa(quartos=1, garagem=False)
        self.assertEqual(casa.calcular_aluguel(), 900)

    def test_casa_2_quartos_com_garagem(self):
        casa = Casa(quartos=2, garagem=True)
        self.assertEqual(casa.calcular_aluguel(), 900 + 250 + 300)


class TestEstudio(unittest.TestCase):

    def test_estudio_sem_vagas(self):
        est = Estudio(vagas=0, vagas_extras=0)
        self.assertEqual(est.calcular_aluguel(), 1200)

    def test_estudio_com_pacote_2_vagas(self):
        est = Estudio(vagas=2, vagas_extras=0)
        self.assertEqual(est.calcular_aluguel(), 1200 + 250)

    def test_estudio_com_vagas_extras(self):
        est = Estudio(vagas=2, vagas_extras=3)  # 250 + (3*60)
        self.assertEqual(est.calcular_aluguel(), 1200 + 250 + 180)


class TestOrcamento(unittest.TestCase):

    def test_orcamento_apartamento(self):
        ap = Apartamento(quartos=2, garagem=True, possui_criancas=False)
        orc = Orcamento(ap)
        resumo = orc.gerar_resumo()
        self.assertEqual(resumo["Imóvel"], "Apartamento")
        self.assertGreater(resumo["Valor mensal"], 0)
        self.assertEqual(resumo["Valor contrato"], 2000)


if __name__ == "__main__":
    unittest.main()
