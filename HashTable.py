import util

class HashTable(object):
	# 0.1.Construtor
	def __init__(self,size=int(1),count=int(0)):
		self.table = ['0'] * size # Lista "vazia" de elementos
		self.size = size # Tamanho da tabela de Hash
		self.count = 0; # auxilia seed do hash duplo
		pass
		
	# 0.2.Funções que determinam posição na tabela
	# numKey é conversão da chave para um valor numérico
	def hash1(self,numKey=int(0)): 
  		return numKey % self.size # MOD function
	
	def hash2(self,numKey=int(0)):
		result = numKey % self.size
		# TO DO: Tratar Colisões de hash Duplo
		return self.count * result
		
	# 0.3.Inserção na tabela	
	def insertTable(self,key,value):
		# Definir posição em tabelahash
		pos = self.hashFunction(util.strScore(key)) 
		# TO DO: Tratar colisões de Hash Simples na Lista de Colisões
		self.table[pos] = value
		pass
