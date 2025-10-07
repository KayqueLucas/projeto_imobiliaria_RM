# 🏠 Projeto Imobiliária R.M - Orçamento de Aluguel

Este projeto foi desenvolvido como parte da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**.
O objetivo é criar uma aplicação que **gera orçamentos de aluguel** para diferentes tipos de imóveis da Imobiliária R.M, aplicando regras de negócio pré-definidas com base no tipo de imóvel e nas preferências do cliente.

---

## 🎯 Funcionalidades

-   Cálculo do aluguel mensal para **Apartamentos, Casas e Estúdios**.
-   Regras de negócio implementadas:
    -   Acréscimo para imóveis com 2 quartos.
    -   Acréscimo para garagem (casas/apartamentos).
    -   Acréscimo para vagas de estacionamento (estúdios).
    -   Desconto de 5% em apartamentos sem crianças.
-   Exibição do **valor mensal final** e do **valor do contrato (R$ 2.000,00, parcelável em até 5x)**.
-   Geração automática de arquivo **`.csv`** com as 12 parcelas do aluguel.
-   Tratamento de erros com `try/except` em todas as operações sensíveis.
-   Loop interativo para permitir vários orçamentos consecutivos.
-   Testes automatizados com **unittest** e **pytest**.
-   Script automático para rodar todos os testes com apenas um comando (`rodar_testes.py`).

---

## ⚙️ Tecnologias Utilizadas

-   **Python 3.11+**
-   **Paradigma Orientado a Objetos (POO)**
-   **Bibliotecas padrão:**
    -   `csv` (para geração de arquivos)
    -   `os` e `sys` (manipulação de diretórios e caminhos)
    -   `unittest` (testes automatizados)
-   **Biblioteca externa:**
    -   `pytest` (para execução e validação de testes)

---

## 📂 Estrutura de Pastas

```
projeto_imobiliaria_RM/
├── main.py                 # Arquivo principal para executar o programa
├── classes_imoveis.py      # Contém as classes (Imovel, Apartamento, Casa, Estudio, Orcamento)
├── orcamentos/             # Pasta onde serão salvos os arquivos CSV
├── tests/                  # Pasta com testes automatizados
│   ├── test_classes.py
│   └── test_imoveis.py
├── rodar_testes.py         # Script que executa pytest e unittest automaticamente
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivos a serem ignorados no repositório
```

---

## 🚀 Como Executar

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/KayqueLucas/projeto_imobiliaria_RM](https://github.com/KayqueLucas/projeto_imobiliaria_RM)
    ```
2.  **Acesse a pasta do projeto:**
    ```bash
    cd projeto_imobiliaria_RM
    ```
3.  **Execute o programa principal:**
    ```bash
    python main.py
    ```
4.  **(Opcional) Execute todos os testes automaticamente:**
    ```bash
    python rodar_testes.py
    ```
    O script irá instalar o `pytest` (caso ainda não tenha) e rodar os testes com `pytest` e `unittest`.

### 🧪 Rodando os Testes Manualmente

Você também pode rodar os testes manualmente:

🔹 **Usando Pytest:**
```bash
python -m pytest -v
```

🔹 **Usando Unittest:**
```bash
python -m unittest discover tests
```

---

### 📊 Exemplo de Orçamento

| Tipo de Imóvel | Quartos | Garagem | Crianças | Valor Final | Contrato                                  |
| :------------- | :------ | :------ | :-------- | :---------- | :---------------------------------------- |
| Apartamento    | 2       | Sim     | Não       | R$ 1.140,00 | R$ 2.000,00 (parcelado em até 5x)         |

Ao finalizar, o programa oferece a opção de gerar um arquivo `.csv` com as 12 parcelas do aluguel na pasta `/orcamentos/`.

---

### 🧱 Conceitos Aplicados

**Programação Orientada a Objetos (POO):**
-   Uso de herança com as classes `Imovel`, `Apartamento`, `Casa`, e `Estudio`.
-   Encapsulamento das regras de negócio em métodos.
-   Classe `Orcamento` responsável pelo cálculo final e geração de relatórios.

**Tratamento de Exceções (`try/except`):**
-   Evita travamentos em entradas inválidas.

**Pensamento Algorítmico:**
-   Estrutura sequencial, condicional e repetitiva.

**Boas Práticas:**
-   Estrutura de pastas organizada.
-   Testes automatizados.
-   README informativo.

---

### 📦 Entregáveis do Projeto

-   **Parte Teórica:** PDF com fluxograma e explicação da lógica do sistema.
-   **Parte Prática:** Código-fonte completo, testes e README.
-   **Vídeo Pitch:** Apresentação de até 4 minutos demonstrando o funcionamento e a estrutura do código.

---

### 🧑‍💻 Autor

**Kayque Lucas**
*Estudante de Análise e Desenvolvimento de Sistemas - 2025*
*📍 Rio de Janeiro*
*📧 Contato: kayquelucassilvaneves@gmail.com*

---

### 🏁 Versão

**v1.0 - Outubro/2025**
*Projeto finalizado e validado com testes automatizados.*