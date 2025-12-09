#Função para depositar dinheiro
def depositar_conta(numero_conta, valor):
    global saldo
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            if valor <= 0:
                print("Valor inválido!")
                return
            conta["saldo"] += valor
            conta["historico"].append(f"Depósito de R${valor:.2f}")
            print('\n' +'='*45)
            print(f"Depósito de R${valor:.2f} realizado na conta {numero_conta}.")
            print(f"Saldo atual: R${conta['saldo']:.2f}")
            print('='*45 + '\n')
            return
    print()
    print('----------ERRO----------')
    print("   Conta não encontrada!")
    print('----------ERRO----------')
    print()

# Função para sacar dinheiro
def sacar_conta(numero_conta, valor):
    global saldo
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            if conta["numero_saques"] >= 3:
                print("Limite máximo de 3 saques atingido!")
                return

            if valor <= 0:
                print("Valor inválido!")
                return
            if valor <= 0:
                print("Valor inválido!")
                return
            if valor > conta["saldo"]:
                print("Saldo insuficiente!")
                return
            conta["saldo"] -= valor
            conta["historico"].append(f"Saque de R${valor:.2f}")
            conta["numero_saques"] += 1
            print("\n==============================================")
            print(f"Saque de R${valor:.2f} realizado na conta {numero_conta}.")
            print(f"Saldo atual: R${conta['saldo']:.2f}")
            print("==============================================\n")
            return
    print("Conta não encontrada!")

# Função para visualizar histórico de operações
def visualizar_historico(historico):
    print("Histórico de operações:")
    for operacao in historico:
        print(operacao)

# Função para criar usuário sem permitir CPF duplicado
def criar_usuario(nome,data_nascimento, cpf, endereco):
    # Verifica se já existe um usuário com esse CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print()
            print('--------ERRO--------')
            print(" CPF já cadastrado!")
            print('--------ERRO--------')
            print()
            return None

    # Cria usuário
    usuario = {
        "nome": nome,
        "data de nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "numero_saques" : numero_saques
    }
    usuarios.append(usuario)
    print('\n' + '='*40)
    print(f"Usuário {nome} criado com sucesso.")
    print('=' * 40 + '\n')
    return usuario

# Capturar endereço com validações de entrada
def capturar_endereco():
    print("\n--- Cadastro de Endereço ---")
    while True:
        logradouro = input("Logradouro: ")
        if all(palavra.isalpha() for palavra in logradouro.split()):
         break
        else:
            print("Entrada inválida! Digite somente letras.\n")

    while True:
        numero = input("Número: ")
        if numero.isdigit():  # Verifica se todos os caracteres são dígitos
            break
        else:
            print("Entrada inválida! Digite somente números.\n")

    while True:
        bairro = input("Bairro: ")
        if all(palavra.isalpha() for palavra in bairro.split()):
         break
        else:
            print("Entrada inválida! Digite somente letras.\n")

    while True:
        cidade = input("Cidade: ")
        if all(palavra.isalpha() for palavra in cidade.split()):
         break
        else:
            print("Entrada inválida! Digite somente letras.\n")

    while True:
        estado = input("Estado (sigla): ")
        if all(palavra.isalpha() for palavra in estado.split()):
            break
        else:
            print("Entrada inválida! Digite somente letras.\n")

    # Formatação do endereço
    endereco_formatado = (
        f"{logradouro}, nº {numero}, {bairro}, {cidade}/{estado}"
    )
    #print(endereco_formatado)
    return endereco_formatado


