# Relógio em Python - Tempo Real.

# Import das bibliotecas usadas.
from tkinter import *
from tkinter import ttk

from datetime import datetime

# Cores selecionadas e armazenadas em variáveis.
cor_Preta = "#3d3d3d"
cor_Branca = "#f1fcff"
cor_Verde = "#21c25c"

# Criação da janela para o relógio com o uso da biblioteca Tkinter.
janela=Tk()
janela.geometry("440x180")
janela.title("Relógio - PYTHON")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor_Preta)

# Definindo uma função para resgatar os horários, dia, mês e ano.
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_Semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text = hora)
    l1.after(100, relogio)

    l2.config(text = dia_Semana + " - " + str(dia) + " / " + str(mes) + " / " + str(ano))

l1 = Label(janela, text="", font="Arial 80", bg=cor_Preta, fg=cor_Verde)
l1.grid(row = 0, column = 0, sticky = NW, padx = 5)

l2 = Label(janela, text="", font="Arial 20", bg=cor_Preta, fg=cor_Branca, )
l2.grid(row = 1, column = 0, sticky = NW, padx = 5)

relogio()
janela.mainloop()