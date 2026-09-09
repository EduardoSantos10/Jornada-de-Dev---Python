# EXERCICIO 07:

# SOLICITE AO USUARIO 5 NUMEROS PARA ARMAZENAR NAS VARIAVEIS
V1 = int(input("Informe um número: "))
V2 = int(input("Informe um número: "))
V3 = int(input("Informe um número: "))
V4 = int(input("Informe um número: "))
V5 = int(input("Informe um número: "))

# GUARDE OS NUMEROS DIGITADOS DENTRO DE UMA LISTA
lista = [V1, V2, V3, V4, V5]

# DENTRO DESSA NOVA LISTA, USE A FUNÇÃO "SORTED()" PARA VERIFICAR A ORDEM
# DESSA LISTA E CLASSIFICAR OS NUMEROS DO MENOR PARA O MENOR AO MAIOR
nova_lista = sorted(lista)

# IMPRIMA ESSES NUMEROS EM ORDEM, JUNTO DO ENUNCIADO
print("A ordem crescente desta lista é ", nova_lista)