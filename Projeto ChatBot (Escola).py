
print("===================================")
print("  BEM-VINDO À PIZZARIA SABOR REAL!")
print("===================================")

print("\nOlá! Seja bem-vindo ao nosso atendimento.")
print("Sou o assistente virtual da pizzaria.")

nome = input("\nQual é o seu nome? ")

print("\nPrazer em atender você,", nome + "!")

print("\n========== MENU PRINCIPAL ==========")
print("1 - Ver cardápio")
print("2 - Fazer um pedido")
print("3 - Consultar horário de funcionamento")
print("4 - Sair")

opcao = input("\nDigite o número da opção desejada: ")

if opcao == "1":
    print("\n========== CARDÁPIO ==========")
    print("1 - Pizza de Calabresa - R$ 35")
    print("2 - Pizza de Mussarela - R$ 32")
    print("3 - Pizza de Frango - R$ 38")
    print("4 - Pizza Portuguesa - R$ 42")

    print("\nObrigado por consultar nosso cardápio!")

elif opcao == "2":
    print("\n========== FAZER PEDIDO ==========")
    print("1 - Calabresa - R$ 35")
    print("2 - Mussarela - R$ 32")
    print("3 - Frango - R$ 38")
    print("4 - Portuguesa - R$ 42")

    pizza = input("\nEscolha sua pizza (1, 2, 3 ou 4): ")

    if pizza == "1":
        sabor = "Calabresa"
        preco = 35
    elif pizza == "2":
        sabor = "Mussarela"
        preco = 32
    elif pizza == "3":
        sabor = "Frango"
        preco = 38
    elif pizza == "4":
        sabor = "Portuguesa"
        preco = 42
    else:
        sabor = ""
        preco = 0

    if preco > 0:
        endereco = input("\nDigite seu endereço de entrega: ")

        quantidade = int(input("Quantas pizzas deseja? "))

        total = preco * quantidade

        print("\n========== RESUMO DO PEDIDO ==========")
        print("Cliente:", nome)
        print("Sabor:", sabor)
        print("Quantidade:", quantidade)
        print("Endereço:", endereco)
        print("Valor total: R$", total)

        print("\nSeu pedido foi registrado com sucesso!")
        print("Agradecemos pela preferência!")
    else:
        print("\nOpção inválida! Não foi possível realizar o pedido.")

elif opcao == "3":
    print("\nNosso horário de funcionamento é:")
    print("De segunda a sábado, das 18h às 23h.")
    print("Aos domingos, das 18h às 22h.")

elif opcao == "4":
    print("\nVocê escolheu sair do atendimento.")

else:
    print("\nOpção inválida! Por favor, tente novamente.")

print("\n===================================")
print("Obrigado por entrar em contato!")
print("A Pizzaria Sabor Real agradece!")
print("Tenha um ótimo dia! Até a próxima!")
print("===================================")
