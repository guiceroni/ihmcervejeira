import pyrebase

config = {
    "apiKey": "AIzaSyB7hqzc1Ml6d9uGUYRLF1Iad6J6QiTWjSM",
    "authDomain": "loginemail-a0eb8.firebaseapp.com",
    "databaseURL": "https://loginemail-a0eb8.firebaseio.com",
    "projectId": "loginemail-a0eb8",
    "storageBucket": "loginemail-a0eb8.appspot.com",
	"messagingSenderId": "565232829032"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def getConta(key):
	#print("***Def getConta***")
	data = db.child("maquinas/" + key).get()
	
	#print(data.val())
	
	for user in data.each():
		conta = user.val()

	conta = str(conta)
	#print(conta)
	return conta
	
def getData(key):
	#print("***Def getData***")
	conta = getConta(key)
	data = db.child(conta).child("/produzindo").get()
	
	for user in data.each():
		resul = user.val()
	
	return resul
	
def pushData(key, data, local):
	#print("***Def pushData***")
	conta = getConta(key)
	chave = db.child(conta).child("/produzindo").shallow().get()
	chave = chave.each()
	chave = chave[0]
	db.child(conta).child("produzindo").child(chave).update({local: data})

def confTempo(key):	
	conta = getConta(key)
	chave = db.child(conta).child("/produzindo").shallow().get()
	chave = chave.each()
	chave = chave[0]
	tempoAtualRaw = ""
	tempoTotalRaw = ""
	db.child(conta).child("produzindo").child(chave).update({'tempoAtualRaw': '0'})
	db.child(conta).child("produzindo").child(chave).update({'tempoTotalRaw': '0'})

def finaliza(key):
	conta = getConta(key)
	data = getData(key)
	db.child(conta).child("producoes").child(data['fKey']).update({'tempAlc': data['tempoAlc']})
	db.child(conta).child("producoes").child(data['fKey']).update({'tempLupulo': (data['rampAtTempo'] + "/" + data['tempLupulo'])})
	db.child(conta).child("producoes").child(data['fKey']).update({'tempoTot': data['tempoTotal']})
	db.child(conta).child("produzindo").remove()

def relatorio(key):
	conta = getConta(key)
	data = getData(key)
	db.child(conta).child("producoes").child(data['fKey']).update({'tempAlc': data['tempAlc']})
	db.child(conta).child("producoes").child(data['fKey']).update({'tempLupulo': data['tempLupulo']})
	db.child(conta).child("producoes").child(data['fKey']).update({'tempoTot': data['tempoTotal']})
