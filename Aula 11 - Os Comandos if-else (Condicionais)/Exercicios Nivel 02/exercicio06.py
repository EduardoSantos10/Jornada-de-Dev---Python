# EXERCICIO 06:

# SOLICITE O USER
user = input("Informe seu user: ")

# SOLICITE A SENHA
senha = input("Informe sua senha: ")

# SE USER FOR IGUAL A "admin" E SENHA FOR IGUAL A "Linux123", ENTÃO:
if (user == "admin" and senha == "Linux123"): # UTILIZEI UM OPERADOR LÓGICO "AND"
    print("Autenticação bem-sucedida! Sessão interativa iniciada.") # CONDIÇÃO VERDADEIRA
else:
    print("Falha na autenticação: Usuário ou senha incorretos.") # CONDIÇÃO FALSA