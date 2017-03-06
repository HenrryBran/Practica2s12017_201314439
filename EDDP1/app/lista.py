import os
from graphviz import Digraph
import nodol
nodo = nodol

#Clase Lista simple enlazada
class lista(object):
	def __init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__tamanio = 0

	def getVacioL(self):
		if self.__primero == None:
			return True

	def insertarL(self ,cadena):
		nuevo = nodo.nodol(cadena)
		if self.getVacioL() == True:
			self.__primero = nuevo
			self.__ultimo = nuevo
		else:
			self.__ultimo.psig = nuevo
			self.__ultimo = nuevo
		self.__tamanio +=1

	def gettamanioL(self):
		return self.__tamanio

	def eliminarL(self,indice):
		if indice == 0:
			self.__primero = self.__primero.psig
			self.__tamanio -=1
		elif indice == self.__tamanio -1:
			val = True
			temp = self.__primero
			while(val):
				if temp.psig == self.__ultimo:
					temp2 = self.__ultimo
					self.__ultimo = temp
					temp2 = None
					val = False
					self.__tamanio -=1
				else:
					temp = temp.psig
		elif indice > self.__tamanio-1:
			print("El indice no existe")
		else:
			temp = self.__primero
			cont = 0
			while cont<indice-1:
				temp = temp.psig
				cont +=1
			temp2 = temp.psig
			temp.psig = temp2.psig
			temp2 = None
			temp = None
			self.__tamanio -=1

	def buscarL(self,dato):
		temp = self.__primero
		cont = 0
		cont2 = 0
		mensaje = 'NO SE ENCONTRO EL DATO'
		while temp!=None and cont!=1:
			if dato == temp.getCadena():
				cont = 0
				mensaje2 = "DATO SE ENCUENTRA EN EL ÍNDICE <" + str(cont2) + ">"
				return mensaje2
			elif cont2 == self.__tamanio-1:				
				return mensaje
			else:
				temp = temp.psig
				cont2+=1

	def imprimirL(self):
		if self.getVacioL()==True:
			return("lista vacia")
		else:
			val = True
			temp = self.__primero
			while(val):
				print(temp.getCadena())
				if temp == self.__ultimo:
					val = False
				else:
					temp = temp.psig

	def graficarL(self):
		temp = self.__primero
		file_path = "Grafos"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Grafos/listasimple.dot","w")
			archivo.write("digraph Lista_simple{\n")
			archivo.write("subgraph cluster_1{\n")
			archivo.write("\t node[style=filled,color=orange];\n")
			while temp!=None :
				archivo.write("\t"+temp.getCadena())										
				if temp !=self.__ultimo:
					temp = temp.psig
					archivo.write("->"+temp.getCadena())
					archivo.write("\n")					
				else:
					archivo.write("; \n")
					temp = None
			archivo.write("\t label = \" Lista Simple \" ;\n")
			archivo.write("\t color=blue")
			archivo.write("\t}\n")
			archivo.write("}")
			archivo.close()
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Grafos\\listasimple.dot -o Grafos\\listasimple.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")