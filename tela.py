from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class principal:

    wr_escolhe_temp: Combobox

    def __init__(self, janela=None):
        self.janela = Label(janela, text="Bem Vindo a sua Cervejeira")

        self.lb_telainicial = Label(janela, text="Bem Vindo a sua Cervejeira!!", font="Arial 20")
        self.lb_telainicial.place(x=220, y=70)

        self.btreceita = Button(janela, text="Receitas", width=40, height=5, command=self.Receitas)
        self.btreceita.place(x=50, y=150)

        self.btconexao = Button(janela, text="Login APP", width=40, height=5)
        self.btconexao.place(x=450, y=150)

    def Receitas(self):
        rec = Tk()
        rec.title("Automação Brassagem e Fervura")
        self.lb_rec = Label(rec, text="Menu de Receitas", font="Arial 20")
        self.lb_rec.place(x=300, y=70)
        self.bt_novareceita = Button(rec, text="Programar Receita", width=40, height=5, command=self.receita_nova)
        self.bt_novareceita.place(x=50, y=150)
        self.bt_rec_return = Button(rec, text="Voltar", width=40, height=5, command=rec.destroy)
        self.bt_rec_return.place(x=450, y=150)
        rec.geometry("800x480+200+200")

    def receita_nova(self):
        rec_nova = Tk()
        rec_nova.title("Automação Brassagem e Fervura")
        self.lb_rec_nova = Label(rec_nova, text="Cadastro de Receitas", font="Arial 20")
        self.lb_rec_nova.place(x=270, y=70)
        self.lb_qtde_rampas = Label(rec_nova, text="Qual a quantidade de rampas?", font="Arial 15")
        self.lb_qtde_rampas.place(x=120, y=180)
        self.wr_qtde_rampas = ttk.Combobox(rec_nova, width=20)
        self.wr_qtde_rampas['values'] = ("1", "2", "3", "4", "5", "6", "7")
        self.wr_qtde_rampas.place(x=400, y=195)
        
        self.bt_confirma_recnova = Button(rec_nova, text="Confirmar", width=40, height=5, command=self.conf_rampas)
        self.bt_confirma_recnova.place(x=150, y=300)
        self.bt_cancela_recnova = Button(rec_nova, text="Cancelar", width=30, height=5, command=rec_nova.destroy)
        self.bt_cancela_recnova.place(x=450, y=300)
        rec_nova.geometry("800x480+200+200")

    def conf_rampas(self):
        conf_rampas = Tk()
        conf_rampas.title("Automação Brassagem e Fervura")
        self.lb_conf_ramp = Label(conf_rampas, text="Cadastre sua receita", font="Arial 20")
        self.lb_conf_ramp.place(x=270, y=70)
                    
        self.lb_rampa1=Label(conf_rampas,text="Temperatura Rampa 1: ",font="Arial 15")
        self.lb_rampa1.place(x=180,y=120)
        self.wr_escolhe_temp = ttk.Combobox(conf_rampas, width=20)
        self.wr_escolhe_temp['values'] = ("45ºC", "46ºC", "47ºC", "48ºC", "49ºC", "50ºC", "51ºC", "52ºC", "53ºC", "54ºC", "55ºC", "56ºC", "57ºC", "58ºC", "59ºC", "60ºC", "61ºC", "62ºC", "63ºC", "64ºC", "65ºC", "66ºC", "67ºC", "68ºC", "69ºC","70ºC","71ºC","72ºC","73ºC","74ºC","75ºC","76ºC","77ºC","78ºC","79ºC","80ºC","81ºC","82ºC","83ºC","84ºC","85ºC")
        self.wr_escolhe_temp.place(x=400, y=125)
        self.lb_rampa_tempo1=Label(conf_rampas,text="Tempo para Rampa 1: ",font="Arial 15")
        self.lb_rampa_tempo1.place(x=180,y=150)
        self.wr_seleciona_tempo = ttk.Combobox(conf_rampas, width=20)
        self.wr_seleciona_tempo['values'] = ("5min", "10min", "15min","20min", "25min", "30min", "35min", "40min", "45min", "50min", "55min", "60min", "65min", "70min", "75min", "80min", "85min", "90min", "95min", "100min")
        self.wr_seleciona_tempo.place(x=400, y=155)
        self.bt_confirma_temp = Button(conf_rampas, text="Confirmar", width=40, height=5, command=self.conf_fervura)
        self.bt_confirma_temp.place(x=150, y=300)
        self.bt_cancela_rampas = Button(conf_rampas, text="Cancelar", width=30, height=5, command=conf_rampas.destroy)
        self.bt_cancela_rampas.place(x=450, y=300)
        conf_rampas.geometry("800x480+200+200")

    def conf_fervura(self):
        conf_fervura = Tk()
        conf_fervura.title("Automação Brassagem e Fervura")
        self.lb_conf_fervura = Label(conf_fervura, text="Configure a fervura", font="Arial 20")
        self.lb_conf_fervura.place(x=270, y=70)
        self.lb_conf_fervura_combo=Label(conf_fervura,text="Tempo de fervura: ",font="Arial 15")
        self.lb_conf_fervura_combo.place(x=180,y=120)
        self.wr_seleciona_fervura = ttk.Combobox(conf_fervura, width=20)
        self.wr_seleciona_fervura['values'] = ("5min", "10min", "15min","20min", "25min", "30min", "35min", "40min", "45min", "50min", "55min", "60min", "65min", "70min", "75min", "80min", "85min", "90min", "95min", "100min")
        self.wr_seleciona_fervura.place(x=400, y=125)
        self.wr_qtde_lupulo= ttk.Combobox(conf_fervura, width=20)
        self.lb_conf_fervura_combo=Label(conf_fervura,text="Quantidade lupulos: ",font="Arial 15")
        self.lb_conf_fervura_combo.place(x=180,y=150)
        self.wr_qtde_lupulo['values'] = ("1", "2", "3", "4", "5", "6", "7")
        self.wr_qtde_lupulo.place(x=400, y=155)
        self.bt_confirma_temp = Button(conf_fervura, text="Confirmar", width=40, height=5)
        self.bt_confirma_temp.place(x=150, y=300)
        self.bt_cancela_rampas = Button(conf_fervura, text="Cancelar", width=30, height=5, command=conf_fervura.destroy)
        self.bt_cancela_rampas.place(x=450, y=300)
        conf_fervura.geometry("800x480+200+200")
        
        


root = Tk()
root.title("Automação Brassagem e Fervura")
principal(root)

# imagem = PhotoImage(file="TelaIHM.png")
# img = Label(root, image=imagem)
# img.imagem = imagem
# img.place(x=0, y=0)

margem = Label(root, height=7)
margem.pack(anchor=W)

root.geometry("800x480+200+200")
root.mainloop()
