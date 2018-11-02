import pyrebase

config = {
    "apiKey": "AIzaSyB7hqzc1Ml6d9uGUYRLF1Iad6J6QiTWjSM",
    "authDomain": "loginemail-a0eb8.firebaseapp.com",
    "databaseURL": "https://loginemail-a0eb8.firebaseio.com",
    "projectId": "loginemail-a0eb8",
    "storageBucket": "loginemail-a0eb8.appspot.com",
	"messagingSenderId": "565232829032"
};

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def getConta(key):
	print("***Def getConta***")
	data = db.child("maquinas/" + key).get()
	
	print(data.val())
	
	for user in data.each():
		conta = user.val()

	conta = str(conta)
	print(conta)
	return conta
	
def getData(key):
	print("***Def getData***")
	conta = getConta(key)
	data = db.child(conta + "/produzindo").get()

	for user in data.each():
		resul = user.val()

	return resul
	
def pushData(key, data, local):
	print("***Def pushData***")
	conta = getConta(key)
	db.child(conta).child("produzindo").update({local: data})

def confTempo():	
	db.child(key).child("produzindo").set({tempoAtualRaw: ""})
	db.child(key).child("produzindo").set({tempoTotalRaw: ""})
