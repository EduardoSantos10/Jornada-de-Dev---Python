# EXERCICIO 06:

# SOLICITE O NÚMERO DA PORTA
porta = int(input("Informe o número da porta: "))

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (porta == 22):
    print("Serviço: SSH (Secure Shell) - Acesso Remoto Seguro.")
    
elif (porta == 80 or porta == 443): # COM USO DO OPERADOR LÓGICO "OR"
    print("Serviço: Web Server (HTTP / HTTPS).")
    
elif (porta == 53):
    print("Serviço: DNS (Domain Name System) - Resolução de Nomes.")
    
elif (porta == 3306 or  porta == 5432):
    print("Serviço: Banco de Dados Relacional (MySQL / PostgreSQL).")
    
else:
    print("Porta não catalogada nas regras padrão de infraestrutura.")