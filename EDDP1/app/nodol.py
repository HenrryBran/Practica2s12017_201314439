#Clase Nodo Simple con puntero 
class nodol(object):
	def __init__(self,cadena):
		#Atributo que tendra el Nodo, en este caso es una cadena
		self.__cadena=cadena
		#Puntero que servira para unir los nodos 
		self.__psig = None
	def getCadena(self):
		return self.__cadena