def criar_conta(cpf, agencia_numero="0001"):
    # Verificar se o usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print()
        print('-'*24, "ERRO", '-'*24)
        print(" Usuário não encontrado. Cadastre o usuário primeiro!")
        print('-'*24, "ERRO", '-'*24)
        return None

    # Número da conta = quantidade de contas + 1
    numero_conta = len(contas) + 1

    conta = {
        "agencia": agencia_numero,
        "numero_conta": numero_conta,
        "cpf": cpf,
        "saldo": 0,
        "historico": [],
        "numero_saques":0
    }

    contas.append(conta)
    print('\n' + '='*30)
    print(f"Conta criada com sucesso!")
    print(f"Agência: {agencia_numero}")
    print(f"Número da Conta: {numero_conta}")
    print(f"Titular: {usuario_encontrado['nome']}\n")
    print('=' * 30 + '\n')
    return conta
def visualizar_extrato(numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            print("\n========== EXTRATO ==========")
            print(f"========== Conta {numero_conta} ==========")
            if not conta["historico"]:
                print("Nenhuma movimentação.")
            else:
                for operacao in conta["historico"]:
                    print(operacao)
            print(f"Saldo atual: R${conta['saldo']:.2f}")
            print("=============================\n")
            return

    print()
    print("-" * 9, "ERRO", "-" * 9)
    print("Conta não encontrada!")
    print("-" * 9, "ERRO", "-" * 9)
    print()

def listar_contas_do_usuario(cpf):
    print(f"\n--- Contas do CPF {cpf} ---")
    encontrou = False

    for conta in contas:
        if conta["cpf"] == cpf:
            encontrou = True
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Saldo: R${conta['saldo']:.2f}")

    if not encontrou:
        print('='*43)
        print("Nenhuma conta encontrada para este usuário.")
        print('='*43)




menu = """
[a] Criar conta bancária
[l] Listar contas do usuário
[c] Criar Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# Lista para armazenar
usuarios = []
historico = []
agencias = [{"numero": "0001"}]  # agência padrão do banco
contas = []

global numero_saques
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "a":
        while True:
            cpf = input("Digite o CPF do usuário para criar a conta: ")
            if cpf.isdigit():
                break
            else:
                print("Entrada inválida! Digite somente números.\n")
        criar_conta(cpf)

    elif opcao == "l":
        cpf = input("Digite o CPF para listar as contas: ")
        listar_contas_do_usuario(cpf)

    elif opcao == "c":
        #Validar entrada apenas com letras
        while True:
            nome = input("Digite o nome do usuário: ")
            if all(palavra.isalpha() for palavra in nome.split()):
                break
            else:
                print("Entrada inválida! Digite somente letras.\n")

        # Validar entrada apenas com numeros
        while True:
            cpf = input("Digite o CPF: ")
            if cpf.isdigit():
                break
            else:
                print("Entrada inválida! Digite somente números.\n")

        # Validar entrada apenas com numeros
        while True:
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            if data_nascimento.isdigit():  # Verifica se todos os caracteres dígitos
                break
            else:
                print("Entrada inválida! Digite somente números.\n")

        # Captura e formata o endereço
        endereco = capturar_endereco()

        # Cria o usuário
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "d":

        # Validar entrada apenas com numeros
        while True:
            try:
                numero = int(input("Digite o número da conta para depósito: "))
                break
            except ValueError:
                print("Entrada inválida! Digite somente números.\n")


        while True:
            try:
                valor = int(input("Digite o valor do depósito: "))
                break
            except ValueError:
                print("Entrada inválida! Digite somente números.\n")
        depositar_conta(numero, valor)

    elif opcao == "s":
        while True:
            try:
                numero = int(input("Digite o número da conta para saque: "))
                break
            except ValueError:
                print("Entrada inválida! Digite somente números.\n")

        while True:
            try:
                valor = int(input("Digite o valor do saque: "))
                break
            except ValueError:
                print("Entrada inválida! Digite somente números.\n")
        sacar_conta(numero, valor)

    elif opcao == "e":
        while True:
            try:
                numero = int(input("Digite o número da conta para extrato: "))
                break
            except ValueError:
                print("Entrada inválida! Digite somente números.\n")
        visualizar_extrato(numero)

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
