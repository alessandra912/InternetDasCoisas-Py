import customtkinter as ctk
import webbrowser
import os
#Nome biblioteca: pip install auto-py-to-exe

#FUNÇÃO
def tela_azul():
    janela2 = ctk.CTkToplevel()
    janela2.attributes('-fullscreen', True)
    janela2.configure(fg_color='#0078d7')

    mensagem = """
    :(

    Seu dispositivo encontrou um problema e precisa ser reiniciado.
    Estamos coletando algumas informações sobre o erro e, em seguida,
    reiniciaremos para você.

    100% concluído

    Para obter mais informações sobre esse problema e possíveis correções,
    visite https://www.windows.com/stopcode

    Se você ligar para uma pessoa de suporte, forneça estas informações:
    Código de parada: CRITICAL_PROCESS_DIED"""

    texto = ctk.CTkLabel(janela2,
                        text=mensagem,
                        font=('Arial', 25),
                        justify='left',
                        text_color='white')
    texto.pack(expand=True)


def reiniciar():
    os.system('shutdown /r /t 0')

def desligar():
    os.system('shutdown /s /t 0')

def google():
    webbrowser.open('http://www.google.com')

def calculadora():
    os.system('calc')

def bloquear():
    os.system('rundll32.exe user32.dll, LockWorkStation')



ctk.set_appearance_mode('light')

#JANELA
janela = ctk.CTk()
janela.geometry('300x410')
janela.title('Bomba Patch 2026')


#AQUI COMEÇA OS ELEMENTOS DA JANELA
bt01 = ctk.CTkButton(janela,
                     text='Desligar',
                     fg_color='darkblue',
                     text_color='white',
                     width=200,
                     height=20,
                     font=('Verdana', 30),
                     command=desligar)
bt01.pack(pady=20)


bt02 = ctk.CTkButton(janela,
                     text='Reiniciar',
                     fg_color='darkblue',
                     text_color='white',
                     width=200,
                     height=20,
                     font=('Verdana', 30),
                     command=reiniciar)
bt02.pack()


bt03 = ctk.CTkButton(janela,
                     text='Bloquear',
                     fg_color='darkblue',
                     text_color='white',
                     width=200,
                     height=20,
                     font=('Verdana', 30),
                     command=bloquear)
bt03.pack(pady=20)


bt04 = ctk.CTkButton(janela,
                     text='Calculadora',
                     fg_color='darkblue',
                     text_color='white',
                     width=200,
                     height=20,
                     font=('Verdana', 30),
                     command=calculadora)
bt04.pack()


bt05 = ctk.CTkButton(janela,
                     text='Google',
                     fg_color='darkblue',
                     text_color='white',
                     width=200,
                     height=20,
                     font=('Verdana', 30),
                     command=google)
bt05.pack(pady=20)


bt06 = ctk.CTkButton(janela,
                     text='Não Clique Aqui 😮',
                     fg_color='red',
                     text_color='white',
                     width=200,
                     height=20,
                     font=('Verdana', 28),
                     command=tela_azul)
bt06.pack()


janela.mainloop()