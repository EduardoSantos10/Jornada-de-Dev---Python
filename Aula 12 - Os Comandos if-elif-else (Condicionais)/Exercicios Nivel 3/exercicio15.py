# EXERCICIO 15:

# SOLICITE O TIPO DE BACKUP:
backup = input("Informe o tipo de backup solicitado: ").upper()

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (backup == "FULL"):
    print("Backup Completo: Copiando 100% dos blocos de dados do Storage.")
    
elif (backup == "INC"):
    print("Backup Incremental: Copiando apenas blocos alterados desde o último backup.")
    
elif (backup == "DIFF"):
    print("Backup Diferencial: Copiando blocos alterados desde o último Backup Full.")
    
else:
    print("Tipo de backup inválido: Seleção cancelada por segurança.")