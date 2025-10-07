import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from classes_imoveis import Apartamento, Casa, Estudio


from classes_imoveis import Apartamento, Casa, Estudio

def test_apartamento_simples():
    ap = Apartamento(quartos=1, garagem=False, possui_criancas=True)
    assert ap.calcular_aluguel() == 700

def test_apartamento_completo_com_desconto():
    ap = Apartamento(quartos=2, garagem=True, possui_criancas=False)
    assert ap.calcular_aluguel() == 1140  # (700 + 200 + 300) * 0.95

def test_casa_2_quartos_com_garagem():
    casa = Casa(quartos=2, garagem=True)
    assert casa.calcular_aluguel() == 1450  # 900 + 250 + 300

def test_estudio_com_vagas_extras():
    est = Estudio(vagas=2, vagas_extras=3)
    assert est.calcular_aluguel() == 1630  # 1200 + 250 + 180
