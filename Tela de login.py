import tkinter as tk # Importa e apelida
from tkinter import messagebox # Importa a função de mensagens
#from PIL import Image, ImageTk # Importa as classes ImageTk da biblioteca PIL
import os # Importa biblioteca que verifica a existência de arquivos

                # Criando funções

def confirmar(): # Mostra uma mensagem ao clicar no botão 'confirmar'
    messagebox.showinfo("Confirmar", "Login confirmado")

def cancelar(): # Fecha a janela ao clicar no botão 'cancelar'
    root.destroy()
    
                # Construção do formulario

# Cria a janela principal
root = tk.Tk()
root.title("Formulário de login") # Titulo da página

root.geometry("500x500") # Ajusta o tamanho da janela

            # Criando frame para os campos de login e senha

frame = tk.Frame(root)
frame.pack(pady=10)

# Cria um campo de entrada para o LOGIN
login_label = tk.Label(frame, text="Login:")
login_label.grid(row=0, column=0, padx=5, pady=5) # Adiciona rotulo ao frame
login_entry = tk.Entry(frame)
login_entry.grid(row=0, column=1, padx=5, pady=5) # Adiciona campo de entrada ao frame

# Cria um campo de entrada para a SENHA
senha_label = tk.Label(frame, text="Senha:")
senha_label.grid(row=1, column=0, padx=5, pady=5) # Adiciona rotulo ao frame
senha_entry = tk.Entry(frame, show="*") #Oculta a senha digitada (*)
senha_entry.grid(row=1, column=1, padx=5, pady=5) # Adiciona campo de entrada ao frame

            # Criando os botões confirmar e cancelar

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Cria um botão para confirmar o login
confirmar_button = tk.Button(button_frame, text="Confirmar", command=confirmar)
confirmar_button.grid(row=0, column=0, padx=5) # Adiciona botão ao frame

# Cria um botão para cancelar o login
cancelar_button = tk.Button(button_frame, text="Cancelar", command=cancelar)
cancelar_button.grid(row=0, column=1, padx=5) # Adiciona botão ao frame


                # Adicionar uma imagem

image_path = r"D:\ALUNO\imagens\niketenis1.png"
if os.path.exists(image_path): # Verifica se o caminho do arquivo existe
    try:
        image = Image.open(image_path) # Abre a imagem
        image = image.resize((200,200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image) # Converte a imagem para um formato compativel com Tkinter

        # Cria rótulo para exibir a imagem
        image_label = tk.Label(root, image=photo)
        image_label.image = photo # Mantem uma refência da imagem para evitar que seja coletada pelo garbage
        image_label.pack(pady=10) # Adiciona o rótulo à janela com um espaçamento vertical
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir a imagem: {e}")
    else:
        messagebox.showerror("Erro", f"Arquivo não foi encontrado: {e}")


root.mainloop()