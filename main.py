import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import random

print("Iniciando ETL...")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Lendo usuarios.csv...")
df = pd.read_csv("usuarios.csv")

mensagens = [
    "Olá {nome}! Sua conta {conta} está ativa e pronta para uso!",
    "Oi {nome}, tudo bem? A conta {conta} já está liberada!",
    "{nome}, boas notícias! Sua conta {conta} está ativa!",
    "Olá {nome}! Seu cartão final {cartao} já pode ser utilizado!",
]

def gerar_mensagem(row):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente bancário educado."},
                {
                    "role": "user",
                    "content": f"""
                    Crie uma mensagem curta, amigável e profissional para um cliente de banco.
                    Nome: {row['nome']}
                    Conta: {row['conta']}
                    Cartão: {row['cartao']}
                    """
                }
            ],
            timeout=10
        )
        return response.choices[0].message.content.strip()

    except Exception:
        template = random.choice(mensagens)
        return template.format(
            nome=row['nome'], 
            conta=row['conta'], 
            cartao=row['cartao'][-1]
        )

print("Gerando mensagens...")
df["mensagem"] = df.apply(gerar_mensagem, axis=1)

# -----------------------------
# LOAD
# -----------------------------
print("Salvando mensagens_personalizadas.csv...")
df.to_csv("mensagens_personalizadas.csv", index=False)

print("ETL finalizado com sucesso!")