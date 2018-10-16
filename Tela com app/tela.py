from tkinter import *
#import firedb

key = "7745"
data = ""

def conta():
	val = "0"
	#firedb.getConta(key)
	if val == "0":
		lbResul["text"] = "Nao foi encontrada conta vinculada com essa maquina"
		lbExpl["text"] = "Faca o cadastro pelo aplicativo"
	else:
		lbResul["text"] = val
		lbExpl["text"] = ""
		pri.destroy()
	
def data():
	pass#data = firedb.getData(key)
	
def sim():
	seg.destroy()

def nao():
	lbResul_seg["text"] = "Programe sua receita pelo app"
	lbExpl_seg["text"] = "e depois clique no botao \"Sim\" acima"
	
def ok():
	pass
	
def checaSensores():
	print(btnOk["state"])
	if(btnOk["state"] == "disabled"):
		ter.after(1000, checaSensores)

##################  PRIMEIRA TELA  ##################  
pri = Tk()
imagem = PhotoImage(file="TelaIHM.png")
img = Label(pri, image=imagem)
img.imagem = imagem
img.place(x=0, y=0)

margem = Label(pri, height=7)
margem.pack(anchor=W)

lb = Label(pri, text="O numero da sua maquina e "+key,font=("Arial", 30, "bold"), height=2)
lb.pack()
btnConf = Button(pri,text="Ok", font=("Arial",20,"bold"), width=10, height=2, command=conta)
btnConf.pack()
lbResul = Label(pri, text="",font=("Arial",20,"bold"), height = 2)
lbResul.pack()
lbExpl = Label(pri, text="",font=("Arial",20,"bold"), height = 1)
lbExpl.pack()

pri.geometry("800x480+200+200")
pri.mainloop()

##################  SEGUNDA TELA ##################  

seg = Tk()
imagem = PhotoImage(file="TelaIHM.png")
img = Label(seg, image=imagem)
img.imagem = imagem
img.place(x=0, y=0)

margem_seg = Label(seg, height=7)
margem_seg.pack(anchor=W)

lb_seg = Label(seg, text="Ja foi feita a programacao da receita pelo app?",font=("Arial", 20, "bold"), height=2)
lb_seg.pack()
btnConf_seg = Button(seg,text="Sim", font=("Arial",20,"bold"), width=10, height=2, command=sim)
btnConf_seg.place(x = 150, y = 180)
btnNeg_seg = Button(seg,text="Nao", font=("Arial",20,"bold"), width=10, height=2, command=nao)
btnNeg_seg.place(x = 450, y = 180)
espaco_seg = Label(seg, height=7)
espaco_seg.pack()
lbResul_seg = Label(seg, text="",font=("Arial",20,"bold"), height = 2)
lbResul_seg.pack()
lbExpl_seg = Label(seg, text="",font=("Arial",20,"bold"), height = 1)
lbExpl_seg.pack()

seg.geometry("800x480+200+200")
seg.mainloop()

##################  TERCEIRA TELA  ##################  

ter = Tk()
imagem = PhotoImage(file="TelaIHM.png")
img = Label(ter, image=imagem)
img.imagem = imagem
img.place(x=0, y=0)

margem_ter = Label(ter, height=7)
margem_ter.pack(anchor=W)

lbTemp = Label(ter, text="Temperatura atual do processo:", font=("Arial",20,"bold"))
lbTemp.pack()
Temp = Label(ter, text="22", font=("Arial",30,"bold"))
Temp.pack()
lbGraus = Label(ter, text="C", font=("Arial",30,"bold"))
lbGraus.place(x=450,y=135)
lbRamp = Label(ter, text="Rampa atual:", font=("Arial",15,"bold"))
lbRamp.pack()
Ramp = Label(ter, text="2", font=("Arial",15,"bold"))
Ramp.place(x=480,y=183)
Aviso = Label(ter, text ="Para mais informacoes consulte o app", font=("Arial",20,"bold"), height=2)
Aviso.pack()
btnOk = Button(ter, text="OK", font=("Arial",20,"bold"), width=10, height=2, command=ok, state=DISABLED)
btnOk.pack()

ter.after(100, checaSensores)

ter.geometry("800x480+200+200")
ter.mainloop()


