import sqlite3
from tkinter import *
from tkinter import ttk
import DataBaseSoma

# Conectando ao banco de dados
conn = sqlite3.connect('Soma.db')
cursor = conn.cursor()

janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.Criar_Tabela()
        self.Labels()
        self.atualizar_tabela()  # Carregar dados existentes na tabela logo após a criação
        janela.mainloop()

    def tela(self):
        self.janela.title('SOMA DE NÚMEROS')
        self.janela.configure(background='black')
        self.janela.geometry('850x400')  # Ajuste o tamanho da janela conforme necessário
        self.janela.resizable(False, False)

    def Criar_Tabela(self):
        self.Tabela = ttk.Treeview(self.janela, height=20, columns=('col_id', 'col_1', 'col_2', 'col_res'))
        # Definindo colunas da tabela
        self.Tabela.heading('#0', text='')
        self.Tabela.heading('#1', text='Id')
        self.Tabela.heading('#2', text='Numero1')
        self.Tabela.heading('#3', text='Numero2')
        self.Tabela.heading('#4', text='Resultado')
        # Definindo tamanho das colunas
        self.Tabela.column('#0', width=1)
        self.Tabela.column('#1', width=50)
        self.Tabela.column('#2', width=100)
        self.Tabela.column('#3', width=100)
        self.Tabela.column('#4', width=100)
        # Definindo posição
        self.Tabela.place(relx=0.1, rely=0.2, relheight=0.7, relwidth=0.7)

    def limpa_tela(self):
        self.entrada_numero1.delete(0, END)
        self.entrada_numero2.delete(0, END)

    def Adicionar(self):
        # Selecionando as variáveis
        numero1 = float(self.entrada_numero1.get())
        numero2 = float(self.entrada_numero2.get())
        resultado = numero1 + numero2

        # Adicionando valores ao banco de dados
        cursor.execute("""
        INSERT INTO Somatorio (Numero1, Numero2, Resultado) VALUES (?, ?, ?)
        """, (numero1, numero2, resultado))
        DataBaseSoma.conn.commit()
        self.limpa_tela()
        self.atualizar_tabela()

    def Labels(self):
        self.lb_numero1 = Label(self.janela, text='Número 1', bg='white')
        self.lb_numero1.place(relx=0.05, rely=0.1, relheight=0.04, relwidth=0.1)
        self.entrada_numero1 = Entry(self.janela, bg='white')
        self.entrada_numero1.place(relx=0.16, rely=0.1, relheight=0.04, relwidth=0.1)

        self.lb_numero2 = Label(self.janela, text='Número 2', bg='white')
        self.lb_numero2.place(relx=0.4, rely=0.1, relheight=0.04, relwidth=0.1)
        self.entrada_numero2 = Entry(self.janela, bg='white')
        self.entrada_numero2.place(relx=0.51, rely=0.1, relheight=0.04, relwidth=0.1)

        self.botao_adiciona = Button(self.janela, background='gray', text='SOMAR', 
                                     command=self.Adicionar)
        self.botao_adiciona.place(relx=0.7, rely=0.1, relheight=0.05, relwidth=0.1)

    def atualizar_tabela(self):
        # Limpa a tabela existente
        for i in self.Tabela.get_children():
            self.Tabela.delete(i)

        # Preenche a tabela com dados do banco de dados
        cursor.execute("SELECT * FROM Somatorio")
        for row in cursor.fetchall():
            self.Tabela.insert('', END, values=row)

Application()
