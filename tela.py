from tkinter import *
from tkinter import ttk

class principal:

    def __init__(self,janela=None):
        
        
        self.janela=Label(janela,text= "Bem Vindo a sua Cervejeira") 

        self.lb_telainicial=Label(janela, text = "Bem Vindo a sua Cervejeira!!", font= "Arial 20")
        self.lb_telainicial.place(x=220,y=70)
        
        self.btreceita = Button(janela, text="Receitas", width=40, height= 5,command= self.Receitas)
        self.btreceita.place(x=50, y=150)       

        self.btconexao = Button(janela, text="Login APP", width=40,height= 5)
        self.btconexao.place(x=450, y=150)

    
    def Receitas(self):

        rec=Tk()
        self.lb_rec=Label(rec, text="Menu de Receitas", font="Arial 20")
        self.lb_rec.place(x = 300, y= 70)
        self.bt_novareceita=Button(rec, text="Cadastrar Nova Receita", width=40,height=5,command= self.receita_nova)
        self.bt_novareceita.place(x = 50, y = 150)
        self.bt_rec_cadastradas=Button(rec, text="Receitas Cadastradas", width=40, height=5)
        self.bt_rec_cadastradas.place(x=450,y=150)
        self.bt_rec_return=Button(rec, text="Voltar", width=40, height=5, command= rec.destroy)
        self.bt_rec_return.place(x=250,y=350)   
        rec.geometry("800x480+200+200")
        
    def receita_nova(self):

        rec_nova=Tk()
        self.lb_rec_nova=Label(rec_nova, text="Cadastro de Receitas", font="Arial 20")  
        self.lb_rec_nova.place(x=270,y=70)        
        self.lb_qtde_rampas=Label(rec_nova, text="Qual a quantidade de rampas?", font="Arial 15")
        self.lb_qtde_rampas.place(x=120,y=180)
        self.wr_qtde_rampas=ttk.Combobox(rec_nova,width=20)
        self.wr_qtde_rampas['values'] = ("1","2","3","4","5","6","7")
        self.wr_qtde_rampas.place(x=400,y=190)
        self.bt_confirma_recnova=Button(rec_nova, text="Confirmar", width=40, height=5,command=self.conf_rampas)
        self.bt_confirma_recnova.place(x=150,y=300)
        self.bt_cancela_recnova=Button(rec_nova, text="Cancelar", width=30, height=5,command=rec_nova.destroy)
        self.bt_cancela_recnova.place(x=450,y=300)
        rec_nova.geometry("800x480+200+200")

    def conf_rampas(self):
    	conf_rampa=Tk()
    	if self.wr_qtde_rampas == 1:
    		self.temp=Label(conf_rampa,text="Qual a temperatura?",font="Arial 15")
    		self.vtemp=ttk.Combobox(conf_rampa, width=20)
    		self.vtemp['values'] = ("40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76")
    	conf_rampa.geometry("800x480+200+200")


root = Tk()
principal(root)

imagem = PhotoImage(file="TelaIHM.png")
img = Label(root, image=imagem)
img.imagem = imagem
img.place(x=0, y=0)

margem = Label(pri, height=7)
margem.pack(anchor=W)

root.geometry("800x480+200+200")
root.mainloop()


        







