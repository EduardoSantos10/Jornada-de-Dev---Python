# 🛡️ Projeto 05: Auditoria de Log de Tentativas de Invasão (SecOps Parser)

> Sistema automatizado em Python para monitoramento de perímetro, contagem de ameaças e gerenciamento de estado de firewall em tempo real, desenvolvido com foco em Segurança da Informação e Operações de Segurança (SecOps).

---

## 🎯 Sobre o Projeto

O **SecOps Parser** simula o comportamento interno de um sistema de detecção e prevenção de intrusão (IDS/IPS). Em ambientes corporativos de infraestrutura e redes, analistas e engenheiros precisam lidar com o fluxo contínuo de requisições maliciosas — como ataques de força bruta (*brute-force*) ou varreduras de portas. 

Este projeto automatiza a auditoria de pacotes de rede, avaliando o comportamento de IPs suspeitos e aplicando contramedidas automáticas de bloqueio assim que o limiar de segurança (*threshold*) é ultrapassado.

---

## 🧱 Arquitetura em 4 Blocos

Seguindo o padrão modular de desenvolvimento de sistemas, o script está estruturado nas seguintes etapas:

1. **Bloco 01 (Inputs / Aquisição):** Captura o endereço IP sob análise forense e define a constante de política de segurança (`LIMITE_ATAQUES = 5`).
2. **Bloco 02 (State / Contadores & Baselines):** Inicializa as variáveis de controle de estado (`contador_ataque = 0` e a *flag* booleana `bloqueado_firewall = False`).
3. **Bloco 03 (Logic Engine / Processamento):** Motor de decisão em laço contínuo (`while` com *retry logic*) que lê a simulação de tráfego inserida pelo operador, incrementa ataques e gerencia o gatilho de contenção.
4. **Bloco 04 (Reporting / Auditoria & Saída):** Emite o boletim forense pós-incidente, exibindo o IP do atacante, a volumetria de ameaças interceptadas e o status final da regra aplicada no Firewall (IPTables/WAF).

---

## ⚙️ Especificações Técnicas & Lógica Aplicada

* **Linguagem:** Python 3.x
* **Conceitos de TI Aplicados:**
  * **Identity and Access Management (IAM) & Security Baselines:** Aplicação de políticas restritivas de acesso.
  * **State Management:** Manipulação de variáveis booleanas para controle de fluxo de execução.
  * **Input Sanitization & Type Casting:** Conversão segura de dados de entrada (`int()`) para garantir a integridade das comparações lógicas.
  * **Threat Mitigation:** Automação de resposta a incidentes baseada em contadores de volumetria de requisições maliciosas.

---

## 🚀 Como Executar o Script

1. Certifique-se de ter o Python instalado em seu ambiente (Ubuntu ou Windows).
2. Clone o repositório e navegue até o diretório do projeto.
3. Execute o script via terminal:
   ```bash
   python3 projeto_05_secops.py