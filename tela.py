from tkinter import *
import firedb
import comandos as comand

key = "7757"
data = ""

def conta():
	val = firedb.getConta(key)
	if val == "0":
		lbResul["text"] = "Nao foi encontrada conta vinculada com essa maquina"
		lbExpl["text"] = "Faca o cadastro pelo aplicativo"
	else:
		lbResul["text"] = val
		lbExpl["text"] = ""
		pri.destroy()
	
def data():
	data = firedb.getData(key)
	
def sim():
	seg.destroy()

def nao():
	lbResul_seg["text"] = "Programe sua receita pelo app"
	lbExpl_seg["text"] = "e depois clique no botao \"Sim\" acima"
	
def ok():
	print("Botao pressionado")
	if(int(data['comando']) == 0):
		firedb.pushData(key, "001", "comando")
	elif(int(data['comando']) == 2):
		comando = int(data['rampAtual'] + "00")
		firedb.pushData(key, comando, "comando")
	elif(int(data['comando']) == 3):
		firedb.pushData(key, "004", "comando")
	btnOk["state"] = "disabled"
	atualizaMensagem()
	tempo()
	ter.after(5000, checaSensores)
	
def tempo():
	data = firedb.getData(key)
	firedb.pushData(key, comand.tempoProcesso(data['tempoTotalRaw']), "tempoTotal")
	if(int(data['comando']) > 100 and int(data['comando'])%2 == 1):
		firedb.pushData(key, comand.tempoProcesso(data['tempoAtualRaw']), "tempoAtual")
	
def checaSensores():
	tempo()
	print("Ler sensor de temperatura")
	#firedb.pushData(key, PEGAR VALOR DO SENSOR, "tempAtual")
	if(data['rampAtTempe'] == '''Valor do sensor'''):
		if(data['comando'] == "001"):
			firedb.pushData(key, "002", "comando")
			firedb.pushData(key, comand.mensagem("002"), "mensagem")
		elif(int(data['comando']) > 100 and int(data['comando'])%2 == 0):
			firedb.pushData(key, comand.tempoInicio(), "tempoAtualRaw")
			firedb.pushData(key, (data['tempAlc'] + str(comand.tempoProcesso(data['tempoTotalRaw'])) + "-"), "tempoTotal")
			firedb.pushData(key, str(int(data['comando']) + 1), "comando")
			firedb.pushData(key, comand.mensagem(str(int(data['comando']) + 1)), "mensagem")
		elif(int(data['comando']) > 100 and int(data['comando'])%2 == 1):
			if(data['tempoAtual'] == data['rampAtTempo']):
				if(data['rampAtual'] == data['QntRamp']):
					#COMECAR PROCESSO DE FERVURA
					pass
				else:
					pass
					#parou aqui, colocar tempo no tempAlc, trocar de rampa
	if(data['comando'] == "000" or data['comando'] == "002" or data['comando'] == "003"):
		btnOk["state"] = "enabled"
	elif(btnOk["state"] == "disabled"):
		#CONTROLE DE CHAMA
		ter.after(5000, checaSensores)
		
def atualizaMensagem():
	firedb.pushData(key, comand.mensagem(data['comando']), "mensagem")

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

############## INICIO DA CONFIGURACAO ###############

firedb.pushData(key, 1, "rampAtual")
data = firedb.getData(key)
firedb.pushData(key, comand.mensagem(data['comando']), "mensagem")
comand.configurarRampa(key, 1, data['tempPro'])
firedb.pushData(key, 0, "tempoAtual")
firedb.pushData(key, 0, "tempoTotal")
firedb.confTempo()
firedb.pushData(key, comand.tempoInicio(), "tempoTotalRaw")

##################  TERCEIRA TELA  ##################  

ter = Tk()
imagem = PhotoImage(file="TelaIHM.png")
img = Label(ter, image=imagem)
img.imagem = imagem
img.place(x=0, y=0)

margem_ter = Label(ter, height=7)
margem_ter.pack(anchor=W)

lbNome = Label(ter, text = data['name'], font=("Arial",15,"bold"))
lbNome.pack()
lbNome['text'] = data['name']
lbTemp = Label(ter, text="Temperatura atual do processo:", font=("Arial",20,"bold"))
lbTemp.pack()
Temp = Label(ter, text=data['tempAtual'], font=("Arial",30,"bold"))
Temp.pack()
lbGraus = Label(ter, text="C", font=("Arial",30,"bold"))
lbGraus.place(x=450,y=135)
lbRamp = Label(ter, text="Rampa atual:", font=("Arial",15,"bold"))
lbRamp.pack()
Ramp = Label(ter, text=data['rampAtual'], font=("Arial",15,"bold"))
Ramp.place(x=480,y=183)
Aviso = Label(ter, text ="Para mais informacoes consulte o app", font=("Arial",20,"bold"), height=2)
Aviso.pack()
btnOk = Button(ter, text="OK", font=("Arial",20,"bold"), width=10, height=2, command=ok, state=enabled)
btnOk.pack()

ter.after(100, checaSensores)

ter.geometry("800x480+200+200")
ter.mainloop()
