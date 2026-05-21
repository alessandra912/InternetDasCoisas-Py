import customtkinter as ctk

ctk.set_appearance_mode('dark')

def calcular():
    salario = float(salario_bruto.get())
    
    if salario <= 2112.00:
        salario_liquido = salario
    elif salario <= 2826.65:
        salario_liquido = salario - (salario * 0.075)
    else:
        salario_liquido = salario - (salario * 0.15)
    
    resultado.configure(text=f'Salário Líquido: {salario_liquido:.2f}')

janela = ctk.CTk()
janela.geometry('640x450')
janela.title('Cálculo de Imposto de Renda')

titulo = ctk.CTkLabel(janela,
                    text='Cálculo de Imposto de Renda',
                    font=('verdana', 20),
                    text_color='white')
titulo.pack(pady=20)


nomeFuncionario = ctk.CTkEntry(janela,
                               width=400,
                               height=40,
                               placeholder_text='Digite o nome do funcionário',
                               border_color='black')
nomeFuncionario.pack(pady=5)


salario_bruto = ctk.CTkEntry(janela,
                               width=400,
                               height=40,
                               placeholder_text='Digite o salário bruto',
                               border_color='black')
salario_bruto.pack(pady=20)


botao = ctk.CTkButton(janela,
                               width=400,
                               height=40,
                               fg_color='blue',
                               text_color='white',
                               text='CALCULAR IMPOSTO',
                               border_color='black',
                               command=calcular)
botao.pack(pady=20)


resultado = ctk.CTkLabel(janela,
                               text='R$ 0,00',
                               font=('verdana',25),
                               text_color='green')
resultado.pack(pady=20)


janela.mainloop()