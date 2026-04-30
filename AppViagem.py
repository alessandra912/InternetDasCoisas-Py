import customtkinter as ctk;

ctk.set_appearance_mode('dark')

# FUNÇÃO

def calcular():
    d = int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    calculo = (d/c) * p
    resultado.configure(text=f'O valor final da viagem é R$ {calculo:.2f}')
    

janela = ctk.CTk()
janela.geometry('640x400')

janela.resizable(False, False)
janela.title('APP VIAGEM')

janela.iconbitmap('imagem.ico')

titulo = ctk.CTkLabel(janela,
                      text= 'APP VIAGEM',
                      text_color= 'white',
                      font=('Space Mono', 24))
titulo.pack(pady=20)


distancia = ctk.CTkEntry(janela,
                     width= 400,
                     height= 40,
                     placeholder_text='Digite a distância da viagem em KM',
                     border_color='white' )
distancia.pack(pady=5)


consumo = ctk.CTkEntry(janela,
                     width= 400,
                     height= 40,
                     placeholder_text='Digite o consumo do seu veiculo',
                     border_color='white')
consumo.pack(pady=5)


preco = ctk.CTkEntry(janela,
                     width= 400,
                     height= 40,
                     placeholder_text='Digite o preço atual do combustível',
                     border_color='white')
preco.pack(pady=5)


botao = ctk.CTkButton(janela,
                     text='Calcular Gasto',
                     width= 150,
                     height= 40,
                     font=('Verdana', 20),
                     fg_color='black',
                     command=calcular)
botao.pack(pady=20)

resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color='white',
                         font=('verdana', 25))
resultado.pack(pady=20)

janela.mainloop()