
#tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()


#dividir a tela em 2
class Applications():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title('CONTADOR YUGIOH')
        self.root.configure(background= '#00BFFF')
        self.root.geometry('900x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=1300, height=1000)
        self.root.minsize(width=400, height=300)
#contador de vida (8000)
    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#F0E68C', highlightbackground= '#FFDAB9',
                            highlightthickness=6)
        self.frame1.place(relx=0.1, rely=0.1, relheight=0.81, relwidth=0.3)

        self.frame2 = Frame(self.root, bd=4, bg='#F0E68C', highlightbackground= '#FFDAB9',
                            highlightthickness=6)
        self.frame2.place(relx=0.6, rely=0.1, relheight=0.81, relwidth=0.3)
#-------------------------------------------------------------------------------------------#
    
#-------------------------------------------------------------------------------------------#
    def botoes(self):

         self.contador1_entry = Entry(self.frame1,justify=CENTER, font=('Roman', 50, 'bold'), bd= 4)
         self.contador1_entry.place(relx=0.01, rely=0.01, relheight=0.2, relwidth=0.99)
         self.contador1_entry.insert(0, 8000)           

         self.contador2_entry = Entry(self.frame2,justify='center', font=('Roman', 50, 'bold'), bd= 4)
         self.contador2_entry.place(relx=0.01, rely=0.01, relheight=0.2, relwidth=0.99)
         self.contador2_entry.insert(0, 8000)
         
         self.lb_turno = Label(self.root, relief= RIDGE, text=' TURNO ', font=('MS Sans Serif', 25, 'bold'), bg= '#DAA520')
         self.lb_turno.place(relx=0.4, rely=0.001, relheight=0.1, relwidth=0.2)
         self.turno_entry = Entry(self.root, font=('MS Sans Serif', 25, 'bold'), justify= CENTER)
         self.turno_entry.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.2)
         self.turno_entry.insert(0, 1)

         self.lb_player1 = Label(self.root, relief=RIDGE, text='PLAYER 1', font=('Segoe UI Symbol', 25, 'bold'), bg= '#FF6347')
         self.lb_player1.place(relx=0.15, rely=0.001, relheight=0.1, relwidth=0.2)
        
         self.lb_player2 = Label(self.root, relief=RIDGE, text='PLAYER 2', font=('MS Sans Serif', 25, 'bold'), bg= '#7FFF00')
         self.lb_player2.place(relx=0.65, rely=0.001, relheight=0.1, relwidth=0.2)

#botoes: 
  #passar turno
         self.bt_turno = Button(self.frame1, text='Passar turno', bd=4, bg='#FFEBCD',
                                font=('courier', 20, 'italic', 'bold'), command= self.muda_turno)
         self.bt_turno.place(relx=0.06, rely=0.25, relheight=0.1, relwidth=0.9)

         self.bt_turno = Button(self.frame2, text='Passar turno', bd=4, bg='#FFEBCD',
                                font=('courier', 20, 'italic', 'bold'), command= self.muda_turno)
         self.bt_turno.place(relx=0.06, rely=0.25, relheight=0.1, relwidth=0.9)
  
  #digite o dano
         self.bt_danop1 = Button(self.frame1, text= 'DANO', bd=4, bg='#FFEBCD',
                                 font=('courier', 20, 'italic', 'bold'), command=self.attack1)
         self.bt_danop1.place(relx=0.06, rely=0.5, relheight=0.1, relwidth=0.9)
         self.danop1_entry = Entry(self.frame1, justify=CENTER, font=('Roman', 25, 'bold'), bd= 4)
         self.danop1_entry.place(relx=0.06, rely=0.39, relheight=0.1, relwidth=0.9)

         self.bt_danop2 = Button(self.frame2, text= 'DANO', bd=4, bg='#FFEBCD',
                                 font=('courier', 20, 'italic', 'bold'), command=self.attack2)
         self.bt_danop2.place(relx=0.06, rely=0.5, relheight=0.1, relwidth=0.9)
         self.danop2_entry = Entry(self.frame2, justify=CENTER, font=('Roman', 25, 'bold'), bd= 4)
         self.danop2_entry.place(relx=0.06, rely=0.39, relheight=0.1, relwidth=0.9)
  #pagar metade da vida
         self.metade_vidap1 = Button(self.frame1, text='Pagar Metade\n da Vida', bd=4, bg='#FFEBCD',
                                   font=('courier', 15, 'italic', 'bold'), command= self.vida_metade1)
         self.metade_vidap1.place(relx=0.06, rely=0.9, relheight=0.1, relwidth=0.9)

         self.metade_vidap2 = Button(self.frame2, text='Pagar Metade\n da Vida', bd=4, bg='#FFEBCD',
                                   font=('courier', 15, 'italic', 'bold'), command= self.vida_metade2)
         self.metade_vidap2.place(relx=0.06, rely=0.9, relheight=0.1, relwidth=0.9)
  #digite quanto de cura se ganhou
         self.bt_curap1 = Button(self.frame1, text='Curar', bd=4, bg='#FFEBCD',
                                 font=('courier', 15, 'italic', 'bold'), command=self.cura1)
         self.bt_curap1.place(relx=0.06, rely=0.75, relheight=0.1, relwidth=0.9)
         self.curap1_entry = Entry(self.frame1, justify=CENTER, font=('Roman', 25, 'bold'), bd= 4)
         self.curap1_entry.place(relx=0.06, rely=0.64, relheight=0.1, relwidth=0.9)

         self.bt_curap2 = Button(self.frame2, text='Curar', bd=4, bg='#FFEBCD',
                                 font=('courier', 15, 'italic', 'bold'), command=self.cura2)
         self.bt_curap2.place(relx=0.06, rely=0.75, relheight=0.1, relwidth=0.9)
         self.curap2_entry = Entry(self.frame2, justify=CENTER, font=('Roman', 25, 'bold'), bd= 4)
         self.curap2_entry.place(relx=0.06, rely=0.64, relheight=0.1, relwidth=0.9)

