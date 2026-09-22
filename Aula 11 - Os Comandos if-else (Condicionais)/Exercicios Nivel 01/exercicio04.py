# EXERCICIO 04:

# SOLICITE O HASH DE UM ARQUIVO
arq = input("Informe a hash MD5/SHA256 de um arquivo: ")

# SE O HASH MD5/SHA265 DESSE ARQUIVO FOR IGUAL AO HASH PEDIDO, ENTÃO:
if (arq == "e10adc3949ba59abbe56e057f20f883e"):
    print("Arquivo íntegro e verificado com sucesso.") # CONDIÇÃO VERDADEIRA
else: # SE NÃO
    print("ALERTA: Hash divergente! Arquivo corrompido ou adulterado.") # CONDIÇÃO FALSA