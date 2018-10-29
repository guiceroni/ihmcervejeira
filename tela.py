from tkinter import *
from tkinter import ttk


limite = 1
limite_max =95
limite_rampas=3
limite_lupulo=2

class principal:

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

    def bt_soma(self):
        
        rampa =int(self.lb_rp["text"])
        rampa = rampa + 1
        if rampa >= 3:
            rampa = limite_rampas
        
        self.lb_rp["text"] = int(rampa)

        arq = open("rampas.txt", "w")
        arq.write(str(rampa))
        arq.close()
        print(rampa)

    def bt_subtracao(self):
        
        rampa =int(self.lb_rp["text"])
        rampa = rampa -1 
        if rampa <= limite:
            rampa = limite
        self.lb_rp["text"] = int(rampa)

        arq = open("rampas.txt", "w")
        arq.write(str(rampa))
        arq.close()
        print(rampa)

    def bt_soma_temp1(self):
        
        temperatura =int(self.lb_temp["text"])
        temperatura = temperatura + 5
        if temperatura >= 95:
            temperatura = 95
        self.lb_temp["text"] = int(temperatura)

        arq = open("temperatura1.txt", "w")
        arq.write(str(temperatura))
        arq.close()
        print(temperatura)

    def bt_subtracao_temp1(self):
        
        temperatura =int(self.lb_temp["text"])
        temperatura = temperatura - 5
        if temperatura <= 0:
            temperatura = 0
        self.lb_temp["text"] = int(temperatura)

        arq = open("temperatura1.txt", "w")
        arq.write(str(temperatura))
        arq.close()
        print(temperatura)

    def bt_soma_temp2(self):
        
        temperatura2 =int(self.lb_temp2["text"])
        temperatura2 = temperatura2 + 5
        if temperatura2 >= 95:
            temperatura2 = 95
        self.lb_temp2["text"] = int(temperatura2)

        arq = open("temperatura2.txt", "w")
        arq.write(str(temperatura2))
        arq.close()
        print(temperatura2)

    def bt_subtracao_temp2(self):
        
        temperatura2 =int(self.lb_temp2["text"])
        temperatura2 = temperatura2 - 5
        if temperatura2 <= 0:
            temperatura2 = 0
        self.lb_temp2["text"] = int(temperatura2)

        arq = open("temperatura2.txt", "w")
        arq.write(str(temperatura2))
        arq.close()
        print(temperatura2)

    def bt_soma_temp3(self):
        
        temperatura3 =int(self.lb_temp3["text"])
        temperatura3 = temperatura3 + 5
        if temperatura3 >= 95:
            temperatura3 = 95
        self.lb_temp3["text"] = int(temperatura3)

        arq = open("temperatura3.txt", "w")
        arq.write(str(temperatura3))
        arq.close()
        print(temperatura3)

    def bt_subtracao_temp3(self):
        
        temperatura3 =int(self.lb_temp3["text"])
        temperatura3 = temperatura3 - 5
        if temperatura3 <= 0:
            temperatura3 = 0 
        self.lb_temp3["text"] = int(temperatura3)

        arq = open("temperatura3.txt", "w")
        arq.write(str(temperatura3))
        arq.close()
        print(temperatura3)

    def bt_soma_time1(self):
        
        tempo =int(self.lb_tempo["text"])
        tempo = tempo + 5
        if tempo >= 95:
            tempo = 95
        self.lb_tempo["text"] = int(tempo)

        arq = open("tempo1.txt", "w")
        arq.write(str(tempo))
        arq.close()
        print(tempo)

    def bt_subtracao_time1(self):
        
        tempo =int(self.lb_tempo["text"])
        tempo = tempo - 5
        if tempo <= 0:
            tempo = 0
        self.lb_tempo["text"] = int(tempo)

        arq = open("tempo1.txt", "w")
        arq.write(str(tempo))
        arq.close()
        print(tempo)

    def bt_soma_time2(self):
        
        tempo2 =int(self.lb_tempo2["text"])
        tempo2 = tempo2 + 5
        if tempo2 >= 95:
            tempo2 = 95
        self.lb_tempo2["text"] = int(tempo2)

        arq = open("tempo2.txt", "w")
        arq.write(str(tempo2))
        arq.close()
        print(tempo2)

    def bt_subtracao_time2(self):
        
        tempo2 =int(self.lb_tempo2["text"])
        tempo2 = tempo2 - 5
        if tempo2 <= 0:
            tempo2 = 0
        self.lb_tempo2["text"] = int(tempo2)
        
        
        arq = open("tempo2.txt", "w")
        arq.write(str(tempo2))
        arq.close()
        print(tempo2)
        

    def bt_soma_time3(self):
        
        tempo3 =int(self.lb_tempo3["text"])
        tempo3 = tempo3 + 5
        if tempo3 >= 95:
            tempo3 = 95
        self.lb_tempo3["text"] = int(tempo3)

        arq = open("tempo3.txt", "w")
        arq.write(str(tempo3))
        arq.close()
        print(tempo3)

    def bt_subtracao_time3(self):
        
        tempo3 =int(self.lb_tempo3["text"])
        tempo3 = tempo3 - 5
        if tempo3 <= 0:
            tempo3 = 0
        self.lb_tempo3["text"] = int(tempo3)

        arq = open("tempo3.txt", "w")
        arq.write(str(tempo3))
        arq.close()
        print(tempo3)


    def bt_soma_fervura(self):

         
        fervura =int(self.lb_fervura["text"])
        fervura = fervura + 5
        if fervura >= 95:
            fervura = 95
        self.lb_fervura["text"] = int(fervura)

        arq = open("fervura.txt", "w")
        arq.write(str(fervura))
        arq.close()
        print(fervura)

    def bt_subtracao_fervura(self):
        
        fervura =int(self.lb_fervura["text"])
        fervura = fervura - 5
        if fervura <= 0:
            fervura = 0            
        self.lb_fervura["text"] = int(fervura)

        arq = open("fervura.txt", "w")
        arq.write(str(fervura))
        arq.close()
        print(fervura)
    

    def bt_soma_lupulo1(self):
        
        lupulo1 =int(self.lb_lupulo1["text"])
        lupulo1 = lupulo1 + 1
        if lupulo1 >= 2:
        	lupulo1 = limite_lupulo
        self.lb_lupulo1["text"] = int(lupulo1)

        arq = open("lupulo1.txt", "w")
        arq.write(str(lupulo1))
        arq.close()
        

    def bt_subtracao_lupulo1(self):
        
        lupulo1 =int(self.lb_lupulo1["text"])
        lupulo1 = lupulo1 - 1
        if lupulo1 <= 1:
            lupulo1 = 1
        self.lb_lupulo1["text"] = int(lupulo1)

        arq = open("lupulo1.txt", "w")
        arq.write(str(lupulo1))
        arq.close()
        print(lupulo1)


    def bt_soma_timelup1(self):
        
        tempolup1 =int(self.lb_tempolup1["text"])
        tempolup1 = tempolup1 + 5
        if tempolup1 >= 95:
            tempolup1 = 95

        self.lb_tempolup1["text"] = int(tempolup1)

        arq = open("tempolup1.txt", "w")
        arq.write(str(tempolup1))
        arq.close()
        print(tempolup1)

    def bt_subtracao_timelup1(self):
        
        tempolup1 =int(self.lb_tempolup1["text"])
        tempolup1 = tempolup1 - 5
        if tempolup1 <= 0:
            tempolup1 = 0
            
        self.lb_tempolup1["text"] = int(tempolup1)        

        arq = open("tempolup1.txt", "w")
        arq.write(str(tempolup1))
        arq.close()
        print(tempolup1)

    def bt_soma_timelup2(self):
        
        tempolup2 =int(self.lb_tempolup2["text"])
        tempolup2 = tempolup2 + 5
        if tempolup2 >= 95:
            tempolup2 = 95
        self.lb_tempolup2["text"] = int(tempolup2)        
        
        arq = open("tempolup2.txt", "w")
        arq.write(str(tempolup2))
        arq.close()
        print(tempolup2)

    def bt_subtracao_timelup2(self):
        
        tempolup2 =int(self.lb_tempolup2["text"])
        tempolup2 = tempolup2 - 5
        if tempolup2 <= 0:
            tempolup2 = 0
        self.lb_tempolup2["text"] = int(tempolup2)     
        

        arq = open("tempolup2.txt", "w")
        arq.write(str(tempolup2))
        arq.close()
        print(tempolup2)



    def receita_nova(self):
        rec_nova = Tk()
        rec_nova.title("Automação Brassagem e Fervura")        
        self.lb_rec_nova = Label(rec_nova, text="Cadastro de Receitas", font="Arial 20")
        self.lb_rec_nova.place(x=270, y=70)
        self.lb_qtde_rampas = Label(rec_nova, text="Qual a quantidade de rampas?", font="Arial 15")
        self.lb_qtde_rampas.place(x=140, y=150)
        
        self.lb_rp = Label(rec_nova,text="1",font="Arial 70", fg= "black")
        self.lb_rp.place(x=330, y=180)
            

        self.bt_soma_rp = Button(rec_nova, width=6, height =4, text="+", command= self.bt_soma)
        self.bt_soma_rp.place(x=450, y=200)
        
        self.bt_subtracao_rp = Button(rec_nova, width=6, height=4, text="-", command= self.bt_subtracao)
        self.bt_subtracao_rp.place(x=520, y=200)       
        
        self.bt_confirma_recnova = Button(rec_nova, text="Confirmar", width=40, height=5, command=self.conf_rampas)
        self.bt_confirma_recnova.place(x=150, y=300)
        self.bt_cancela_recnova = Button(rec_nova, text="Cancelar", width=30, height=5, command=rec_nova.destroy)
        self.bt_cancela_recnova.place(x=450, y=300)
                              
        rec_nova.geometry("800x480+200+200")

    def conf_rampas(self):
        rampa = open("rampas.txt")
        conf_rampa = int(rampa.read())
        
        print(conf_rampa)
                     
        conf_rampas = Tk()        
        conf_rampas.title("Automação Brassagem e Fervura")
        self.lb_conf_ramp = Label(conf_rampas, text="Cadastre sua receita", font="Arial 20")
        self.lb_conf_ramp.place(x=270, y=70)
       
        if conf_rampa == 1:
            self.lb_rampa1=Label(conf_rampas,text="Temperatura Rampa 1: ",font="Arial 15")
            self.lb_rampa1.place(x=180,y=140)            
            self.lb_temp = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_temp.place(x=400, y=140)
            self.bt_soma_temp = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_temp1)
            self.bt_soma_temp.place(x=440, y=140)        
            self.bt_subtracao_temp = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_temp1)
            self.bt_subtracao_temp.place(x=500, y=140)            
            self.lb_rampa_tempo1=Label(conf_rampas,text="Tempo Rampa 1(min): ",font="Arial 15")
            self.lb_rampa_tempo1.place(x=180,y=190)
            self.lb_tempo = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_tempo.place(x=400, y=190)
            self.bt_soma_tempo = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_time1)
            self.bt_soma_tempo.place(x=440, y=190)        
            self.bt_subtracao_tempo = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_time1)
            self.bt_subtracao_tempo.place(x=500, y=190)
            
        elif conf_rampa == 2:
            self.lb_rampa1=Label(conf_rampas,text="Temperatura Rampa 1: ",font="Arial 15")
            self.lb_rampa1.place(x=40,y=140)            
            self.lb_temp = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_temp.place(x=260, y=140)
            self.bt_soma_temp = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_temp1)
            self.bt_soma_temp.place(x=300, y=140)        
            self.bt_subtracao_temp = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_temp1)
            self.bt_subtracao_temp.place(x=340, y=140)            
            self.lb_rampa_tempo1=Label(conf_rampas,text="Tempo Rampa 1(min): ",font="Arial 15")
            self.lb_rampa_tempo1.place(x=400,y=140)
            self.lb_tempo = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_tempo.place(x=620, y=140)
            self.bt_soma_tempo = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_time1)
            self.bt_soma_tempo.place (x=660, y=140)      
            self.bt_subtracao_tempo = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_time1)
            self.bt_subtracao_tempo.place(x=700, y=140)

            self.lb_rampa2=Label(conf_rampas,text="Temperatura Rampa 2: ",font="Arial 15")
            self.lb_rampa2.place(x=40,y=190)           
            self.lb_temp2 = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_temp2.place(x=260, y=190)
            self.bt_soma_temp2 = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_temp2)
            self.bt_soma_temp2.place(x=300, y=190)        
            self.bt_subtracao_temp2 = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_temp2)
            self.bt_subtracao_temp2.place (x=340, y=190)           
            self.lb_rampa_tempo2=Label(conf_rampas,text="Tempo Rampa 2(min): ",font="Arial 15")
            self.lb_rampa_tempo2.place(x=400,y=190)
            self.lb_tempo2 = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_tempo2.place(x=620, y=190)
            self.bt_soma_tempo2 = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_time2)
            self.bt_soma_tempo2.place(x=660, y=190)        
            self.bt_subtracao_tempo2 = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_time2)
            self.bt_subtracao_tempo2.place(x=700, y=190)

        elif conf_rampa == 3:
            self.lb_rampa1=Label(conf_rampas,text="Temperatura Rampa 1: ",font="Arial 15")
            self.lb_rampa1.place(x=40,y=140)            
            self.lb_temp = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_temp.place(x=260, y=140)
            self.bt_soma_temp = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_temp1)
            self.bt_soma_temp.place(x=300, y=140)        
            self.bt_subtracao_temp = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_temp1)
            self.bt_subtracao_temp.place(x=340, y=140)            
            self.lb_rampa_tempo1=Label(conf_rampas,text="Tempo Rampa 1(min): ",font="Arial 15")
            self.lb_rampa_tempo1.place(x=400,y=140)
            self.lb_tempo = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_tempo.place(x=620, y=140)
            self.bt_soma_tempo = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_time1)
            self.bt_soma_tempo.place(x=660, y=140)      
            self.bt_subtracao_tempo = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_time1)
            self.bt_subtracao_tempo.place(x=700, y=140)

            self.lb_rampa2=Label(conf_rampas,text="Temperatura Rampa 2: ",font="Arial 15")
            self.lb_rampa2.place(x=40,y=190)            
            self.lb_temp2 = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_temp2.place(x=260, y=190)
            self.bt_soma_temp2 = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_temp2)
            self.bt_soma_temp2.place (x=300, y=190)        
            self.bt_subtracao_temp2 = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_temp2)
            self.bt_subtracao_temp2.place(x=340, y=190)            
            self.lb_rampa_tempo2=Label(conf_rampas,text="Tempo Rampa 2(min): ",font="Arial 15")
            self.lb_rampa_tempo2.place(x=400,y=190)
            self.lb_tempo2 = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_tempo2.place(x=620, y=190)
            self.bt_soma_tempo2 = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_time2)
            self.bt_soma_tempo2.place(x=660, y=190)        
            self.bt_subtracao_tempo2 = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_time2)
            self.bt_subtracao_tempo2.place(x=700, y=190)

            self.lb_rampa3=Label(conf_rampas,text="Temperatura Rampa 3: ",font="Arial 15")
            self.lb_rampa3.place(x=40,y=240)            
            self.lb_temp3 = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_temp3.place(x=260, y=240)
            self.bt_soma_temp3 = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_temp3)
            self.bt_soma_temp3.place(x=300, y=240)        
            self.bt_subtracao_temp3 = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_temp3)
            self.bt_subtracao_temp3.place(x=340, y=240)            
            self.lb_rampa_tempo3=Label(conf_rampas,text="Tempo Rampa 3(min): ",font="Arial 15")
            self.lb_rampa_tempo3.place(x=400,y=240)
            self.lb_tempo3 = Label(conf_rampas,text="0",font="Arial 20", fg= "black")
            self.lb_tempo3.place(x=620, y=240)
            self.bt_soma_tempo3 = Button(conf_rampas, width=4, height =2, text="+", command= self.bt_soma_time3)
            self.bt_soma_tempo3.place(x=660, y=240)        
            self.bt_subtracao_tempo3 = Button(conf_rampas, width=4, height=2, text="-", command= self.bt_subtracao_time3)
            self.bt_subtracao_tempo3.place(x=700, y=240)
               
        
        self.bt_confirma_temp = Button(conf_rampas, text="Confirmar", width=40, height=5, command=self.conf_fervura)
        self.bt_confirma_temp.place(x=150, y=300)
        self.bt_cancela_rampas = Button(conf_rampas, text="Cancelar", width=30, height=5, command=conf_rampas.destroy)
        self.bt_cancela_rampas.place(x=450, y=300)
        conf_rampas.geometry("800x480+200+200")


    def conf_fervura(self):

                     
        conf_fervura = Tk()
        conf_fervura.title("Automação Brassagem e Fervura")
        self.lb_conf_fervura = Label(conf_fervura, text="Configure a fervura", font="Arial 20")
        self.lb_conf_fervura.place(x=270, y=60)
        
        self.lb_conf_fervura_combo=Label(conf_fervura,text="Tempo de fervura: ",font="Arial 15")
        self.lb_conf_fervura_combo.place(x=180,y=110)
        self.lb_fervura = Label(conf_fervura,text="0",font="Arial 20", fg= "black")
        self.lb_fervura.place(x=360, y=110)
        self.bt_soma_fervura = Button(conf_fervura, width=4, height =2, text="+", command= self.bt_soma_fervura)
        self.bt_soma_fervura.place(x=400, y=115)        
        self.bt_subtracao_fervura = Button(conf_fervura, width=4, height=2, text="-", command= self.bt_subtracao_fervura)        
        self.bt_subtracao_fervura.place(x=440, y=115)       

        self.lb_conf_fervura_combo=Label(conf_fervura,text="Quantidade lupulos: ",font="Arial 15")
        self.lb_conf_fervura_combo.place(x=180,y=170)
        self.lb_lupulo1 = Label(conf_fervura,text="0",font="Arial 20", fg= "black")
        self.lb_lupulo1.place(x=360, y=160)
        self.bt_soma_lupulo1 = Button(conf_fervura, width=4, height =2, text="+", command= self.bt_soma_lupulo1)
        self.bt_soma_lupulo1.place(x=400, y=160)
                
        self.bt_subtracao_lupulo1 = Button(conf_fervura, width=4, height=2, text="-", command= self.bt_subtracao_lupulo1)        
        self.bt_subtracao_lupulo1.place(x=440, y=160)

        self.bt_confirma_temp = Button(conf_fervura, text="Continuar", width=40, height=5, command = self.conf_lupulo)      
	
        self.bt_confirma_temp.place(x=150, y=300)
        self.bt_cancela_rampas = Button(conf_fervura, text="Cancelar", width=30, height=5, command=conf_fervura.destroy)
        self.bt_cancela_rampas.place(x=450, y=300)
        conf_fervura.geometry("800x480+200+200")
        
    def conf_lupulo(self):

        lupulo1 = open("lupulo1.txt")
        lupulo1 = int(lupulo1.read())
        print(lupulo1)

        conf_lupulo= Tk()
        conf_lupulo.title("Automação Brassagem e Fervura")
        self.lb_conf_lupulo = Label(conf_lupulo, text="Configure o tempo dos lupulos", font="Arial 20")
        self.lb_conf_lupulo.place(x=270, y=60)        
        
        if lupulo1 == 1:
            self.lb_conf_fervura_lup1=Label(conf_lupulo,text="Tempo lupulo 1: ",font="Arial 15")
            self.lb_conf_fervura_lup1.place(x=180,y=130)
            self.lb_tempolup1 = Label(conf_lupulo,text="0",font="Arial 20", fg= "black")
            self.lb_tempolup1.place(x=350, y=130)
            self.bt_soma_lup1 = Button(conf_lupulo, width=4, height =2, text="+", command= self.bt_soma_timelup1)
            self.bt_soma_lup1.place(x=400, y=130)        
            self.bt_subtracao_lup1 = Button(conf_lupulo, width=4, height=2, text="-", command= self.bt_subtracao_timelup1)
            self.bt_subtracao_lup1.place(x=440, y=130)

        
        elif lupulo1 == 2:

            self.lb_conf_fervura_lup1=Label(conf_lupulo,text="Tempo lupulo 1: ",font="Arial 15")
            self.lb_conf_fervura_lup1.place(x=180,y=130)
            self.lb_tempolup1 = Label(conf_lupulo,text="0",font="Arial 20", fg= "black")
            self.lb_tempolup1.place(x=350, y=130)
            self.bt_soma_lup1 = Button(conf_lupulo, width=4, height =2, text="+", command= self.bt_soma_timelup1)
            self.bt_soma_lup1.place(x=400, y=130)        
            self.bt_subtracao_lup1 = Button(conf_lupulo, width=4, height=2, text="-", command= self.bt_subtracao_timelup1)
            self.bt_subtracao_lup1.place(x=440, y=130)
            
            self.lb_conf_fervura_lup2=Label(conf_lupulo,text="Tempo lupulo 2: ",font="Arial 15")
            self.lb_conf_fervura_lup2.place(x=180,y=180)
            self.lb_tempolup2 = Label(conf_lupulo,text="0",font="Arial 20", fg= "black")
            self.lb_tempolup2.place(x=350, y=180)
            self.bt_soma_lup2 = Button(conf_lupulo, width=4, height =2, text="+", command= self.bt_soma_timelup2)
            self.bt_soma_lup2.place(x=400, y=180)        
            self.bt_subtracao_lup2 = Button(conf_lupulo, width=4, height=2, text="-", command= self.bt_subtracao_timelup2)
            self.bt_subtracao_lup2.place(x=440, y=180)

        self.bt_confirma_temp = Button(conf_lupulo, text="Iniciar Processo", width=40, height=5)       
	
        self.bt_confirma_temp.place(x=150, y=300)
        self.bt_cancela_rampas = Button(conf_lupulo, text="Cancelar", width=30, height=5, command=conf_lupulo.destroy)
        self.bt_cancela_rampas.place(x=450, y=300)
        conf_lupulo.geometry("800x480+200+200")
        
        


root = Tk()
root.title("Automação Brassagem e Fervura")
principal(root)

#imagem = PhotoImage(file="TelaIHM.png")
#img = Label(root, image=imagem)
#img.imagem = imagem
#img.place(x=0, y=0)

margem = Label(root, height=7)
margem.pack(anchor=W)

root.geometry("800x480+200+200")
root.mainloop()
