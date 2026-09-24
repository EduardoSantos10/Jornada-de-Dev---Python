# EXERCICIO 04:

# SOLICITE A QUANTIDADE DE IOPS
quant = int(input("Informe a quantidade de IOPS: "))

# ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (quant <= 300):
    print("Tecnologia: HD Mecânico (HDD SATA/SAS).")
    
elif (quant <= 10000):
    print("Tecnologia: SSD SATA / SSD SAS.")
    
elif (quant <= 500000):
    print("Tecnologia: NVMe SSD PCIe.")
    
else: # CASO NENHUMA DESSAS CONDIÇÕES SEJAM ATENDIDAS
    print("Tecnologia: Array de Armazenamento Enterprise (Storage SAN / NVMe-oF).")