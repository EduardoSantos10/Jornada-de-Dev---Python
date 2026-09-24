# EXERCICIO 01:

# SOLICITA UM NUMERO DE FAIXA AO COLABORADOR
status = int(input("Informe o código de status HTTP: "))

# PARA VERIFICAR SE O NUMERO ESTÁ ENTRE O INTERVALO DE DETERMINADA FAIXA
if (status >= 200 and status <= 299):
    print("Categoria 2xx: Sucesso na requisição.")

elif (status >= 300 and status <= 399):
    print("Categoria 3xx: Redirecionamento.")
    
elif (status >= 400 and status <= 499):
    print("Categoria 4xx: Erro do Cliente (Client Error).")
    
elif (status >= 500 and status <= 599):
    print("Categoria 5xx: Erro do Servidor (Server Error).")
    
else:
    # CASO DIGITE UM NUMERO FORA DESTES INTERVALOS
    print("Código de Status HTTP não reconhecido.")
    
# OUTRA MANEIRA DE VERIFICAÇÃO

"""
if 200 <= status <= 299:
    print("Categoria 2xx: Sucesso na requisição.")
elif 300 <= status <= 399:
    print("Categoria 3xx: Redirecionamento.")
"""
