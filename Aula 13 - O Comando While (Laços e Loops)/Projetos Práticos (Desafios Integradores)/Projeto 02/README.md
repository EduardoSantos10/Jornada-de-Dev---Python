# 📊 Sistema de Coleta de Métricas Multiservisor (SRE Dashboard CLI)

> **Módulo:** SRE (Site Reliability Engineering) & Observabilidade de Infraestruturas  
> **Linguagem:** Python 3.x  
> **Conceitos:** Auditoria de Clusters, Gestão de Thresholds (SLIs/SLOs), Matriz de Saúde Operacional, Arquitetura em 4 Blocos.

---

## 📌 Visão Geral do Projeto

Este projeto consiste em uma ferramenta de linha de comando (CLI) desenvolvida para automatizar a auditoria de saúde de um cluster corporativo de servidores. 

Diferente de monitorar um único host isolado, a aplicação consolida métricas de múltiplos servidores em tempo real, aplicando regras rígidas de limiar (*Thresholds*) de CPU para classificar o ecossistema em estados operacionais distintos e gerar um painel unificado para o time de Operações (NOC/SRE).

---

## 🏛️ Arquitetura do Sistema (4 Blocos)

O script foi estruturado seguindo o modelo de separação de responsabilidades em 4 estágios:

| Bloco | Função | Descrição |
| :--- | :--- | :--- |
| **Bloco 01** | `Escopo e Inputs` | Captura o tamanho do inventário e a quantidade de nós do cluster a serem auditados. |
| **Bloco 02** | `Gestão de Estado` | Inicializa os contadores de saúde (`OK`, `ALERTA`, `CRÍTICO`) e o iterador de controle. |
| **Bloco 03** | `Engine (Event Loop)` | Executa o laço de varredura sequencial (`while`), coletando Hostnames e usos de CPU. |
| **Bloco 04** | `Relatório SRE` | Consolida os dados e exibe o dashboard final com o resumo de saúde do cluster. |

---

## 📐 Matriz de Limiares e SLA de Hardware

O script avalia o consumo de processamento de cada servidor com base em três faixas operacionais críticas para a engenharia de confiabilidade:

* 🟢 **CPU < 70%:** **OK** — Servidor operando dentro da normalidade e capacidade ideal.
* 🟡 **CPU entre 70% e 85%:** **ALERTA** — Servidor sob carga elevada; requer monitoramento preventivo.
* 🔴 **CPU > 85%:** **CRÍTICO** — Servidor em estado de saturação severa; exige intervenção imediata ou redistribuição de carga (*Load Balancing*).

---

## 🚀 Como Executar o Projeto

1. Certifique-se de possuir o **Python 3.x** instalado em seu ambiente (Windows, Linux Ubuntu ou macOS).
2. Baixe ou clone os arquivos do projeto para o seu diretório de trabalho.
3. Abra o terminal na pasta do projeto e execute o script:
   ```bash
   python main.py