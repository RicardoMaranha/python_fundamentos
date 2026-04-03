from models.user_model import Cliente, PessoaFisica, ContaCorrente, Deposito, Saque

def menu():
    return """
    ================ MENU ================
    [1] Novo Cliente
    [2] Nova Conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Sair
    ======================================
    => """

def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "1":
            criar_cliente(clientes)
        elif opcao == "2":
            criar_conta(clientes, contas)
        elif opcao == "3":
            depositar(clientes)
        elif opcao == "4":
            sacar(clientes)
        elif opcao == "5":
            exibir_extrato(clientes)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def criar_conta(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    numero_conta = input("Informe o número da conta: ")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("Conta criada com sucesso!")

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Cliente não possui conta!")
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Cliente não possui conta!")
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Cliente não possui conta!")
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        return None
    # Retorna a primeira conta, assumindo que cada cliente tem uma conta
    return cliente.contas[0]

if __name__ == "__main__":
    main()





