# PROJETO 04: VALIDADOR AVANÇADO DE COMPLEXIDADE DE SENHAS COM RETRY LOGIC

# BLOCO 01:
# Solicita ao usuário a entrada inicial da senha que passará pelo baseline de segurança.
senha = input("Informe uma nova senha de acesso: ")

# BLOCO 02:
# Estabelece os parâmetros corporativos obrigatórios para conformidade de credenciais.
TAMANHO_MINIMO = 8
cont = 0 # CONTADOR DE TENTATIVAS DE DIGITAR A SENHA

# Escaneamento inicial das regras de complexidade alfabética utilizando iteradores any()
tem_maiuscula = any(c.isupper() for c in senha) # Verifica se tem letras maiusculas na senha
tem_minuscula = any(c.islower() for c in senha) # Verifica se tem letras minusculas na senha


# BLOCO 03:
# Mantém o usuário preso no laço enquanto a senha violar QUALQUER política de segurança.
# Utiliza a lógica de negação (Leis De Morgan) para avaliar falhas de tamanho ou caixa.
while len(senha) < TAMANHO_MINIMO or (not tem_minuscula or not tem_maiuscula):
    # Captura uma nova tentativa e atualiza a variável de estado principal
    senha_verif = input("Informe a sua senha novamente: ")
    senha = senha_verif
    cont += 1 # Incrementa a tentativa a cada ciclo rejeitado
    
    # Recalcula o escaneamento booleano para a nova string submetida
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)

    # Motor de Feedback Preditivo (Direciona o usuário sobre quais critérios faltaram)
    if tem_maiuscula == True:
        print("Esta conforme, tem letras maiusculas!")
    else:
        print("Não está conforme, precisa de uma letra maiúscula... Tente novamente!")
        
    if tem_minuscula == True:
        print("Está conforme, tem letras minusculas!")
    else:
        print("Não está conforme, precisa de letras minusculas... Tente novamente!")
        

# BLOCO 04:
# Atingido apenas quando 100% das regras de conformidade são validadas simultaneamente.
print(f"Cadastro de senha bem sucedido, com um total de {cont} tentativas")