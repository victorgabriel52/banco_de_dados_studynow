import json
import sys
import os

def menu_banco():



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
                print("Saldo aqui")
            if opc == 2:
                print("trasferência aqui")
            if opc == 3:
                print("Saque aqui")
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



# def login():

#     while True:
#         cpf = input("Digite seu cpf: ").strip()
#         senha = input("Digite sua senha: ")

#         if not cpf or not senha:
#             print("\nERRO! Digite Senha e Cpf\n")
#             continue

#         try:
#             with open('usuario.json', 'r', encoding='utf-8') as arquivo:
#                 usuários = json.load(arquivo)

#                 print(f"\nBem vindo, usuário {cpf}\n")
#                 menu_banco()
#             else:
#                 print("\nSenha ou usuário incorretos!\n")
            
#         except (FileNotFoundError, FileExistsError):
#             print("ERRO! ocorreu um erro ao localizar o arquivo")

def cadastro():
    while True:
        nome = input("Digite seu nome: ")
        cpf = input("Digite um cpf para cadastro: ")
        senha = input("Digite uma senha: ")

        if not cpf or not senha:
            print("ERRO! digite um cpf ou senha!")
            continue

        novo_user = {'nome': nome, 'cpf': cpf, 'senha': senha}

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



