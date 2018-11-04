from tkinter import *
import firedb
import comandos as comand
import temperatura as temp
import Funcoes as fun
import Configuracoes as conf

key = "5555"
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
	
def sim():
	seg.destroy()

def nao():
	lbResul_seg["text"] = "Programe sua receita pelo app"
	lbExpl_seg["text"] = "e depois clique no botao \"Sim\" acima"
	
def ok():
	data = firedb.getData(key)
	print("Botao pressionado")
	print(data['controle'])
	if(data['controle'] == "000"):
		fun.Liga(6)
		firedb.pushData(key, "001", "controle")
		ter.after(5000, checaSensores)
	elif(data['controle'] == "002"):
		firedb.pushData(key, "100", "controle")
		ter.after(5000, checaSensores)
	elif(data['controle'] == "003"):
		firedb.pushData(key, "004", "controle")
		fun.Liga(6)
		ter.after(5000, fervura)
	elif(data['controle'] == "005"):
		firedb.finaliza(key)
	btnOk["state"] = "disabled"
	atualizaMensagem()
	tempo()
	
def tempo():
	print("Atualizando Tempo")
	data = firedb.getData(key)
	Temp['text'] = data['tempAtual']
	firedb.pushData(key, comand.tempoProcesso(data['tempoTotalRaw']), "tempoTotal")
	if(int(data['controle']) > 100 and int(data['controle'])%2 == 1):
		firedb.pushData(key, comand.tempoProcesso(data['tempoAtualRaw']), "tempoAtual")
	if(int(data['controle']) >= 4 and int(data['controle']) < 100 and data['tempoAtualRaw'] != "0"):
		firedb.pushData(key, comand.tempoProcesso(data['tempoAtualRaw']), "tempoAtual")
	
def checaSensores():
	tempo()
	data = firedb.getData(key)
	print("Ler sensor de temperatura")
	firedb.pushData(key, temp.read_temp(), "tempAtual")
	if(int(data['rampAtTempe']) >= int(temp.read_temp()) - 2 and int(data['rampAtTempe']) <= int(temp.read_temp()) + 2):
		print("Mantendo temperatura")
		if(data['controle'] == "001"):
			fun.Liga(13)
			firedb.pushData(key, "002", "controle")
			firedb.pushData(key, comand.mensagem("002"), "mensagem")
		elif(int(data['controle']) >= 100 and int(data['controle'])%2 == 0):
			firedb.pushData(key, comand.tempoInicio(), "tempoAtualRaw")
			firedb.pushData(key, (data['tempoAlc'] + str(comand.tempoProcesso(data['tempoTotalRaw'])) + "-"), "tempoAlc")
			firedb.pushData(key, str(int(data['controle']) + 1), "controle")
			firedb.pushData(key, comand.mensagem(str(int(data['controle']) + 1)), "mensagem")
			fun.Alarme()
		elif(int(data['controle']) >= 100 and int(data['controle'])%2 == 1):
			if(str(data['tempoAtual']) == data['rampAtTempo']):
				if(data['rampAtual'] == data['QntRamp']):
					#COMECAR PROCESSO DE FERVURA
					print("Comecando etapa de fervura")
					fun.Alarme()
					fun.Desliga(13)
					fun.Desliga(6)
					firedb.pushData(key, (data['tempoAlc'] + str(comand.tempoProcesso(data['tempoTotalRaw']))), "tempoAlc")
					comand.configurarFervura(key, data['tempoLupulo'])
					firedb.pushData(key, "003", "controle")
					firedb.pushData(key, "Fervura", "rampAtual")
					data = firedb.getData(key)
					firedb.pushData(key, comand.mensagem("003"), "mensagem")
					firedb.pushData(key, "0", "tempoAtual")
					firedb.pushData(key, "0", "tempoAtualRaw")
				else:
					#troca de rampa
					print("Trocando de rampa")
					fun.Alarme()
					firedb.pushData(key, (data['tempoAlc'] + str(comand.tempoProcesso(data['tempoTotalRaw'])) + "/"), "tempoAlc")
					firedb.pushData(key, (int(data['rampAtual']) + 1), "rampAtual")
					comand.configurarRampa(key, (int(data['rampAtual']) + 1), data['tempPro'])
					firedb.pushData(key, (str(int(data['rampAtual']) + 1) + "00"), "controle")
					firedb.pushData(key, comand.mensagem((str(int(data['rampAtual']) + 1) + "00")), "mensagem")
					firedb.pushData(key, "0", "tempoAtual")
	if(data['controle'] == "000" or data['controle'] == "002" or data['controle'] == "003"):
		btnOk["state"] = "active"
	if(btnOk["state"] == "disabled"):
		#CONTROLE DE CHAMA
		ter.after(5000, checaSensores)
		
