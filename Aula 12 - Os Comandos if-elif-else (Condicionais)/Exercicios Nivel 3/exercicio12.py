# EXERCICIO 12:

# SOLICITE O CODIGO DE SAIDA
cod = int(input("Informe o codigo de saida: "))

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (cod == 0):
    print("Exit Code 0: Etapa concluída com sucesso (Success).")
    
elif (cod == 1):
    print("Exit Code 1: Erro geral no script ou falha de teste unitário.")
    
elif (cod == 127):
    print("Exit Code 127: Comando ou binário não encontrado no PATH da imagem.")
    
elif (cod == 137):
    print("Exit Code 137: Processo abortado pelo OOM Killer (Container Out Of Memory).")
    
else:
    print("Exit Code Desconhecido: Falha não tratada na execução do Runner.")