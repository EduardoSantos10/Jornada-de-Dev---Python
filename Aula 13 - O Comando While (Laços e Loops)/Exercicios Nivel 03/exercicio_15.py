# EXERCICIO 15: SIMULADOR DE DESALOCAÇÃO DE MEMÓRIA RAM

# VARIAVEL DE OCUPAÇÃO ATUAL
servidor = 16

# ENQUANTO "SERVIDOR" FOR MAIOR OU IGUAL 4:
while servidor >= 4:
    print(f"O status atual da RAM é {servidor}") # MENSAGEM INFORMANDO A MEMÓRIA ATUAL DA RAM
    
    liberada = int(input("Informe a quantidade de RAM liberada no processo de encerramento: ")) # FINFORME A QUANTIDADE DE RAM QUE SERÁ LIBERADA NO SERVIDOR
    servidor -= liberada # REDUZA A QUANTIDADE LIBERADA PELA OCUPAÇÃO ATUAL
    
    print(f"Processo encerrado! RAM atualmente ocupada: {servidor} GB") # INFORME QUE O PROCESSO FOI CONCLUÍDO E A QUANTIDADE ATUAL DE MEMÓRIA
    
print("A memória do servidor foi estabilizada  com sucesso a um nível operacional seguro!") # INFORME QUE O SERVIDOR ESTÁ OPERANDO NORMALMENTE