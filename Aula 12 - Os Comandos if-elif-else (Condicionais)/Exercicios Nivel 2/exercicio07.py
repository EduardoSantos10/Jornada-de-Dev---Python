# EXERCICIO 07:

# SOLICITE O PRIMEIRO OCTETO DO IP
end = int(input("Informe o primeiro octeto do IP: "))

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (end >= 1 and end <= 126):
    print("Endereço Classe A (Redes Grandes).")
    
elif (end >= 128 and end <= 191): # USO DO OPERADOR LÓGICO "AND"
    print("Endereço Classe B (Redes Médias).")
    
elif (end >= 192 and end <= 223):
    print("Endereço Classe C (Redes Pequenas / LANs).")
    
elif (end >= 224 and end <= 239):
    print("Endereço Classe D (Reservado para Multicast).")
    
else:
    print("Endereço Loopback (127.x.x.x) ou Classe E (Reservado/Experimental).")