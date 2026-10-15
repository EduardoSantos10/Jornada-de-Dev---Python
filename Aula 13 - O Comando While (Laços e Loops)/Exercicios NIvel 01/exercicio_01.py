# EXERCICIO 01: VALIDÇÃO DE SENHA DE ACESSO

# VARIÁVEIS DE CONTROLE: SOLICITAÇÃO DE SENHA
senha = input("Informe a sua senha: ")

# DECLARANDO CONSTANTE PARA VARIÁVEL CORRETA DE SENHA
SENHA_CORRETA = "admin123"

# CONTADOR PARA TENTATIVAS
tentativas_falhas = 0

# ENQUANTO senha FOR DIFERENTE DE senha_correta
while senha != SENHA_CORRETA:
    print("Senha incorreta!") # MENSAGEM PARA CASO ELE DIGITAR A SENHA INCORRETA
    tentativas_falhas += 1 # CONTADOR DE TENTATIVAS PARA ERROS
    
    senha = input("Informe a senha novamente: ") # SOLICITAÇÃO DE SENHA NOVAMENTE
    
print("A senha está correta, acesso concedido!") # MENSAGEM PARA CASO A SENHA ESTEJA CORRETA