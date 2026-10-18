# EXERCICIO 09: VERIFICAÇÃO DE ESPAÇO EM DISCO (DISK CLEANUP)

# SOLICITE A OCUPAÇÃO ATUAL DO DISCO
ocupacao = int(input("Informe a ocupação atual do disco de 500GB: "))

# ENQUANTO "OCUPAÇÃO" FOR MAIOR QUE 400GB:
while ocupacao > 400:
    print(f"Espaço do disco está acima do limite, com {ocupacao}GB") # INFORME QUE O DISCO ESTÁ ACIMA DO LIMITE, COM  QUANTIDADE OCUPADA
    tamanho_del = int(input("Informe o tamanho do arquivo que quer deletar: ")) # SOLICITE A QUANTIDADE QUE DESEJA DELETAR
    
    ocupacao -= tamanho_del # SUBTRAIA OCUPAÇÃO ATUAL POR TAMANHO DELETADO
    print(f"A quantidade de arquivo deletado foi de: {tamanho_del} GB, portanto a sua nova ocupação é de: {ocupacao}") # INFORME A QUANTIDADE QUE FOI DELETADO COM A NOVA OCUPAÇÃO
    
print(f"O disco atingiu {ocupacao} GB, e seu espaço está saudável para uso!") # INFORME A OCUPAÇÃO ATUAL COM A SUA NOVA CAPACIDADE