# 💾 Incremental Disk Backup Manager (Storage Capacity Planning CLI)

> **Módulo:** Storage, SysAdmin & Governança de Infraestrutura  
> **Linguagem:** Python 3.x  
> **Conceitos:** Capacity Planning, Prevenção de Estouro de Mídia (Buffer Overflow), Controle de Laços com Sentinela (`while True` + `break`), Arquitetura em 4 Blocos.

---

## 📌 Visão Geral do Projeto

Este projeto consiste em uma ferramenta de linha de comando (CLI) desenvolvida para simular a rotina de gravação de um **Gerenciador de Backup Incremental**. 

A aplicação monitora e valida a capacidade máxima de fitas ou discos de armazenamento (NAS/SAN) em tempo real, impedindo que novos arquivos excedam o volume disponível. O sistema utiliza validação prévia de capacidade antes do commit dos arquivos, prevenindo corrupção de dados e falhas em discos de destino.

---

## 🏛️ Arquitetura do Sistema (4 Blocos)

O script foi projetado seguindo a separação estrutural em 4 estágios operacionais:

| Bloco | Função | Descrição |
| :--- | :--- | :--- |
| **Bloco 01** | `Inputs e Mídia` | Captura a capacidade total em Gigabytes (GB) do volume/fita de backup. |
| **Bloco 02** | `Gestão de Estado` | Inicializa as variáveis de controle de espaço utilizado (`0 GB`) e quantidade de arquivos salvos (`0`). |
| **Bloco 03** | `Engine & Safe-Commit` | Laço infinito (`while True`) que simula a soma e valida previamente o estouro do limite antes de salvar o arquivo. |
| **Bloco 04** | `Relatório de Mídia` | Exibe o total de arquivos persistidos e o percentual de ocupação útil da mídia ao encerrar a rotina. |

---

## 📐 Regra de Negócio & Capacity Planning

A validação de gravação segue a lógica de segurança do Kernel do sistema operacional:

$$\text{Espaço Simulado} = \text{Espaço Já Ocupado} + \text{Tamanho do Novo Arquivo}$$

* **Se $\text{Espaço Simulado} \le \text{Capacidade Total}$:** O arquivo é gravado com sucesso, o espaço ocupado é atualizado e o contador de arquivos é incrementado.
* **Se $\text{Espaço Simulado} > \text{Capacidade Total}$:** O sistema emite um alerta de *"Espaço Insuficiente na Mídia!"*, aborta a operação via `break` e protege o volume contra escrita além do limite físico.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de possuir o **Python 3.x** instalado.
2. Clone ou faça o download dos arquivos no seu ambiente de desenvolvimento.
3. Execute o script no terminal:
   ```bash
   python main.py
   ```
4. Informe o tamanho total do disco e insira os arquivos sequencialmente até atingir a capacidade máxima da mídia.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Python 3** (Laços de repetição `while True`, controle de fluxo com `break`, estruturas condicionais `if/else`, operações aritméticas de acúmulo).
* **Storage & SysAdmin** (Gestão de capacidade de fitas LTO, volumes RAID, quotas de disco e rotinas de salvaguarda de dados).
* **Engenharia de Software** (Tratamento preventivo de estouro de limites e validação prévia de transações).