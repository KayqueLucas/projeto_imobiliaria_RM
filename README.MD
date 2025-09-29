# 🏠 Projeto Imobiliária R.M - Orçamento de Aluguel

Este projeto foi desenvolvido como parte da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**.  
O objetivo é criar uma aplicação que **gera orçamentos de aluguel** para diferentes tipos de imóveis da Imobiliária R.M, aplicando regras de negócio pré-definidas.

---

## 🎯 Funcionalidades
- Cálculo do aluguel mensal para **Apartamentos, Casas e Estúdios**.
- Regras de negócio implementadas:
  - Acréscimo para imóveis com 2 quartos.
  - Acréscimo para garagem (casas/apartamentos).
  - Acréscimo para vagas de estacionamento (estúdios).
  - Desconto de 5% em apartamentos sem crianças.
- Exibição do **valor mensal final** e do **contrato (R$ 2.000,00, parcelável em até 5x)**.
- Geração de um arquivo **.csv** com as 12 parcelas do aluguel.

---

## 📂 Estrutura de Pastas

projeto_imobiliaria_RM/

├── main.py # Arquivo principal para executar o programa
├── classes_imoveis.py # Contém as classes (Imovel, Apartamento, Casa, Estudio, Orcamento)
├── orcamentos/ # Pasta onde serão salvos os arquivos CSV
├── README.md # Documentação do projeto
└── .gitignore # Arquivos a serem ignorados no repositório

---

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/KayqueLucas/projeto_imobiliaria_RM
Acesse a pasta:

bash
Copiar código
cd projeto_imobiliaria_RM
Execute o programa:

bash
Copiar código
python main.py
📊 Exemplo de Orçamento
Tipo: Apartamento

Quartos: 2

Garagem: Sim

Crianças: Não

Valor Final Mensal: R$ 1.140,00
Contrato: R$ 2.000,00 (parcelado em até 5x)

📝 Autor
Projeto desenvolvido por Kayque (Faculdade de ADS - 2025).