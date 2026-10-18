# EXERCICIO 07: ACUMULADOR DE TRANSFERÊNCIA DE DADOS (DOWNLOAD PROGRESS)

# VARIAVEL INICIALIZADA
baixado = 0

# ENQUANTO BAIXADO FOR MENOR QUE 100
while baixado < 100:
    MB = int(input("Quantos MegaBytes Foram Baixados no Último Segundo: ")) # SOLICITE A QUANTIDADE DE MB BAIXADOS
    
    baixado += MB # ACUMULANDO OS MB BAIXADOS
    
    print(f"Progresso Atual: {baixado}MB / 100MB") # MOSTRANDO O PROGRESSO ATUAL
    
print("Download Concluído com Sucesso") # MENSAGEM DE "DOWNLOAD CONCLUÍDO COM SUCESSO"
