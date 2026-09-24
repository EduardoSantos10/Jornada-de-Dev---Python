# EXEMPLO 01:

# SOLIICITE UM NÚMERO ENTRE 1 E 7:
dia = int(input("Informe um número entre 1 e 7: "))

# CASO NÚMERO 1 SEJA INFORMADO
if (dia == 1):
    print("Domingo!")

elif (dia == 2):
    print("Segunda-Feira")

elif (dia == 3):
    print("Terça-Feira")
    
elif (dia == 4):
    print("Quarta-Feira")
    
elif (dia == 5):
    print("Quinta-Feira")
    
elif (dia == 6):
    print("Sexta-Feira")
    
elif(dia == 7):
    print("Sábado!")
    
# CASO UM NÚMERO FORA DO INTERVALE ENTRE 1 E 7 SEJA INFORMADO:
else:
    print("Número inválido!")