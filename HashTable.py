import util

class HashTable(object): # (0/4)
	# 0.1.Construtor
	def __init__(self,size=int(1),count=int(0)):
		self.table = [''] * size # Lista "vazia" de chaves
		self.occur = [int(0)] * size # conta ocorrências da chave
		self.size = size # Tamanho da tabela de Hash
		self.seed = 0; # auxilia seed do hash duplo
		pass
		
	# 0.2.Funções que determinam posição na tabela
	# numKey é conversão da chave para um valor numérico
	def hash1(self,numKey=int(0)): 
  		primo = 7
		return (numKey + primo) % self.size # MOD function
	
	def hash2(self,numKey=int(0)):
		
		pos1 = hash1(numKey)
		
	
	# 0.3.Colisão na tabela
	def colide(self,key,pos):
		if self.table[pos]=='':
			return False
		elif self.table[pos]==key:
			return False
		else True
			
	# 0.4.Inserção na tabela	
	def insertTable(self,key,value):
		# Definir posição em tabelahash
		pos = self.hash1(util.strScore(key)) 
		# TO DO: Tratar colisões de Hash Simples na Lista de Colisões ORDENADA
		self.table[pos] = value
		pass
	
	def insertTable2(self,key,value):
		pos = self.hash1(util.strScore(key))
		# TO DO: Tratar colisões de Hash Duplo
		while (self.colide(key,pos)):
			self.seed += 1
			numKey = util.strScore(key)
			pos = self.hash1(numKey) + self.seed * self.hash2(numKey)
			pos = pos % 
		self.seed = 0
		pass
