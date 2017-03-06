#Clase Nodo Simple con puntero de cola 
class nodoc(object):
	def __init__(self,numero):
		#Atributo que tendra el Nodo, en este caso es una cadena
		self.__numero=numero
		#Puntero que servira para unir los nodos 
		self.__psig = None
	def getNumero(self):
		return self.__numero