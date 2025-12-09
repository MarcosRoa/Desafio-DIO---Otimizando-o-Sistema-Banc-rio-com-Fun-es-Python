# ✅ README.md
## Sistema Bancário em Python (CLI)
### Este projeto implementa um sistema bancário simples em Python, executado pelo terminal (CLI). O programa permite:
* Cadastro de usuários
* Criação de contas bancárias vinculadas aos usuários
* Lista de contas por usuário
* Depósitos
* Saques (limitados a 3 por conta)
* Exibição de saldo
* Histórico individual de operações
  
#### O sistema utiliza apenas estruturas básicas da linguagem (listas e dicionários), facilitando o aprendizado dos fundamentos da programação orientada a dados.
## 🚀 Funcionalidades
### 👤 Cadastro de Usuário
#### Cada usuário possui:
* Nome
* CPF (único, não pode repetir)
* Endereço formatado automaticamente

### 🏦 Criação de Conta Bancária
* Todas as contas são criadas na mesma agência (0001)
* Número da conta incrementado automaticamente
* Cada usuário pode ter múltiplas contas

### 💰 Depósito
* Permite adicionar saldo
* Registra operação no histórico
* Mostra o saldo atualizado

### 💸 Saque
* Limite de 3 saques por conta
* Impede saque maior que o saldo
* Registra operação no histórico

### 📄 Extrato / Saldo
* Exibe todas as operações realizadas
* Mostra o saldo atual
  
## 🧩 Tecnologias Utilizadas
* Python 3+
* Nenhum módulo externo (somente biblioteca padrão)

 ## 📂 Estrutura do Código
O programa é dividido em funções:
* criar_usuario()
* criar_conta()
* depositar()
*sacar()
* mostrar_saldo()
* extrato()
* E utiliza as listas globais:
  - usuarios
  - contas

## 📊 Diagrama de Fluxo
<img width="740" height="740" alt="image" src="https://github.com/user-attachments/assets/b3d2f2a0-a788-440d-a811-78a9803ccc8b" />

## OUTRAS OPERAÇÕES
─────────────────────────────────────────────────────────────
### Saques:
    - Verifica conta
    - Verifica limite de 3 saques
    - Verifica saldo suficiente
    - Atualiza saldo
    - Registra operação
    - Retorna ao menu

### Extrato:
    - Lista operações da conta
    - Mostra saldo final
    - Volta ao menu

### Sair:
    - Finaliza execução
