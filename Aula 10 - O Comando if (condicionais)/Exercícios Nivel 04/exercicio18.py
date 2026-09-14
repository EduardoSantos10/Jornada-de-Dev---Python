# EXERCICIO 18:

# VOCê SOLICITA O USO DA CPU
consumo = float(input("Informe o uso da CPU: "))

# VOCÊ SOLICITA SE O ALERTA ESTÁ ATIVO
alerta_ativo = input("O alerta está ativo (S/N): ").upper()

# SE O CONSUMO DA CPU FOR MENOR QUE 50.0 E HOUVER A NEGAÇÃO DO ALERTA ATIVO
# SE ELE FOR IGUAL A "S", AUTOMATICAMENTE ELE IRÁ VIRAR "N"
if (consumo < 50.0) and not (alerta_ativo == "S"):
    print("Sistema operando em estado saudável e sem alertas.")