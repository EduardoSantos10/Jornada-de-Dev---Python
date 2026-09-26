# EXERCICIO 16:

# SOLICITE O TIPO DE DNS EM CONSULTA
reg = input("Informe o tipo de DNS: ").upper()

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (reg == "A"):
    print("Registro tipo A: Mapeia um hostname para um endereço IPv4.")

elif (reg == "AAAA"):
    print("Registro tipo AAAA: Mapeia um hostname para um endereço IPv6.")

elif (reg == "CNAME"):
    print("Registro CNAME: Cria um alias (apelido) direcionando para outro hostname.")
    
elif (reg == "MX"):
    print("Registro MX: Aponta para os servidores de correio eletrônico (Mail Exchange).")

elif (reg == "TXT"):
    print("Registro TXT: Armazena texto arbitrário (Usado para validações SPF/DKIM/DMARC).")

else:
    print("Tipo de registro DNS não suportado para esta consulta.")