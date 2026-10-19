# EXERCICIO 13: SISTEMA DE VOTAÇÃO/CLASSIFICAÇÃO DE SATISFAÇÃO CSAT

# SOLICITE AO USUÁRIO A NOTA DE SATISFAÇÃO DO ATENDIMENTO
nota = int(input("Informe a nota de satisfação do atendimento: "))

# ENQUANTO "NOTA" FOR MENOR QUE 1 "OU" "NOTA" FOR MAIOR QUE 5:
while nota < 1 or nota > 5:
    print("ERRO! Digite um valor entre 1 e 5!") # CASO SEJA FORA DO INTERVALO DE 1 E 5, IMPRIME UMA MENSAGEM DE ERRO
    
    nota = int(input("Informe novamente um valor entre 1 e 5: ")) # SOLICITE A NOTA NOVAMENTE
    
print("A sua nota foi computada com sucesso pelo Sistema CSAT do Service Desk!") # CASO SEJA DENTRO DO INTERVALO, EXIBA A MENSAGEM DE OK, E QUE O CHAMADO FOI COMPUTADO!