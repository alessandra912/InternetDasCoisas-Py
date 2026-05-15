import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# função
def calcular():
    media = (float(unidade1.get()) + 
             float(unidade2.get()) + 
             float(unidade3.get())) / 3
    if(media>=5):
        situacao = 'Parabéns, você foi aprovado!'
        text_color = 'green'
    else:
        situacao = 'Infelizmente você foi reprovado!' 
        text_color = 'red'
    resultado.configure(text=f'Média: {media:.1f}\n {situacao}', text_color=text_color)

# janela
janela = ctk.CTk()
janela.geometry("600x400")
janela.title('Sistema Escolar 2026')

# Corpo do aplicativo
titulo = ctk.CTkLabel(janela,
                      text='Sistema Escolar',
                      font=('Verdana', 45),
                      text_color='white')
titulo.pack(pady=20)


unidade1 = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        placeholder_text='Digite a sua nota da 1º unidade',
                        border_color='white')
unidade1.pack(pady=5)


unidade2 = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        placeholder_text='Digite a sua nota da 2º unidade',
                        border_color='white')
unidade2.pack(pady=5)


unidade3 = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        placeholder_text='Digite a sua nota da 3º unidade',
                        border_color='white')
unidade3.pack(pady=5)


botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      fg_color='yellow',
                      text_color='black',
                      text='Resultado',
                      command=calcular)
botao.pack(pady=20)


resultado = ctk.CTkLabel(janela,
                          text='',
                          font=('Verdana', 25),
                          text_color='white')
resultado.pack()

janela.mainloop()