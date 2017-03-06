import os
from graphviz import Digraph
import nodop
nodo = nodop

#Clase Lista simple enlazada
class pila(object):
	def __init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__tamanio = 0

	def getVacioP(self):
		if self.__primero == None:
			return True

	def gettamanioP(self):
		return self.__tamanio

	def imprimirP(self):
		cadena = ""
		if self.getVacioP()==True:
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

	def push(self,numero):
		nuevo = nodo.nodop(numero)
		if self.getVacioP()==True:
			self.__primero = self.__ultimo = nuevo
		else:
			nuevo.psig = self.__primero
			self.__primero = nuevo

	def pop(self):
		if self.getVacioP()==True:
			print("pila vacia")
		elif self.__primero == self.__ultimo:
			self.__primero = None
			self.__ultimo = None
			print("elemento eliminado")
		else:
			temp = self.__primero
			self.__primero = self.__primero.psig
			temp = None
			print("elemento eliminado")

	def graficarP(self):
		temp = self.__primero
		file_path = "Grafos"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Grafos/pila.dot","w")
			archivo.write("digraph pila{\n")
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
			archivo.write("\tlabel = \" Pila \" ;\n")
			archivo.write("\tcolor=blue")
			archivo.write("\t}\n")
			archivo.write("}")
			archivo.close()
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Grafos\\pila.dot -o Grafos\\pila.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")