import customtkinter 
import tkinter as tk
from tkinter import filedialog
import configs
from bloco import NovaAba, AbrirAba

class PaginaInicial:
    def __init__(self):
        customtkinter.set_appearance_mode('dark') # Configuração do Tema da Tela
        self.root = customtkinter.CTk()  # Tela da Pagina Inicial
        self.root.resizable(height=False, width=False) # False não permite a tela maximisar o mudar de tamanho
        self.root.geometry("580x480") # Dimesionamento da Tela
        self.root.title("Notas") # Titulo

        #Imagens
        self.new_ico = tk.PhotoImage(file='imagens/novo.png')
        self.open_ico = tk.PhotoImage(file='imagens/open.png')
    
    def abrir_bloco(self):
        # Metodo  que cria um objeto da Classe AbrirAba e instacia ele
        open_aba = AbrirAba() # Objeto
        open_aba.selecionar_arquivo() # Metodo para selecionar um arquivo
        open_aba.run() # Metodo principal
        
    def novo_bloco(self):
        # Metodo que Cria um objeto  da Classe NovaAba e instacia ele
        nova_aba = NovaAba() # Objeto
        nova_aba.run() # Metodo principal

    def frames(self):
        # Frames
        self.frm_top = customtkinter.CTkFrame(  # Frame Parte de cima
            self.root,
            width=580,
            height=100,
            fg_color=configs.black_dark,
        )
        self.frm_master = customtkinter.CTkFrame( # Frame Principal
            self.root,
            width=520,
            height=380,
            fg_color=configs.black,
        )
    
    def widgets(self):
        # Labels
        self.label_title = customtkinter.CTkLabel(
            self.frm_top,
            text="JS Notas",
            font=configs.font_title,
            text_color=configs.white
        )
        self.label_image = customtkinter.CTkLabel(
            self.frm_top,
            image=configs.lapis_ico,
            text=''
        )
        self.label_new = customtkinter.CTkLabel(
            self.frm_master,
            text='Novo Bloco',
            text_color=configs.white,
            font=configs.font_label,
            fg_color=configs.black_dark
        )
        self.label_open = customtkinter.CTkLabel(
            self.frm_master,
            text='Abrir arquivo',
            font=configs.font_label,
            text_color=configs.white,
            fg_color=configs.black_dark,
        )

        # Buttons
        self.btn_novo = customtkinter.CTkButton(
            self.frm_master,
            image=self.new_ico,
            text="",
            width=10,
            fg_color=configs.black_dark,
            command=self.novo_bloco
        )
        self.btn_open = customtkinter.CTkButton(
            self.frm_master,
            image=self.open_ico,
            text="",
            width=10,
            fg_color=configs.black_dark,
            command=self.abrir_bloco
        )

    def draw_frm(self):
        # Posiciona os frames na tela
        self.frm_top.place(x=0, y=0)
        self.frm_master.place(x=60, y=100)
    

    def draw_widgets(self):
        # Posiciona as Labels
        self.label_title.place(x=20, y=22)
        self.label_image.place(x=200, y=10)
        self.label_new.place(x=10, y=10)
        self.label_open.place(x=10, y=65)

        # Posiciona os Botãos
        self.btn_novo.place(x=187, y=8)
        self.btn_open.place(x=210, y=62)

    def run(self):
        # Metodo que inicia a minha apilicação com todos os elementos na tela
        self.frames()
        self.widgets()
        self.draw_widgets()
        self.draw_frm()
        self.root.mainloop()
        
        