📊 Projeto ETL – Mensagens Personalizadas para Clientes Bancários

Este projeto foi desenvolvido como parte do Bootcamp Santander 2025 – Ciência de Dados com Python, com o objetivo de praticar o fluxo ETL (Extração, Transformação e Carga) utilizando Python.

O sistema lê dados de clientes a partir de um arquivo CSV, gera mensagens personalizadas para cada usuário (utilizando IA quando disponível) e salva o resultado em um novo arquivo CSV.

🧠 Objetivo do Projeto

Demonstrar, de forma prática, o funcionamento de um pipeline ETL, focando no fluxo de dados e não na dependência de uma API específica.

O projeto foi adaptado para funcionar mesmo quando a API externa (OpenAI) estiver indisponível, garantindo robustez e continuidade do processo.

🔄 Fluxo ETL
1️⃣ Extração (Extract)

Os dados dos clientes são lidos a partir do arquivo:

usuarios.csv


Esse arquivo contém informações como:

ID do cliente

Nome

Número da conta

Cartão (mascarado)

2️⃣ Transformação (Transform)

Para cada cliente, o sistema gera uma mensagem personalizada:

🔹 Prioridade: uso da API da OpenAI para criar mensagens naturais e variadas.

🔹 Fallback: caso a API esteja indisponível (erro de quota, conexão, etc.), o sistema utiliza templates dinâmicos em Python, garantindo personalização básica.

Cada mensagem considera dados específicos do cliente, como nome, conta e final do cartão.

3️⃣ Carga (Load)

O resultado final é salvo no arquivo:

mensagens_personalizadas.csv


Esse arquivo contém todas as colunas originais mais a coluna mensagem, pronta para consumo por outro sistema.

🛠️ Tecnologias Utilizadas

Python 3.10+

Pandas

OpenAI SDK (opcional)

dotenv

Git & GitHub

Ambiente virtual (venv)

📁 Estrutura do Projeto
Desafio/
├── usuarios.csv
├── mensagens_personalizadas.csv
├── main.py
├── .env
├── .gitignore
└── README.md

🔐 Variáveis de Ambiente

A chave da OpenAI é armazenada em um arquivo .env para maior segurança.

Exemplo de .env:
OPENAI_API_KEY=sua_chave_aqui


⚠️ O arquivo .env não deve ser versionado.

▶️ Como Executar o Projeto
1️⃣ Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate

2️⃣ Instalar as dependências
pip install pandas openai python-dotenv

3️⃣ Executar o script
python3 main.py

📌 Observações Importantes

O projeto não depende exclusivamente da API da OpenAI para funcionar.

Caso a API esteja indisponível, o fallback garante a geração de mensagens personalizadas.

O foco do desafio é o entendimento do fluxo ETL, não o uso obrigatório de IA.
