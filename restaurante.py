import customtkinter as ctk;

ctk.set_appearance_mode('dark')

def calcular():
    valorTotal = float(valorConsumido.get())
    valorPorPessoa = float(quatidadePessoas.get())
    
    taxaServico = valorTotal * 0.10
    valorTotal += taxaServico
    valorPorPessoa = valorTotal / valorPorPessoa
    
    taxa.configure(text=f'Taxa de Serviço (10%): R$ {taxaServico:.2f}')
    total.configure(text=f'Valor Total: R$ {valorTotal:.2f}')
    valorIndividual.configure(text=f'Valor Individual (por pessoa): R$    {valorPorPessoa:.2f}')

janela = ctk.CTk()
janela.geometry('640x500')
janela.title('Comando Digital de Restaurante')

titulo = ctk.CTkLabel(janela,
                    text='Comando Digital de Restaurante',
                    font=('verdana', 20),
                    text_color='orange')
titulo.pack(pady=20)


valorConsumido = ctk.CTkEntry(janela,
                               width=400,
                               height=40,
                               placeholder_text='Digite o valor consumido',
                               border_color='gray')
valorConsumido.pack(pady=5)


quatidadePessoas = ctk.CTkEntry(janela,
                               width=400,
                               height=40,
                               placeholder_text='Digite a quantidade de pessoas',
                               border_color='gray')
quatidadePessoas.pack(pady=20)


botao = ctk.CTkButton(janela,
                               width=400,
                               height=40,
                               fg_color='#ed671a',
                               text_color='white',
                               text='FECHAR CONTA',
                               border_color='orange',
                               command=calcular)
botao.pack(pady=30)


taxa = ctk.CTkLabel(janela,
                               text='R$ 0,00',
                               font=('verdana',25),
                               text_color='green')
taxa.pack(pady=5)


total = ctk.CTkLabel(janela,
                               text='R$ 0,00',
                               font=('verdana',25),
                               text_color='green')
total.pack(pady=5)


valorIndividual = ctk.CTkLabel(janela,
                               text='R$ 0,00',
                               font=('verdana',25),
                               text_color='green')
valorIndividual.pack(pady=5)

janela.mainloop()