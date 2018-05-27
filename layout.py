"""Layout game."""
from tkinter import (Label, Button, Entry, SUNKEN, Tk, PhotoImage)
from tkinter import (TOP, LEFT, RIGHT)
import motor

game = motor.Entrada()
# pyinstaller --onefile --noconsole nome.py  comando gerar executavel


def bt_npc_click():
    """botão chama função que gera numero para ser descoberto."""
    game.dados_npc()
    lb_npc['text'] = 'Número gerado! Boa Sorte!'


def bt_player_click():
    """
    botão player.

    Número digitado pelo player é verificado se está nas condições.
    do jogo e chama função para ver se houve acerto.
    """
    if game.npc != 0:
        if ed_num.get() != '' and str.isnumeric(ed_num.get()):
            num_player = int(ed_num.get())
            if 999 < num_player < 10000:
                print('número aceito')
                resultado = game.compara_numero(num_=num_player)
                if resultado == 'Você Acertou':
                    lb_resultado['text'] = resultado
                else:
                    acertos = resultado.count('correto')
                    l_errado = resultado.count('local_errado')
                    lb_resultado['text'] = f'{acertos} números estão'
                    'certos e no local certo\n'
                    f'{l_errado} números estão corretos mas no local errado.'
                    print(resultado)
            else:
                lb_resultado['text'] = 'Número não contém 4 dígitos!'
                'digite novamente'
                ed_num.delete(0, len(ed_num.get()))
        else:
            lb_resultado['text'] = 'Digite um número com 4 dígitos'
            ed_num.delete(0, len(ed_num.get()))
    else:
        lb_resultado['text'] = 'Falta gerar número npc!'


def instrucao_popup():
    """Cria popup com instruções do game."""
    popup = Tk()
    popup.wm_title('Instruções')
    lb_instrucoes = Label(popup, font=('Helvetica', 15, 'bold'), text='''Instruções
    O game sorteia um número de 4 digítos
    O jogador deve tentar acertar este número
    conforme as tentativas do jogador o game retornara mensagens:
    correto - quando o jogador acertou 1 número e a posição que eles está
    local_errado - acertou o número porém no local errado
    bagels - se nenhum dígito está correto.
    Boa Sorte!!!
    ''')
    lb_instrucoes.pack(side=TOP, fill='x', pady=20, padx=10)
    bt_ok = Button(popup, text='OK', command=popup.destroy, width=10)
    bt_ok.pack()
    popup.mainloop()


janela = Tk()
janela.title('Game! Adivinhe o número.')

lb_branco1 = Label(janela, pady=1, bg='black', fg='white',
                   font=('Verdana', 10, 'bold'))
lb_branco1.pack(side=TOP)

lb_npc = Label(janela, text='Bem vindo ao game Bagels\nAguardando número',
               pady=30, bg='black', fg='grey', font=('Verdana', 15, 'bold'),
               relief=SUNKEN, borderwidth=10, width=25, height=2)
# lb_npc.place(x=0, y=70)
lb_npc.pack(side=TOP)

lb_branco1 = Label(janela, pady=1, bg='black', fg='white',
                   font=('Verdana', 10, 'bold'))
lb_branco1.pack(side=TOP)

imagem_npc = PhotoImage(file=r'artes\imagembotao.png')
bt_npc = Button(janela, text='Gerar Número NPC', command=bt_npc_click,
                bg='black', fg='white', compound=LEFT,
                font=('Verdana', 10, 'bold'), width=220, height=70,
                image=imagem_npc)
# bt_npc.place(x=180, y=100)
bt_npc.pack(side=TOP)

lb_branco1 = Label(janela, pady=5, bg='black', fg='white',
                   font=('Verdana', 10, 'bold'))
lb_branco1.pack(side=TOP)

lb_num = Label(janela, text='Entre com um número 4 dígitos (xxxx)', pady=10,
               bg='black', fg='white', font=('Verdana', 10, 'bold'))
# lb_num.place(y=170)
lb_num.pack(side=TOP)
ed_num = Entry(janela, width=30, font=20)
# ed_num.place(x=100, y=170)
ed_num.pack(side=TOP)

lb_branco1 = Label(janela, pady=1, bg='black', fg='white',
                   font=('Verdana', 10, 'bold'))
lb_branco1.pack(side=TOP)

imagem_play = PhotoImage(file='artes\imagembotaoplay.png')
bt_player = Button(janela, text='Adivinhar', command=bt_player_click,
                   bg='black', fg='white', font=('Verdana', 10, 'bold'),
                   compound=LEFT, width=220, height=70, image=imagem_play)
# bt_player.place(x=180, y=200)
bt_player.pack(side=TOP)

lb_branco1 = Label(janela, pady=5, bg='black', fg='white',
                   font=('Verdana', 10, 'bold'))
lb_branco1.pack(side=TOP)

lb_resultado = Label(janela, text='Bem vindo ao game Bagels', pady=30,
                     relief=SUNKEN, padx=10, font=('Verdana', 13, 'bold'),
                     fg='grey', bg='black', borderwidth=10, width=38, height=2)
# lb_resultado.place(x=100, y=250)
lb_resultado.pack(side=TOP)

bt_instrucao = Button(janela, width=20, text='Instruções',
                      command=instrucao_popup, bg='black', fg='white',
                      font=('Verdana', 10, 'bold'))
bt_instrucao.pack(side=RIGHT)

janela.configure(bg='black')
janela.geometry('550x650')
janela.mainloop()