#passar turno
    def muda_turno(self):
        turno = int(self.turno_entry.get())
        turno = turno + 1
        self.turno_entry.delete(0, END)
        self.turno_entry.insert(0, f'{turno}')
        
#diminuir a vida do oponente
    def attack1(self):
        numero = int(self.danop1_entry.get())
        vida = int(self.contador2_entry.get())
        
        vida = vida - numero
        self.danop1_entry.delete(0, END)
        self.contador2_entry.delete(0, END)
        self.contador2_entry.insert(0, f'{vida:.0f}')
        if vida >= 1:
            pass
        elif vida <= 0:
            self.danop1_entry.delete(0, END)
            self.contador2_entry.delete(0, END)
            self.contador2_entry.insert(0, '0')
            messagebox.showinfo('PARABÉNS', '\nJOGADOR 1 VENCEU!')

    def attack2(self):
        numero = int(self.danop2_entry.get())
        vida = int(self.contador1_entry.get())
        
        vida = vida - numero
        self.danop2_entry.delete(0, END)
        self.contador1_entry.delete(0, END)
        self.contador1_entry.insert(0, f'{vida:.0f}')
        if vida >= 1:
            pass
        elif vida <= 0:
            self.danop2_entry.delete(0, END)
            self.contador1_entry.delete(0, END)
            self.contador1_entry.insert(0, '0')
            messagebox.showinfo('PARABÉNS', '\nJOGADOR 2 VENCEU!')

#curar a propria vida
    def cura1(self):
        cura = int(self.curap1_entry.get())
        vida = int(self.contador1_entry.get())
        vida = vida + cura
        self.contador1_entry.delete(0, END)
        self.curap1_entry.delete(0, END)
        self.contador1_entry.insert(0, f'{vida:.0f}')

    def cura2(self):
        cura = int(self.curap2_entry.get())
        vida = int(self.contador2_entry.get())
        vida = vida + cura
        self.curap1_entry.delete(0, END)
        self.contador2_entry.delete(0, END)
        self.contador2_entry.insert(0, f'{vida:.0f}')
#cortar a propria vida pela metade
    def vida_metade1(self):
        vida = float(self.contador1_entry.get())
        vida = vida/2
        self.contador1_entry.delete(0, END)
        self.contador1_entry.insert(0, f'{vida:.0f}')

    #-------------------------------------------------------------------------------#
    def vida_metade2(self):
        vida = float(self.contador2_entry.get())
        vida = vida/2
        self.contador2_entry.delete(0, END)
        self.contador2_entry.insert(0, f'{vida:.0f}')



    



Applications()