import customtkinter
import tkinter
from PIL import Image

# Configurações gerais que ultilizei por todo meu projeto

#Cores
white = '#ffffff'
black = '#383838'
blue = '#4634eb'
black_dark = '#262626'


#Fontes
font_title = ('calibri', 45, 'bold')
font_text = ('consolas', 25, 'bold')
font_menu = ('calibri', 25, 'bold')
font_label = ('calibri', 35, 'bold')

#Imagens
lapis_ico = customtkinter.CTkImage(
        dark_image=Image.open('imagens/ico_lapis_2.png'),
        size=(80, 80),
)
salvar_ico = customtkinter.CTkImage(
    dark_image=Image.open('imagens/salvar.png')
)
