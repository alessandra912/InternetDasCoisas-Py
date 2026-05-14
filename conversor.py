import customtkinter as ctk;

ctk.set_appearance_mode('dark')


cotacao = 5.00

def converter_dolar():
    valor = float(conversor.get())
    resultado_convertido = valor / cotacao
    
    resultado.configure(text=f'R$ {valor:.2f} = US$ {resultado_convertido:.2f}')
    
def converter_real():
    valor = float(conversor.get())
    resultado_convertido = valor * cotacao
    
    resultado.configure(text=f'US$ {valor:.2f} = R$ {resultado_convertido:.2f}')

janela = ctk.CTk()
janela.geometry('640x400')

janela.resizable(False, False)
janela.title('Conversor de Moeda')

titulo = ctk.CTkLabel(janela,
                      text='Conversor de Moeda',
                      text_color='white',
                      font=('Space Mono', 24))
titulo.pack(pady=20)


conversor = ctk.CTkEntry(janela,
                         width=400,
                         height=40,
                         placeholder_text='Digite um valor para converter',
                         border_color='black')
conversor.pack(pady=20)


botao_dolar = ctk.CTkButton(janela,
                            text='Dólar',
                            width=150,
                            height=40,
                            font=('Verdana', 20),
                            fg_color='blue',
                            command=converter_dolar)
botao_dolar.pack(pady=5)


botao_real = ctk.CTkButton(janela,
                            text='Real',
                            width=150,
                            height=40,
                            font=('Verdana', 20),
                            fg_color='green',
                            command=converter_real)
botao_real.pack(pady=5)



resultado = ctk.CTkLabel(janela,
                            text='',
                            text_color='white',
                            font=('Verdana', 20))
resultado.pack(pady=20)

janela.mainloop()