# EXERCICIO 11: SCANNER DE PORTAS DE REDE (PORT RANGE CHECKER)

# SOLICITE AO COLABORADOR A PORTA INICIAL DA VARREDURA
porta_inicial = int(input("Informe a porta inicial do intervalo: "))

# SOLIICITE AO COLABORADOR A PORTA FINAL DA VARREDURA
porta_final = int(input("Informe a porta final do intervalo: "))

# VARIAVÉL DE CONTROLE: A PORTA QUE ESTÁ SENDO VERIFICADA NO MOMENTO
porta_atual = porta_inicial

# ENQUANTO "PORTA_ATUAL" FOR MENOR OU IGUAL A "PORTA_FINAL"
while porta_atual <= porta_final:
    print(f"Testando conectividade da porta {porta_atual}") # MENSAGEM INFORMANDO QUE ESTÁ TESTANDO A PORTA ATUAL
    porta_atual += 1 # INCREMENTANDO A SEQUÊNCIA DE PORTA QUE ESTÁ SENDO VERIFICADA
    
print(f"Varredura solicitada da {porta_inicial} a {porta_final}, foi concluída com sucesso!") # MENSAGEM QUE A VARREDURA DAS PORTAS FORAM CONCLUÍDAS COM SUCESSOsssss