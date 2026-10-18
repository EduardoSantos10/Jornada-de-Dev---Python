# EXERCICIO 08: PROCESSAMENTO DA FILA DE CHAMADOS N1

# SOLICITA O NÚMERO DE CHAMADOS PENDENTES
chamados_p = int(input("Qual a quantidade inicial de chamados pendentes: "))

# ENQUANTO "CHAMADOS_P" FOR MAIOR QUE ZERO:
while chamados_p > 0:
    
    # INICIA O DECREMENTO: CHAMADOS_P -= 1
    chamados_p -= 1
    print(f"Um chamado foi atendido, ainda restam: {chamados_p}") # MENSAGEM SOBRE CONCLUSÃO DO ATENDIMENTO E QUANTOS RESTAM
    
print("Todos os chamado da fila foram conluídos!") # MENSAGEM DE CONCLUSÃO FINAL