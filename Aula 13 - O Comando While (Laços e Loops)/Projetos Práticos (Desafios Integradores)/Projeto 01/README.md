# 📡 Monitor de Pacotes Perdidos em Rede (Ping Sweep CLI)

> **Módulo:** Automação de Infraestrutura & Telemetria de Redes  
> **Linguagem:** Python 3.x  
> **Conceitos:** Observabilidade, Análise de SLA, Protocolo ICMP, Arquitetura em 4 Blocos.

---

## 📌 Visão Geral do Projeto

Este projeto consiste em uma ferramenta de linha de comando (CLI) projetada para simular a medição de qualidade e estabilidade de conexões de rede em ativos de TI (IPs, Gateways e Servidores). 

A aplicação utiliza uma **Arquitetura Lógica de 4 Blocos** para coletar amostras estatísticas de tráfego, calcular a taxa de perda de pacotes (*Packet Loss %*) e classificar a saúde da infraestrutura com base em níveis de serviço de rede (*Service Level Agreement - SLA*).

---

## 🏛️ Arquitetura do Sistema (4 Blocos)

O script foi estruturado seguindo o modelo de separação de responsabilidades em 4 estágios:

| Bloco | Função | Descrição |
| :--- | :--- | :--- |
| **Bloco 01** | `Inputs / Telemetria` | Captura o IP de destino e o volume total da amostragem de testes. |
| **Bloco 02** | `Gestão de Estado` | Inicializa os acumuladores e contadores de memória do agente. |
| **Bloco 03** | `Engine (Event Loop)` | Executa a varredura contínua (`while`) simulando a recepção de sinal do ICMP. |
| **Bloco 04** | `Processamento & SLA` | Processa a fórmula estatística de perda de carga e gera o painel de alerta do NOC. |

---

## 📐 Regra de Negócio & Matriz de SLA

A métrica de estabilidade de rede é calculada através da equação:

$$\text{Packet Loss (\%)} = \left( \frac{\text{Pacotes Perdidos}}{\text{Total de Pacotes Enviados}} \right) \times 100$$

### Classificação Operacional do Link:

* 🟢 **0% de Perda:** **EXCELENTE** — Link estável sem ruído ou degradação.
* 🟡 **Até 20% de Perda:** **INSTÁVEL** — Alerta de atenuação de sinal ou congestionamento de banda.
* 🔴 **Acima de 20% de Perda:** **INOPERANTE** — Falha crítica na interface de rede ou queda de link.