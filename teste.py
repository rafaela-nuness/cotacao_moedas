import tkinter as tk
from tkinter import ttk
import requests


def consultar_cotacao():

    moeda = combo_moeda.get()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    resposta = requests.get(url)

    dados = resposta.json()

    cotacao = dados[f"{moeda}BRL"]["bid"]

    resultado.config(
        text=f"1 {moeda} = R$ {float(cotacao):.2f}"
    )


janela = tk.Tk()

janela.title("Cotação de Moedas")
janela.geometry("400x300")


titulo = tk.Label(
    janela,
    text="COTAÇÃO DE MOEDAS",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=30)


combo_moeda = ttk.Combobox(
    janela,
    values=["USD", "EUR", "GBP", "JPY"],
    state="readonly"
)

combo_moeda.pack()

combo_moeda.set("USD")


botao = tk.Button(
    janela,
    text="Consultar Cotação",
    command=consultar_cotacao
)

botao.pack(pady=20)


resultado = tk.Label(
    janela,
    text="Aguardando consulta...",
    font=("Arial", 16, "bold")
)

resultado.pack(pady=20)


janela.mainloop()