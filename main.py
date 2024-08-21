menu = """
    SISTEMA BANCÁRIO
    ------------------------
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
"""

depositos = []
saques = []
LIMITE_SAQUES = 3
valor_maximo = 500
saldo = 0


def mostrar_menu():
    print(menu)


def depositar(valor):
    global saldo
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f"Depositado {valor:.2f} reais.")
    else:
        print("Valor inválido. Depósito não realizado.")


def sacar(valor):
    global saldo
    global LIMITE_SAQUES

    if valor > 0 and valor <= saldo and LIMITE_SAQUES > 0:
        saques.append(valor)
        saldo -= valor
        LIMITE_SAQUES -= 1
        print(f"Saque realizado com sucesso. Saldo atual: {saldo:.2f} reais.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif LIMITE_SAQUES == 0:
        print("Limite de saques excedido.")


def mostrar_extrato():
    print("\n========== EXTRATO ==========")
    if not depositos and not saques:
        print("Nenhuma operação realizada.")
        return

    print("DEPÓSITOS:")
    for operacao in depositos:
        print(f"+ R$ {operacao:.2f}")
    print("SAQUES:")
    for operacao in saques:
        print(f"- R$ {operacao:.2f}")
    print(f"SALDO: R$ {saldo:.2f}")


def main():
    while True:
        mostrar_menu()
        operacao = input("Digite a opção desejada: ")

        if operacao.lower() == "q":
            print("Saindo do sistema...")
            break
        elif operacao.lower() == "d":
            valor = float(input("Digite o valor do depósito: "))
            depositar(valor)
        elif operacao.lower() == "s":
            valor = float(input("Digite o valor do saque: "))
            sacar(valor)
        elif operacao.lower() == "e":
            mostrar_extrato()


if __name__ == "__main__":
    main()
