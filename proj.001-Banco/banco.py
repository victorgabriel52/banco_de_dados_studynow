import json
import sys
import os

def carregar_usuário():
    with open('usuario.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def salvar_usuario(dados):
    with open('usuario.json', 'w', encoding='utf-8')as arquivo:
        json.dump(dados, arquivo, indent=4)

def saque(usuario, usuarios):

    saldo = usuario['saldo']

    valor = input("\nValor do saque: ")
    if valor.isnumeric():
        valor = int(valor)
        if valor <= saldo:
            saldo -= valor
            usuario['saldo'] = saldo
            salvar_usuario(usuarios)
            print(f"O saque de R${valor:.2f} foi efetuado com sucesso!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Digite um valor válido")


def menu_banco(cpf_logado):

    usuarios = carregar_usuário()
    usuario = next((u for u in usuarios if u["cpf"] == cpf_logado), None)

    if not usuario:
        print("Não existe esse usuário!")
        return

    saldo = usuario['saldo']

    while True:
        print("-="*15)
        print(f"{'BEM VINDO DE VOLTA':^30}")
        print("-="*15)
        
        print("1) ver saldo") 
        print("2) transferência") 
        print("3) saque") 
        print("4) Depositar") 
        print("5) estrato") 
        print("6) sair") #
        opc = input("Escolha: \n")

        if opc.isnumeric():
            opc = int(opc)
            if opc == 1:
                print(f"\nSaldo atual: {saldo:.2f}\n")
            if opc == 2:
                print("trasferência aqui")
            if opc == 3:
                saque(usuario, usuarios)
            if opc == 4:
                print("Deposito aqui")
            if opc == 5:
                print("Estrato aqui")
            if opc == 6:
                print("Volte sempre!!")
                print("SAINDO...")
                sys.exit()
        else:
            print(F"A opção {opc} não existe")



def login():
    while True:
        cpf = input("Digite um cpf para logar: ").strip()
        senha = input("Digite uma senha: ")

        if not cpf or not senha:
            print("ERRO! digite um cpf ou uma senha")
            continue
        
        if os.path.exists("usuario.json"):
            with open("usuario.json", 'r', encoding="utf8") as arquivo:
                try:
                    usuarios = json.load(arquivo)
                except json.JSONDecodeError:
                    print("Erro ao ler arquivo json")
                    return
            for usuario in usuarios:
                if usuario['cpf'] == cpf and usuario['senha'] == senha:
                    print(f"\nBem vindo de volta {usuario['nome']}\n")
                    menu_banco(cpf)
                
            print("Usuário ou senha incorretos!")

        else:
            print("Nenhum usuário cadastrado ainda!")
            return


def cadastro():
    while True:
        nome = input("Digite seu nome: ").strip()
        cpf = input("Digite um cpf para cadastro: ").strip()
        senha = input("Digite uma senha: ")

        if not cpf or not senha:
            print("ERRO! digite um cpf ou senha!")
            continue

        novo_user = {'nome': nome, 'cpf': cpf, 'senha': senha, 'saldo': 0.00}

        if os.path.exists("usuario.json"):
            with open("usuario.json", 'r', encoding="utf-8") as arquivo:
                try:
                    usuários = json.load(arquivo)
                except json.JSONDecodeError:
                    usuários =[]
        else:
            usuários = []
        
        usuários.append(novo_user)
        
        with open("usuario.json", 'w', encoding='utf-8') as arquivo:
            json.dump(usuários, arquivo, ensure_ascii=False, indent=4)
        
        print(f"Usuário {nome} cadastrado com sucesso")
        break



