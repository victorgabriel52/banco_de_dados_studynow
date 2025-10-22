from banco import login, cadastro

while True:
    print("-="*15)
    print(f"{'ÁREA DE LOGIN':^30}")
    print("-="*15)
    
    print("1) Entrar")
    print("2) Cadastra-se")
    print("3) sair")
    opc = input("Escolha: \n")

    if opc.isnumeric():
        opc = int(opc)
        
        if opc == 1:
            login()
        elif opc == 2:
            cadastro()
        elif opc == 3:
            break
        else:
            print("ERRO! digite uma opção válida\n")
    else:
        print("ERRO! digite um número válido")
    