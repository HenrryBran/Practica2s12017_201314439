import os
from graphviz import Digraph
import nodoc
nodo = nodoc

#Clase Lista simple enlazada
class cola(object):
	def __init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__tamanio = 0

	def getVacioC(self):
		if self.__primero == None:
			return True

	def gettamanioC(self):
		return self.__tamanio

	def imprimirC(self):
		cadena = ""
		if self.getVacioC()==True:
			return("lista vacia")
		else:
			val = True
			temp = self.__primero
			while(val):
				cadena = cadena +"->"+ str(temp.getNumero())
				print(temp.getNumero())
				if temp == self.__ultimo:
					val = False
				else:
					temp = temp.psig
		return cadena

	def queue(self,numero):
		nuevo = nodo.nodoc(numero)
		if self.getVacioC()==True:
			self.__primero = self.__ultimo = nuevo
		else:
			nuevo.psig = self.__primero
			self.__primero = nuevo

	def dequeue(self):
		if self.getVacioC()==True:
			print("cola vacia")
		elif self.__primero == self.__ultimo:
			self.__primero = None
			self.__ultimo = None
			print("elemento eliminado")
		else:
			val = True
			temp = self.__primero
			while(val):
				if temp.psig == self.__ultimo:
					temp2 = self.__ultimo
					self.__ultimo = temp
					temp2 = None
					val = False
					print("elemento eliminado")
				else:
					temp = temp.psig

	def graficarC(self):
		temp = self.__primero
		file_path = "Grafos"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Grafos/cola.dot","w")
			archivo.write("digraph cola{\n")
			archivo.write("subgraph cluster_1{\n")
			archivo.write("\t node[style=filled,color=orange];\n")
			while temp!=None :
				archivo.write("\t"+ str(temp.getNumero()))										
				if temp !=self.__ultimo:
					temp = temp.psig
					archivo.write("->"+ str(temp.getNumero()))
					archivo.write("\n")					
				else:
					archivo.write("; \n")
					temp = None
			archivo.write("\t label = \" Cola \" ;\n")
			archivo.write("\t color=blue")
			archivo.write("\t}\n")
			archivo.write("}")
			archivo.close()
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Grafos\\cola.dot -o Grafos\\cola.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")