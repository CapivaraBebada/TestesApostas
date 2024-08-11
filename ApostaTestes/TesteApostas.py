from tkinter import *
# Para criar as colunas 
from tkinter import ttk
# Para criar o calendario
from tkcalendar import Calendar, DateEntry
# Importando Banco de dados
import DataBaseTesteApostas

janela = Tk()

class Funcao():
    
    # Função para o botao LIMPAR
    def Limpar(self):
        self.Entrada_Competicao.delete(0, END)
        self.Entrada_Casa.delete(0, END)
        self.Entrada_Fora.delete(0, END)
        self.Entrada_Data.delete(0, END)
        self.Entrada_Mercado.delete(0, END)
        self.Entrada_Unidade.delete(0, END)
        self.Entrada_Odd.delete(0, END)    

    # Para criar calendário
    def calendario(self):
        # Mostrar calendário
        self.calendario1 = Calendar(self.Frame_1, fg='gray', bg='black', font=('Times', '9', 'bold'), 
                                   locale='pt_br')      # Indica o formato de data de acordo com o país
        self.calendario1.place(relx=0.27, rely=0.22)
        # Mostrar botão para inserir a data
        self.callData = Button(self.Frame_1, text='Inserir data', font=('Amble', 11, 'bold'), 
                               bg='#323437', fg='white', command=self.Printa_Data)
        self.callData.place(relx=0.5, rely=0.23, height=40, width=128)
    def Printa_Data(self):
        # Para inserir a data na entrada
        Pega_Data = self.calendario1.get_date()
        self.calendario1.destroy()
        self.Entrada_Data.delete(0, END)
        self.Entrada_Data.insert(END, Pega_Data)
        self.callData.destroy()

    def nao_apaga(self, event):
        # Impede que os primeiros três caracteres sejam apagados
        if self.Entrada_Em_conta.index(INSERT) <= 3 and event.keysym == 'BackSpace':
            return 'break'
        
    def sempre_inicio(self, event):
        # Garante que 'R$ ' esteja sempre no início
        if not self.Entrada_Em_conta.get().startswith('R$ '):
            self.Entrada_Em_conta.delete(0, END)
            self.Entrada_Em_conta.insert(0, 'R$ ')
        

