# EXERCICIO 17:

# SOLICITA O GRUPO DO USUÁRIO
grup = input("Informe o grupo do usuário: ")

# SOLICITA SE ELE É DONO DO ARQUIVO
resp = input("Você é dono do arquivo (S/N): ").upper()

# SOLICITA SE ELE TEM PERMISSÕES GLOBAIS
perm = input("Este arquivo tem permissão de escrita global (S/N): ").upper()

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (grup == "root"):
    print("Acesso de Escrita Concedido: Superusuário do Sistema.")
    
elif (perm == "S"):
    print("Acesso de Escrita Concedido: Proprietário com permissões seguras.")
    
elif (resp == "S"):
    print("ALERTA DE SEGURANÇA: Arquivo World-Writable! Escrita negada até correção via chmod.")
    
else:
    print("Acesso de Escrita Negado: Princípio do Menor Privilégio Aplicado.")