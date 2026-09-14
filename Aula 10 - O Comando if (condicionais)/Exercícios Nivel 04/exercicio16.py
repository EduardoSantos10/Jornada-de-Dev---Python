# EXERCICIO 16:

# SOLICITA AO COLABORADOR SE O SERVIÇO ESTÁ ATIVO
servico_ativo = input("Este serviço está ativo (S/N): ").upper()

# UTILIZA O OPERADOR LOGICO "NOT" PARA INVERTER A CONDIÇÃO QUE NESTE MOMENTO ESTÁ VERDADEIRA
if not (servico_ativo == "S"):
    print("ATENÇÃO: Serviço inativo! Tentando reiniciar...")