class Application(Funcao):
    # Chamando Funções
    def __init__(self):
        self.janela = janela
        self.tela()
        self.tela_principal()
        self.Labels_Botoes()
        self.Tabela_Valores()
        self.Tabela_Apostas()
        self.Tabela_Green_Red()
        self.AdicionaEmTabelaApostas()
        janela.mainloop()
        
    def tela(self):
        self.janela.title('ANÁLISE DE APOSTAS')
        self.janela.configure(background='black')
        self.janela.geometry('1850x1000')
        self.janela.resizable(False, False)
        
    def tela_principal(self):
        # Tela à esquerda
        self.Frame_1 = Frame(self.janela, bg='black', highlightbackground='white', highlightthickness=1)
        self.Frame_1.place(relx=0.0, rely=0.0, relheight=1, relwidth=0.5)
        # Tela à direita
        self.Frame_2 = Frame(self.janela, bg='#061021', highlightthickness=1, highlightbackground='white')
        self.Frame_2.place(relx=0.5, rely=0.0, relheight=1, relwidth=0.5)

    def Labels_Botoes(self):
    # Label para valor EM CONTA
        self.Em_conta = Label(self.Frame_1, bg='#323437', highlightbackground='gray', foreground='white',text='Em conta', font=('Amble', 11, 'bold'))
        self.Em_conta.place(relx=0.02, rely=0.05, relwidth=0.14, relheight=0.04)
    # Entrada para o valor em conta
        self.Entrada_Em_conta = Entry(self.Frame_1, bg='#8c95a2', font=('Amble', 15, 'bold'))
        self.Entrada_Em_conta.place(relx=0.17, rely=0.051, relheight=0.039, relwidth=0.15)
            # Adicionando o símbolo no início
        self.Entrada_Em_conta.insert(0, 'R$ ')
            # Associar eventos para ter 'R$' no início do Label 'Em_conta'
        self.Entrada_Em_conta.bind("<KeyPress>", self.nao_apaga)
        self.Entrada_Em_conta.bind("<KeyRelease>", self.sempre_inicio)
        
    # Label do time da CASA
        self.lb_Casa = Label(self.Frame_1, bg='#323437', highlightbackground='gray', foreground='white',text='Time - Casa', font=('Amble', 11, 'bold'))
        self.lb_Casa.place(relx=0.02, rely=0.11, relheight=0.04, relwidth=0.14)
    # Entrada do time da CASA
        self.Entrada_Casa = Entry(self.Frame_1, bg='#8c95a2', text='Time da casa', font=('Amble', 15, 'bold'))
        self.Entrada_Casa.place(relx=0.17, rely=0.11, relheight=0.039, relwidth=0.15)
        
        # Label para ODD
        self.lb_Odd = Label(self.Frame_1, bg='#323437', font=('Amble', 11, 'bold'), text='Odd', foreground='white')
        self.lb_Odd.place(relx=0.02, rely=0.17, relheight=0.039, relwidth=0.14)
        # Entrada para ODD
        self.Entrada_Odd = Entry(self.Frame_1, bg='#8c95a2', font=('Amble', 15, 'bold'))
        self.Entrada_Odd.place(relx=0.17, rely=0.17, relheight=0.039, relwidth=0.15)
        
    # Label time COMPETIÇÃO
        self.lb_Competicao = Label(self.Frame_1, bg='#323437', text='Competição', font=('Amble', 11, 'bold'), foreground='white')
        self.lb_Competicao.place(relx=0.35, rely=0.05, relheight=0.039, relwidth=0.14)
    # Entrada time COMPETIÇÃO
        self.Entrada_Competicao = Entry(self.Frame_1, bg='#8c95a2', font=('Amble', 15, 'bold'))
        self.Entrada_Competicao.place(relx=0.50, rely=0.05, relheight=0.04, relwidth=0.14)
        
        # Label time de FORA
        self.lb_Fora = Label(self.Frame_1, bg='#323437', text='Time - Fora', font=('Amble', 11, 'bold'), foreground='white')
        self.lb_Fora.place(relx=0.35, rely=0.11, relheight=0.04, relwidth=0.14)   
        # Entrada do time de FORA
        self.Entrada_Fora = Entry(self.Frame_1, bg='#8c95a2', font=('Amble', 15, 'bold'))
        self.Entrada_Fora.place(relx=0.50, rely=0.11, relheight=0.04, relwidth=0.14) 
        
    # Label para UNIDADE
        self.lb_Unidade = Label(self.Frame_1, bg='#323437', font=('Amble', 11, 'bold'), text='Unidade', foreground='white')
        self.lb_Unidade.place(relx=0.68, rely=0.11, relheight=0.04,relwidth=0.14)
    # Entrada para UNIDADE
        self.Entrada_Unidade = Entry(self.Frame_1, bg='#8c95a2', font=('Amble', 15, 'bold'))
        self.Entrada_Unidade.place(relx=0.83, rely=0.11, relheight=0.04, relwidth=0.14)     
        
        # Label para MERCADO
        self.lb_Mercado = Label(self.Frame_1, bg='#323437', font=('Amble', 11, 'bold'), text='Mercado', foreground='white')
        self.lb_Mercado.place(relx=0.68, rely=0.05, relheight=0.04, relwidth=0.14)   
        # Entrada para MERCADO
        self.Entrada_Mercado = Entry(self.Frame_1, bg='#8c95a2', font=('Amble', 15, 'bold'))
        self.Entrada_Mercado.place(relx=0.83, rely=0.05, relheight=0.04, relwidth=0.14)
        
    # DATA
            # Criando botão para abrir o calendário
        self.bt_calendario = Button(self.Frame_1, text='Data do jogo', bg='#323437', font=('Amble', 11, 'bold'), fg='white', 
                                    command=self.calendario)
        self.bt_calendario.place(relx=0.35, rely=0.17, relheight=0.04, relwidth=0.14)
            # Criando entrada para mostrar a data selecionada
        self.Entrada_Data = Entry(self.Frame_1, width= 10, font=('Amble', 15, 'bold'), bg='#8c95a2')
        self.Entrada_Data.place(relx=0.5, rely=0.17, height=40, width=128)

    # Botão GANHOU
        self.Botao_ganhou = Button(self.Frame_1, bg='#323437', font=('Amble', 15, 'bold'), text='GANHOU', 
                                   activebackground='green', foreground='white', command=self.AdicionaEmTabelaApostas)
        self.Botao_ganhou.place(relx=0.7, rely=0.19, relheight=0.07, relwidth=0.11)
        
    # Botão PERDEU
        self.Botao_perdeu = Button(self.Frame_1, bg='#323437', font=('Amble', 15, 'bold'), text='PERDEU', activebackground='red', foreground='white')
        self.Botao_perdeu.place(relx=0.85, rely=0.19, relheight=0.07, relwidth=0.1)
        
        # Botão ALTERAR
        self.Botao_Alterar = Button(self.Frame_1, bg='#323437', font=('Amble', 11, 'bold'), text='Alterar', fg='white')
        self.Botao_Alterar.place(relx=0.02, rely=0.25, relheight=0.04, relwidth=0.14)

        # Botão LIMPAR
        self.Botao_Limpar = Button(self.Frame_1, bg='#323437', font=('Amble', 11, 'bold'), text='Limpar', fg='white',
                                    command=self.Limpar)
        self.Botao_Limpar.place(relx=0.02, rely=0.31, relheight=0.04, relwidth=0.14)
        
    # Botão Excluir
        self.Botao_Excluir = Button(self.Frame_1, bg='#323437', font=('Amble', 11, 'bold'), text='Ecluir', fg='white')
        self.Botao_Excluir.place(relx=0.76, rely=0.3, relheight=0.04, relwidth=0.14)
    
        #Criando moldura
        self.canvas_1 = Canvas(self.Frame_1, bd=1, bg='black', highlightbackground='white', highlightthickness=2)
        self.canvas_1.place(relx=0.07, rely=0.38, relwidth=0.47, relheight=0.09)
        self.canvas_2 = Canvas(self.Frame_1, bd=1, bg='black', highlightbackground='white', highlightthickness=2)
        self.canvas_2.place(relx=0.59, rely=0.38, relwidth=0.32, relheight=0.09)
        
    # Tabela de apostas
    def Tabela_Apostas(self):
        # Criando colunas
        self.tabela = ttk.Treeview(self.Frame_1, height=50, columns=('col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9', 'col_10'))
        self.tabela.heading('#0', text='')
        self.tabela.heading('#1', text='id')
        self.tabela.heading('#2', text='Data')
        self.tabela.heading('#3', text='Competicao')
        self.tabela.heading('#4', text='Casa')
        self.tabela.heading('#5', text='Fora')
        self.tabela.heading('#6', text='Mercado')
        self.tabela.heading('#7', text='Odd')
        self.tabela.heading('#8', text='Unidade')
        self.tabela.heading('#9', text='L/P')
        self.tabela.heading('#10', text='Montante')
        # Definindo tamanho de colunas
        self.tabela.column('#0', width=1)
        self.tabela.column('#1', width=50)
        self.tabela.column('#2', width=50)
        self.tabela.column('#3', width=50)
        self.tabela.column('#4', width=50)
        self.tabela.column('#5', width=50)
        self.tabela.column('#6', width=50)
        self.tabela.column('#7', width=50)
        self.tabela.column('#8', width=50)
        self.tabela.column('#9', width=50)
        self.tabela.column('#10', width=50)
        # Definindo lugar
        self.tabela.place(relx=0.02, rely=0.52, relheight=0.44, relwidth=0.94)
                
        self.scroolLista = Scrollbar(self.Frame_1, orient='vertical')   # Definindo direção da barra
        self.tabela.configure(yscroll=self.scroolLista.set)   # Adicionando a barra à "ListaCli"
        self.scroolLista.place(relx=0.96, rely=0.52, relwidth=0.02, relheight=0.44)
        #self.tabela.bind("<Double-1>", self.duplo_click)      # "bind" define tipo de interação, no caso, duplo click

    def Tabela_Valores(self):
        # Criando colunas
        self.tabela_valores = ttk.Treeview(self.Frame_1, height=10, columns=('col_1', 'col_2', 'col_3'))
        self.tabela_valores.heading('#0', text='')
        self.tabela_valores.heading('#1', text='Valor inicial')
        self.tabela_valores.heading('#2', text='Lucro')        
        self.tabela_valores.heading('#3', text='Total')
        # Definindo tamanho das colunas
        self.tabela_valores.column('#0', width=1)
        self.tabela_valores.column('#1', width=100)
        self.tabela_valores.column('#2', width=100)        
        self.tabela_valores.column('#3', width=100)
        # Definindo lugar
        self.tabela_valores.place(relx=0.08, rely=0.39, relheight=0.07, relwidth=0.45)
    
    def Tabela_Green_Red(self):
        #Criando tabela
        self.tabela_acertos = ttk.Treeview(self.Frame_1, height=10, columns=('col_1', 'col_2'))
        self.tabela_acertos.heading('#0', text='')
        self.tabela_acertos.heading('#1', text='Green')
        self.tabela_acertos.heading('#2', text='Red')
        # Definindo tamanhp das colunas
        self.tabela_acertos.column('#0', width=1)
        self.tabela_acertos.column('#1', width=100)
        self.tabela_acertos.column('#2', width=100)
        # Definindo posição
        self.tabela_acertos.place(relx=0.6, rely=0.39, relheight=0.07, relwidth=0.3) 

   # Associando valores do banco de dados à TABELA PRINCIPAL
    def AdicionaEmTabelaApostas(self):
        # Selecioando valores
        Data = self.Entrada_Data.get()
        Competicao = self.Entrada_Competicao.get()
        Casa = self.Entrada_Casa.get()
        Fora = self.Entrada_Fora.get()
        Mercado = self.Entrada_Mercado.get()
        Odd = float(self.Entrada_Odd.get())
        Unidade = float(self.Entrada_Unidade.get())
        Em_Conta = float(self.Entrada_Em_conta.get())
        # Apenas ganhas
        L_P = Unidade * Odd
        Montante = L_P + Em_Conta
        
        #Adicionando valores ao banco de dados
        DataBaseTesteApostas.cursor.execute("""
        INSERT INTO  AnaliseTeste (Data, Competicao, Casa, Fora, Mercado, Odd, Unidade, L_P, Montante)
        VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (Data, Competicao, Casa, Fora, Mercado, Odd, Unidade, L_P, Montante))
        
        DataBaseTesteApostas.conn.commit()
        self.Limpar()
        self.AtualizaTabelaApostas()
        
        '''     
            Erro na linha 243. 
            O erro diz que não tem como converter string em float, associada ao valor da variável 'Odd'. 
        Porém, já é estabelecido, no banco de dados, que o tipo de caractere que essa variável receberá é um valor real.
        O erro aparece antes mesmo de abrir a janela, sendo assim, parece que, primeiramente o código interpreta que esta
        widget já está preenchida com alguma string, mesmo estando vazia, pois eu não digitei nada nela, já que a janela 
        não cheaga a abrir. Para garantir que fique vazia, tentei o '.strip()', mas ainda dá o mesmo erro.
        '''
        
    def AtualizaTabelaApostas(self):
        # Limpar tabela existente
        for i in self.tabela.get_children():
            self.tabela.delete(i)
        
        # Preenchendo tabela com dados do banco de daddos
        cursor = DataBaseTesteApostas.conn.cursor()
        cursor.execute("SELECT * FROM AnaliseTeste")
        for row in cursor.fetchall():
            self.tabela.insert('', END, values=row)


Application()