def fervura():
	print("Fervura")
	tempo()
	firedb.pushData(key, temp.read_temp(), "tempAtual")
	data = firedb.getData(key)
	print(int(data['rampAtTempe']))
	print(int(temp.read_temp()))
	if(int(data['rampAtTempe']) >= int(temp.read_temp()) - 1 and int(data['rampAtTempe']) <= int(temp.read_temp()) + 1):
		firedb.pushData(key, comand.tempoInicio(), "tempoAtualRaw")
		firedb.pushData(key, (data['tempoLupulo'] + str(comand.tempoProcesso(data['tempoTotalRaw'])) + "/"), "tempoLupulo")
		#CONTROLE DE CHAMA PARA FICAR EM CHAMA MEDIA
		fun.Alarme()
		ter.after(5000, lupulo)
	else:
		#CONTROLE DE CHAMA
		ter.after(5000, fervura)
	
def lupulo():
	tempo()
	data = firedb.getData(key)
	print("Lupulo")
	fun.Desliga(6)
	tempLupulos = data['tempoLupulo'].split('*')
	tempLupulos = tempLupulos[0]
	tempLupulos = tempLupulos.split('-')
	tamanho = len(tempLupulos)
	contador = 0
	while(contador < tamanho):
		print(tempLupulos[contador])
		print(data['tempoAtual'])
		if(int(tempLupulos[contador]) == int(data['tempoAtual'])):
			fun.Alarme()
			firedb.pushData(key, comand.mensagem("0"+str(contador+1)+"4"), "mensagem")
			mens = data['tempoLupulo'].split('*')
			mens = mens[1]
			try:
				mens = mens.split('/')
				taman = len(mens)
				print(int(data['tempoTotal']))
				print(int(mens[taman-2]))
				if(int(mens[taman-2]) != int(data['tempoTotal'])):
					firedb.pushData(key, data['tempoLupulo'] + str(data['tempoTotal']) + "/", "tempoLupulo")
				else:
					pass
			except:
				firedb.pushData(key, data['tempoLupulo'] + data['tempoTotal'] + "/", "tempoLupulo")
		contador = contador + 1
	if(int(data['tempoAtual']) == int(data['rampAtTempo'])):
		#DESLIGA CHAMA
		fun.Alarme()
		firedb.pushData(key, "005", "controle")
		firedb.pushData(key, data['tempoLupulo'] + str(data['tempoTotal']), "tempoLupulo")	
		atualizaMensagem()
		btnOk["state"] = "active"
	else:
		ter.after(5000, lupulo)
		
def atualizaMensagem():
	data = firedb.getData(key)
	firedb.pushData(key, comand.mensagem(data['controle']), "mensagem")

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

pri.geometry("800x480")
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

seg.geometry("800x480")
seg.mainloop()

############## INICIO DA CONFIGURACAO ###############

firedb.pushData(key, 1, "rampAtual")
data = firedb.getData(key)
firedb.pushData(key, comand.mensagem(data['controle']), "mensagem")
comand.configurarRampa(key, 1, data['tempPro'])
firedb.pushData(key, 0, "tempoAtual")
firedb.pushData(key, 0, "tempoTotal")
firedb.confTempo(key)
firedb.pushData(key, comand.tempoInicio(), "tempoTotalRaw")
conf.inicio()

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
lbGraus.place(x=450,y=140)
lbRamp = Label(ter, text="Rampa atual:", font=("Arial",15,"bold"))
lbRamp.pack()
Ramp = Label(ter, text=data['rampAtual'], font=("Arial",15,"bold"))
Ramp.place(x=480,y=188)
Aviso = Label(ter, text ="Para mais informacoes consulte o app", font=("Arial",20,"bold"), height=2)
Aviso.pack()
btnOk = Button(ter, text="OK", font=("Arial",20,"bold"), width=10, height=2, command=ok, state="active")
btnOk.pack()

ter.after(100, checaSensores)

ter.geometry("800x480")
ter.mainloop()
