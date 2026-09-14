# EXERCICIO 11:

# SOLICITE AO USUÁRIO O STATUS A
statusA = input("Informe o status do link A (A/F): ")

# SOLICITE AO USUÁRIO O STATUS B
statusB = input("Informe o status do link B (A/F): ")

# OBS: A = ABERTO / F = FECHADO

# SE O STATUS A OU STATUS B ESTIVER ABERTO, OU AMBOS ESTIVEREM ABERTOS, ENTÃO, IMPRIMA
if (statusA == "A") or (statusB == "A"):
    print("Rede operacional: Pelo menos um link está ativo.")