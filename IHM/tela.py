from Tkinter import *
import Funcoes as fun
import Configuracoes as conf
import temperatura as temp
import RPi.GPIO as gpio

conf.inicio()

janela = Tk()

def bom_l():
    fun.Liga(6)
    
def bom_d():
    fun.Desliga(6)
    
def pa_l():
    fun.Liga(13)
    
def pa_d():
    fun.Desliga(13)
    
def acen_l():
    fun.Liga(20)
    
def acen_d():
    fun.Desliga(20)
    
def passo_f():
	fun.PassoF()
	
def passo_t():
	fun.PassoT()
	
def alarme():
	fun.Alarme()
    
def sensor():
    s_temp["text"] = temp.read_temp()
    if(gpio.input(19) == True):
        s_chama["text"] = "0"
    else:
        s_chama["text"] = "1"
    if(gpio.input(12) == True):
        s_gas["text"] = "0"
        janela.after(500, sensor)
    else:
        s_gas["text"] = "1"
        janela.after(500, sensor)
    
    
Button(janela, text="Liga Pa", width=20, command=pa_l).place(x=150, y=50)
Button(janela, text="Desliga Pa", width= 20, command=pa_d).place(x=450, y=50)

Button(janela, text="Liga Bomba", width=20, command=bom_l).place(x=150, y=100)
Button(janela, text="Desliga Bomba", width= 20, command=bom_d).place(x=450, y=100)

Button(janela, text="Liga Acendedor", width=20, command=acen_l).place(x=150, y=150)
Button(janela, text="Desliga Acendedor", width= 20, command=acen_d).place(x=450, y=150)

Button(janela, text="Passo Frente", width=20, command=passo_f).place(x=150, y=200)
Button(janela, text="Passo Tras", width= 20, command=passo_t).place(x=450, y=200)

Button(janela, text="Alarme", width=20, command=alarme).place(x=300, y=250)

Label(janela, text="Temperatura:").place(x=150, y=250)
s_temp = Label(janela, text="X.X")
s_temp.place(x=450, y=250)
Label(janela, text="Chama:").place(x=150, y=300)
s_chama = Label(janela, text="2")
s_chama.place(x=450, y=300)
Label(janela, text="Gas:").place(x=150, y=350)
s_gas = Label(janela, text="2")
s_gas.place(x=450, y=350)

janela.after(100, sensor)

janela.title("Teste dos componentes")
janela.geometry("800x480")
#janela.attributes("-fullscreen", 1)

janela.mainloop()

gpio.cleanup()
