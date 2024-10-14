# 🔐 Sistema de Login Simples em Python

Este é um sistema de login simples escrito em Python. O usuário tem três tentativas para inserir as credenciais corretas (nome de usuário e senha). Se o login for bem-sucedido, uma mensagem de boas-vindas é exibida e o programa termina. Caso o usuário erre todas as tentativas, o acesso é bloqueado, e uma mensagem repetida três vezes é exibida.

## Funcionalidades

- Verifica o nome de usuário e a senha inseridos.
- Permite até três tentativas de login.
- Exibe uma mensagem de boas-vindas se as credenciais estiverem corretas.
- Bloqueia o acesso após três tentativas falhadas, exibindo a mensagem "Acesso bloqueado" três vezes.

## Como funciona

1. O usuário tem **três tentativas** para acertar o nome de usuário e a senha.
2. Se as credenciais forem corretas, o programa imprime **"Bem-vindo(a)!"** e encerra.
3. Se o usuário errar as credenciais, o programa informa quantas tentativas restam.
4. Após três tentativas incorretas, o acesso é bloqueado e a mensagem **"Acesso bloqueado"** é exibida três vezes.

## Requisitos

- Python 3.x

## Como Executar

1. Clone ou baixe este repositório para a sua máquina.
2. Navegue até o diretório do projeto no terminal.
3. Execute o seguinte comando para rodar o programa:

   ```bash
   python login.py
