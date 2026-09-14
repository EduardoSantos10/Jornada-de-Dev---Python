# EXERCICIO 15:
 # INFORME UM DIA DA SEMANA
dia = input("Informe o dia da semana: ").lower()

# VALIDANDO A ENTRADA DO FERIADO, MESMO SENDO BOOLEANA
# HOJE É FERIADO
diaF = input("Hoje é feriado(S/N): ").upper()

# SE DIA DA SEMANA FOR IGUAL A "SABADO" OU "DOMINGO" OU DIA DA SEMANA FOR FERIADO IGUAL A S.
# ENTÃO, IMPRIMA
if (dia == "sabado" or dia == "domingo") or (diaF == "S"):
    print("Redirecionando chamados para a equipe de plantão On-Call.")