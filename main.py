from classes_imoveis import Apartamento, Casa, Estudio, Orcamento


def main():
    print("🏠 Bem-vindo ao sistema da Imobiliária R.M")
    print("Escolha o tipo de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    try:
        escolha = int(input("Digite o número da opção: "))
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números.")
        return

    imovel = None

    try:
        if escolha == 1:
            quartos = int(input("Número de quartos (1 ou 2): "))
            garagem = input("Deseja garagem? (s/n): ").lower() == "s"
            criancas = input("Possui crianças? (s/n): ").lower() == "s"
            imovel = Apartamento(quartos=quartos, garagem=garagem, possui_criancas=criancas)

        elif escolha == 2:
            quartos = int(input("Número de quartos (1 ou 2): "))
            garagem = input("Deseja garagem? (s/n): ").lower() == "s"
            imovel = Casa(quartos=quartos, garagem=garagem)

        elif escolha == 3:
            vagas = int(input("Deseja pacote de 2 vagas? (0=Não, 2=Sim): "))
            extras = int(input("Quantas vagas extras (0 se nenhuma): "))
            imovel = Estudio(vagas=vagas, vagas_extras=extras)

        else:
            print("❌ Opção inválida!")
            return

    except ValueError:
        print("❌ Entrada inválida! Digite apenas números quando solicitado.")
        return
    except Exception as e:
        print(f"Erro ao criar imóvel: {e}")
        return

    # 🚨 Garantia: só segue se o imóvel existir
    if imovel is None:
        print("❌ Não foi possível criar o imóvel.")
        return

    try:
        orcamento = Orcamento(imovel)
        resumo = orcamento.gerar_resumo()

        print("\n📊 Orçamento Gerado:")
        print(f"Tipo de Imóvel: {resumo['Imóvel']}")
        print(f"Valor mensal: R$ {resumo['Valor mensal']:.2f}")
        print(f"Valor contrato: R$ {resumo['Valor contrato']:.2f} (parcelável em até 5x)")

        salvar = input("\nDeseja gerar arquivo CSV com 12 parcelas? (s/n): ").lower()
        if salvar == "s":
            orcamento.gerar_csv("orcamentos/orcamento.csv")

    except Exception as e:
        print(f"Erro ao processar orçamento: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro inesperado: {e}")
