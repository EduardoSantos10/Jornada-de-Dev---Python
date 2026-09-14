# EXERCICIO 12:

# SOLICITE O NOME AO USUÁRIO
nome = input("Informe o nome do usuário: ")

# SOLICITE O ID AO USUÁRIO
id = int(input("Informe o GID do usuário: "))

# SE O NOME DO USUÁRIO, FOR IGUAL A "ROOT" OU ID FOR IGUAL A 0, ENTÃO, IMPRIMA:
if(nome == "root") or (id == 0):
    print("Acesso total ao sistema operacional concedido.")