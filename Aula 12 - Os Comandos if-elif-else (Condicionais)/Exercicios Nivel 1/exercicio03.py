# EXERCICIO 03:

# INFORME A PORCETAGEM DO USO DE MEMÓRIA RAM
mem = float(input("Informe a porcentagem de uso da memória RAM: "))

# ESTRUTURA CONDICIONAL COM IF-ELIF-ELSE
if (mem < 60.0):
    print("Uso de RAM Estável.")
    
elif (mem < 80.0):
    print("Uso de RAM Moderado: Monitorando processos.")
    
elif (mem <  95.0):
    print("ALERTA: Memória RAM em nível crítico!")
    
else: # CASO NÃO ATINJA NENHUMA DAS CONDIÇÕES ACIMA
    print("EMERGÊNCIA: Invocando OOM Killer (Out Of Memory) do Kernel Linux.")