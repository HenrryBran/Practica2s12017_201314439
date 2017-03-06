import lista
import pila
import cola
from flask import Flask, request
ocola = cola.cola()
opila = pila.pila()
olista = lista.lista()
app = Flask("eddp1")

#METODOS PARA LA LISTA SIMPLE
@app.route('/insertarL',methods=['POST'])
def insetarL():
	cadena = str(request.form['cadena'])
	olista.insertarL(str(cadena))
	olista.imprimirL()
	olista.graficarL()
	return "Se ha insertado el valor en la lista " + str(cadena)

@app.route('/eliminarL',methods=['POST'])
def eliminarL():
	numero = str(request.form['numero'])
	olista.eliminarL(int(numero))	
	olista.imprimirL()
	olista.graficarL()
	return "Se ha eliminado el siguiente indice " + str(numero)

@app.route('/buscarL',methods=['POST'])
def buscarL():
	cadena = str(request.form['cadena'])
	aux = olista.buscarL(str(cadena))
	return str(aux)

#METODOS PARA LA PILA
@app.route('/push',methods=['POST'])
def push():
	numero = str(request.form['numero'])
	opila.push(int(numero))
	opila.graficarP()
	cadena = str(opila.imprimirP())
	return cadena

@app.route('/pop',methods=['POST'])
def pop():
	numero = str(request.form['numero'])
	opila.pop()
	opila.graficarP()
	cadena = str(opila.imprimirP())
	return cadena

#METODOS PARA LA COLA
@app.route('/queue',methods=['POST'])
def queue():
	numero = str(request.form['numero'])
	ocola.queue(int(numero))
	ocola.graficarC()
	cadena = str(ocola.imprimirC())
	return cadena

@app.route('/dequeue',methods=['POST'])
def dequeue():
	numero = str(request.form['numero'])
	ocola.dequeue()
	ocola.graficarC()
	cadena = str(ocola.imprimirC())
	return cadena

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')