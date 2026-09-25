# EXERCICIO 09:

# SOLICITE A FUNÇÃO DO USUÁRIO:
func = input("Informe a função do usuário: ")

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (func == "SysAdmin"):
    print("Permissões: Acesso Total (Root / Sudoer - Nível 0).")
    
elif (func == "Dev"):
    print("Permissões: Leitura/Escrita nos Ambientes de Sandbox e Staging.")
    
elif (func == "Auditor"):
    print("Permissões: Acesso Somente-Leitura (Read-Only) em Logs de Auditoria.")
    
else:
    print("Função não reconhecida: Acesso Negado por padrão (Zero Trust).")