from datetime import datetime
import firedb

def mensagem(cod):
	if cod == "000":
		return "Adicione os 30L de agua, coloque a pa e precione OK para iniciar"
	if cod == "001":
		return "Esquentando agua"
	if cod == "002":
		return "Adicione o malte e precione OK"
	if cod == "003":
		return "Retire a primeira panela e lave o malte, retire a pa e precione OK"
	if cod == "004":
		return "Etapa da fervura"
	if int(cod) >= 14 and int(cod) < 100:
		while int(cod) > 10:
			cod = int(cod) - 10 
		return ("Emulsione o lupulo " + str(int(cod) - 3))
	if cod == "005":
		return "Agora eh com voce, resfrie-a, adicione o fermento e coloque no fermentador"
	if (int(cod) % 2) == 1:
		return "Mantendo temperatura desejada"
	if (int(cod) % 2) == 0:
		return "Aquecendo agua"
	
def tempoInicio():
	now = datetime.now()
	
	minutos = now.hour * 60
	minutos = minutos + now.minute
	
	return minutos
	
def tempoProcesso(inicio):
	now = datetime.now()
	
	minutos = now.hour * 60
	minutos = minutos + now.minute
	
	minutos = minutos - int(inicio)
	
	return minutos

def configurarRampa(key, ramp, rampas):
	rampas = rampas.split('/')
	ramp = rampas[ramp-1]
	ramp = ramp.split('-')
	firedb.pushData(key, ramp[0], "rampAtTempe")
	firedb.pushData(key, ramp[1], "rampAtTempo")
	return 0

def configurarFervura(key, data):
	rampa = data.split('/')
	tempo = rampa[0]
	lupulo = rampa[1]
	firedb.pushData(key, tempo, "rampAtTempo")
	firedb.pushData(key, "96", "rampAtTempe")
	firedb.pushData(key, lupulo, "tempoLupulo")
	return 0
	
	
