# EXEMPLO 01:

# IMPORTANDO UMA BIBLIOTECA / FUNÇÕES
import math
import os

# DECLAREI A VARIAVEL X COM O VALOR 16
x = 16

raiz_quadrad = math.sqrt(x) # SQRT = FUNÇÃO PARA OBTER A RAIZ QUADRADA DE UM NÚMERO

# IMPRIMINDO A RAIZ QUADRADA
print("A raiz quadrada de ", x, "é igual a ", raiz_quadrad)

angulo = 45

# FUNÇÃO PARA CALCULAR O SENO DE UM ANGULO
seno = math.sin(angulo)

print("O seno de ", angulo, "é igual a ", seno)


####################################################################################

# BIBLIOTECA OS = AJUDA A INVOCAR FUNCIONALIDADES DO SISTEMA OPERACIONAL (WINDOWS, LINUX, MACOS)

# VOU CHAMAR O DIRETORIO CORRENTE (ONDE ESTÁ OS MEUS CÓDIGOS)
diretorio = os.getcwd()

print("O diretório corrente é", diretorio)

# PERMITE QUE EU EMITA COMANDOS DO MEU TERMINAL DE TEXTO
# os.system("clear") # "CLEAR" = COMANDO PARA LIMPAR O TERMINAL

# DECLAREI UMA LISTA
lista = [10, 20, 30]

# ESTOU CHAMANDO A FUNÇÃO "LEN" = QUE EMITE O TAMANHO DESTA LISTA
tam = len(lista)

# IMPRIMINDO O TAMANHO DESTA LISTA
print("O tamanho da minha lista é", tam)

# FUNÇÃO "SUM" = ELA SOMA TODOS OS ELEMENTOS RETORNA NA TELA
soma = sum(lista)

# IMPRIMINDO A SOMA DA LISTA
print("A soma dos elemenos da lista é", soma)