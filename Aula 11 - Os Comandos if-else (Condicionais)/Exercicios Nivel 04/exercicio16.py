# EXERCICIO 16: NEGAÇÃO E LÓGICO COMPOSTA

# SOLICITE AO COLABORADOR SE O DOCKER ESTÁ EM EXECUÇÃO
docker = input("O serviço Docker está em execução(S/N): ").upper()

# SE O DOCKER FOR IGUAL A "S", A CONDIÇÃO SE TORNA FALSA
if not (docker == "S"): # OPERADOR NOT, INVERTE A  CONDIÇÃO
    print("Executando comando: systemctl restart docker") # CONDIÇÃO VERDADEIRA, VIRA FALSA
else:# SENÃO
    print("Serviço Docker rodando normalmente.") # CONDIÇÃO FALSA, SE TORNA VERDADEIRA