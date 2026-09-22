# EXERCICIO 07:

# SOLICITE SE O CERTIFICADO ESTÁ DENTRO DA VALIDADE
cert = input("O certificado está dentro da validade?(S/N): ").upper()

# SOLIICITE SE ELE É CONFIÁVEL
aut = input("A autoridade emissora é confiavél?(S/N): ").upper()

# SE "cert" e (and) "aut" FOR "S", ENTÃO:
if (cert == "S" and aut == "S"): # USEI OPERADOR LÓGICO "AND"
    print("Conexão HTTPS segura estabelecida.") # CONDIÇÃO SEJA VERDADEIRA
else:
    print("ALERTA: Conexão insegura! Risco de ataque Man-in-the-Middle.") # CONDIÇÃO SEJA FALSA