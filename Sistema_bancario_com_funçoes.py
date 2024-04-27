

# Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

def menu(): 
    
    menu = """===== MENU =====

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Criar Conta
[6] Listar Clientes
[7] Listar Contas
[0] Sair
=> """
    opcao = int(input(menu))
    return opcao

def depositar(saldo, valor, extrato, /):
    verificar = valor > 0
    if verificar:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.\n")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques == LIMITE_SAQUES
    excedeu_saldo = valor > saldo

    if excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número de saques diários excedido. @@@")

    elif excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.\n")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def verificar_usuario(cpf, usuarios):
    usuarios_verificados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_verificados[0] if usuarios_verificados else None
    
def cadastrar_cliente(usuarios):
    cpf = int(input("Informe o CPF (somente números): "))
    
    if len(usuarios) >= 1:
        if verificar_usuario(cpf, usuarios):
            print("CPF já cadastrado.")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})

    print("=== Usuário criado com sucesso! ===")

def listar_clientes(usuarios):
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        lista = ""
        for usuario in usuarios:
            lista += f"Nome:{usuario["nome"]}\nData de Nascimento: {usuario["data_nascimento"]}\nCPF: {usuario["cpf"]}\nEndereço: {usuario["endereco"]}\n\n"
        
        print(lista)

# Conta corrente: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

def criar_conta_corrente(agencia, usuarios, numero_conta):
    cpf = int(input("Informe o CPF (somente números): "))
    usuario_verificado = verificar_usuario(cpf, usuarios)

    if usuario_verificado:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_verificado}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        
def listar_contas(contas):
    if len(contas) == 0:
        print("Nenhuma conta criada.")
    else:
        lista = ""
        for conta in contas:
            lista += f"Agência: {conta["agencia"]}\nC/C: {conta["numero_conta"]}\nTitular: {conta["usuario"]["nome"]}\n\n"
        
        print(lista)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    extrato = ""
    limite = 500
    numeros_saques = 0
    usuarios = []
    contas = []
    
    while True:
        op = menu()

        if op == 1:
            valor = float(input("Digite a quantia do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif op == 2:
            valor = float(input("Digite a quantia do saque: "))
            saldo, extrato, numeros_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numeros_saques, LIMITE_SAQUES=LIMITE_SAQUES
                )
            
        elif op == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif op == 4:
            cadastrar_cliente(usuarios)

        elif op == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(
                agencia=AGENCIA, 
                numero_conta=numero_conta, 
                usuarios=usuarios 
            )

            if conta:
                contas.append(conta)
        
        elif op == 6:
            listar_clientes(usuarios)

        elif op == 7:
            listar_contas(contas)

        elif op == 0:
            print("Encerrando...")
            break


main()