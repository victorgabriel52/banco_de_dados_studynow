from database import *

import sys

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



def login():

    criar_tabela()

    while True:
        cpf = input("Digite seu cpf: ").strip()
        senha = input("Digite sua senha: ")

        if not cpf or not senha:
            print("\nERRO! Digite Senha e Cpf\n")
            continue
        
        con = banco()
        cur = con.cursor()
        cur.execute("SELECT * FROM usuarios WHERE cpf = ? AND senha = ?", (cpf, senha))
        usuário = cur.fetchone()
        con.close()

        if usuário:
            print(f"\nBem vindo, usuário {cpf}\n")
            menu_banco()
        else:
            print("\nSenha ou usuário incorretos!\n")


def cadastro():

    criar_tabela()

    cpf = input("Digite um cpf para cadastro: ")
    senha = input("Digite uma senha: ")

    con = banco()
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO usuarios (cpf, senha) VALUES (?, ?)", (cpf, senha))
        con.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Usuário já cadastrado!")
    finally:
        con.close()
