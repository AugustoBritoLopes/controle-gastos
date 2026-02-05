# CLI Controle de Gastos

Uma ferramenta de linha de comando (CLI) simples e eficiente para registrar seus gastos pessoais diretamente em uma planilha do Google Sheets, sem precisar abrir o navegador.

Feito em Python, para quem prefere o terminal.

## Funcionalidades

* Registro Rapido: Adicione gastos com um unico comando.
* Automatico: Cria colunas para novos meses e linhas para novas categorias automaticamente.
* Inteligente: Se a categoria ja existe no mes, ele soma o valor ao total existente.
* Nuvem: Sincronizacao em tempo real com o Google Sheets (acessivel pelo celular depois).

## Pre-requisitos

* Python 3.8 ou superior
* Uma conta Google

## Instalacao

1. Clone o repositorio:
   git clone https://github.com/AugustoBritoLopes/controle-gastos.git
   cd cli-controle-gastos

2. Crie um ambiente virtual (Recomendado):
   # Windows
   python -m venv venv
   .\\venv\\Scripts\\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependencias:
   pip install -r requirements.txt

## Configuracao (Importante!)

Para que o script acesse sua planilha, voce precisa criar uma "Conta de Servico" no Google.

1.  Acesse o Google Cloud Console (https://console.cloud.google.com/).
2.  Crie um novo projeto.
3.  Va em "APIs e Servicos > Biblioteca" e ative duas APIs:
    * Google Sheets API
    * Google Drive API
4.  Va em "APIs e Servicos > Credenciais" e clique em "Criar Credenciais > Conta de Servico".
5.  De um nome (ex: bot-gastos) e clique em Continuar/Concluir.
6.  Na lista de contas de servico, clique no e-mail criado, va na aba "Chaves", clique em "Adicionar Chave > Criar nova chave > JSON".
7.  O download comecara. RENOMEIE esse arquivo para "credentials.json" e coloque na raiz da pasta do projeto.

### Conectando a Planilha
1.  Crie uma planilha no Google Sheets com o nome exato: Controle-Gastos
2.  Abra o arquivo credentials.json, copie o endereco de e-mail que esta em "client_email".
3.  Na sua planilha, clique em Compartilhar e de acesso de Editor para esse e-mail.

## Como Usar

### Modo Basico (Python direto)
python main.py <categoria> <valor>

Exemplos:
python main.py uber 25.50
python main.py "burger king" 40

## Dica de Visualizacao
Para deixar sua planilha bonita como um App:
1.  Congele a primeira linha e a primeira coluna.
2.  Use Formatacao Condicional (Escala de Cores) nas celulas de valor para criar um mapa de calor dos seus gastos.

## Contribuicao
Sinta-se a vontade para abrir Issues ou Pull Requests para melhorar o codigo!
"""
