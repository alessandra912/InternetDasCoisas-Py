# Importando biblioteca, as é utilizado para apelida biblioteca
import customtkinter as ctk

# Definindo tema
ctk.set_appearance_mode('dark')

# Começando janela
janela = ctk.CTk()
janela.geometry('600x400')
# Tirando janela no modo elástico, deixando-a estática
janela.resizable(False, False)
janela.title('Sistema de Acesso')
# Para mudar o icone é preciso baixar uma imagem no formato ico, a única aceita
janela.iconbitmap('01.ico')

# Elementos de dentro da Janela
titulo = ctk.CTkLabel(janela, 
                      text='Sistema de Acesso', 
                      text_color='#e01499',
                      font=('Verdana', 40))
titulo.pack(pady=20)



longin = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      placeholder_text='Digite o seu Login',
                      border_color='#e01499')
longin.pack()


senha = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      placeholder_text='Digite a sua Senha',
                      border_color='#e01499',
                      show='🤞')
senha.pack(pady=20)


botao = ctk.CTkButton(janela,
                      text='Acessar',
                      width=150,
                      height=40,
                      font=('Verdana', 20),
                      fg_color='black',
                      text_color='white')
botao.pack(pady=30)






janela.mainloop()