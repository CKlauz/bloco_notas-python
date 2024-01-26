import customtkinter 
from tkinter import filedialog
import configs

class NovaAba:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry('580x480')
        self.root.resizable(width=False, height=False) 
        self.root.config(bg=configs.black_dark)
        self.root.title("Nota")

    def salvar_arquivos(self):
        # Metodo para salvar arquivos
        titulo = self.title.get() # Pega o titulo da nota e automaticamente é colocado ao salvar o arquivo
        file_path = filedialog.asksaveasfilename( # Seleciona o caminho para salvar o arquivo
            defaultextension='.txt', # Extensão do arquivo 
            initialfile=titulo, # Titulo
            filetypes=[("Arquivos de texto", "*.txt",),( "Todos os arquivos", "*.*")]
            )
        
        if file_path: # Condição para verificar se um caminho foi selecionado
            with open(file_path, "w") as file: # Se sim abri o arquivo com o with
                conteudo = self.body.get('0.0', 'end') # Copia o texto da minha caixa de texto
                file.write(conteudo) # E cola o texto no arquivo txt
    
    def frames(self):
        # Frames
        self.frm_top = customtkinter.CTkFrame( # Frame de cima
            self.root,
            width=580,
            height=100,
            fg_color=configs.black_dark,
        )
        self.frm_body = customtkinter.CTkFrame( # Frame parte do texto
            self.root,
            width=580,
            height=400,
            fg_color=configs.black,
        )
        
    def widgets(self):
        # Label
        self.title = customtkinter.CTkEntry( 
            self.frm_top,
            width=420,
            height=100,
            font=configs.font_title,
            fg_color=configs.black_dark,
            text_color=configs.white,
            border_color=configs.black_dark,
            placeholder_text="Título",
        )

        # Caixa de Texto
        self.body = customtkinter.CTkTextbox(
            self.frm_body,
            width=580,
            height=400,
            font=configs.font_text,
            fg_color=configs.black,
            text_color=configs.white,
        )

        # Botão
        self.btn_salvar = customtkinter.CTkButton(
            self.root,
            width=10,
            fg_color=configs.black,
            font=configs.font_menu,
            text_color=configs.white,
            text='Salvar',
            command=self.salvar_arquivos
        )
      
    def draw_widgets(self):
        # Posiciona os widgets na tela
        self.widgets()
        self.title.place(x=0, y=0)
        self.body.place(x=0, y=0)
        self.btn_salvar.place(x=500, y=5)

    def draw_frames(self):
        # Posiciona os frames na tela
        self.frames()
        self.frm_top.place(x=0, y=0)
        self.frm_body.place(x=0, y=100)

    def run (self):
        #Metodo principal
        self.draw_frames()
        self.draw_widgets()
        self.root.mainloop()
        
class AbrirAba(NovaAba): # Herda da classe NovaAba com alguns metodos a mais
    def __init__(self):
        super().__init__()

    def selecionar_arquivo(self):
        # Selecionar arquivo
        self.file_path = filedialog.askopenfilename( # Seleciona o caminho do arquivo
            defaultextension=".txt", # Extensão do arquivo
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")]
            )
        if self.file_path: # Condição se houver um caminho
            with open(self.file_path, "r") as file: # Abre com o with
                self.conteudo = file.read() # E copia todo o texto do arquivo 
    
    def inserir_texto(self):
        self.body.delete('0.0', 'end') # (Nem precisava mas fico ai)
        self.body.insert('0.0', f'{self.conteudo}' ) # Colo a minha variavel conteudo 
        # que esta com o texto no meu Campo de texto
    
    def run(self):
        # Metodo principal
        self.draw_frames()
        self.draw_widgets()
        self.inserir_texto()
        self.root.mainloop()
        