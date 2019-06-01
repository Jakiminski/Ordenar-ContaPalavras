import sys #.argv, .executable and .exit([int or obj])
from util import *

# Não-Constantes Globais
PRIMO = 23 # Não par  
TRY = 1000 # Tentativas em cada Busca ou Inserção

class TupleForHash(object): # A tupla é uma Quádrupla: (Chave, ocorrências, status, endereço da lista)
	def __init__(self,key,counter=int(1),status='EMPTY'):
		self.key = key.lower() # Chave de consulta
		self.counter = counter # Conta as ocorrências da Key no arquivo
		self.status = status.upper() # 'EMPTY'/'BUZY'/'COLLISION'
		self.listaCol = [] # Lista Vazia para Colisões, para endereçamento encadeado
		pass

class HashTable(object):
	# 0.1.Construtor
	def __init__(self,size=int(1),method='duplo'):
		self.size = size # EVITAR Potência de 2
		self.table = [] * size # Tabela vazia
		self.seed = 0 # auxilia Hashing-Duplo
		self.method = method.lower() # Determina tratamento de colisão 'duplo' ou 'encadeado'
		pass

	# 0.2.Funções que determinam posição na tabela
	def hashing(self,key): # Retorna um índice para a lista
		primo = PRIMO
		num = stringToNumber(key)
		index = (num + primo) % self.size 
		print(index)
		print(str(num),' ',str(primo))
		return index # index pertence ao intervalo [0,self.size[

	def hashing2(self,key,mult=int(1)): # Hashing Duplo
		#mult = incrementar a cada chamada
		primo = PRIMO
		num = stringToNumber(key)
		index = (num + mult * primo) % self.size 
		print(str(index))
		return index # index pertence ao intervalo [0,self.size[
		
	# 0.3.Colisão na tabela e afins
	def collision(self,index): # Colisão na posição da lista 
		#TRUE -> 'BUZY' / 'COLLISION' and FALSE -> 'EMPTY'
		if index < len(self.table): # Previne "list index out of range"	
			if self.table[index] is not None: # Posição na tabela existe
				flag = True if self.table[index].status is not 'EMPTY' else False
				self.table[index].status = 'COLLISION' # 'BUZY' não indica colisão
				return flag
		else: 
			return False

	# 0.4.Inserção na tabela	
	def insertTable(self,key,status):
		tryInsert = 0 # Tolerância / Tentativas de Inserção
		index = self.hashing(key)
		collision = self.collision(index) # Boolean
		if collision is False:
			if index < len(self.table): # Previne "list index out of range"	
				self.table[index] = TupleForHash(key,1,status)
				print('{} inserido em {}.Status: {}'.format(elem,index,status))
			else: 
				for i in range(0,len(self.table)):
					self.table.append(TupleForHash('',1,'EMPTY')) # Insere posições vazias
				self.table[index] = TupleForHash(key,1,status)
				print('{} inserido em {}.Status: {}'.format(elem,index,status))
		else: # TRATAR COLISÃO
			if self.table[index].key != key:
				if self.method == 'encadeado':
					lista = self.table[index].listaCol # Lista de colisões
					lista.append(elem)
				elif self.method == 'duplo':
					# OBTER INDEX DA FUNCAO DE HASHING DUPLO VIA LOOP
					while (collision):
						if tryInsert >= TRY:
							break
						else:
							tryInsert += 1 # Mais uma tentativa
							index = self.hashing2(key,tryInsert+1)
							collision = self.collision(index)
					
					if tryInsert < TRY:
						self.table[index] = elem # Insere em uma posição avaliável
			
					else:
						print('Erro de inserção. Limite de tentativas excedido.')
		pass

	#0.5. Busca elemento na tabela, retorna elemento TupleForHash
	def findTable(self,key):
		trySearch = 0 # Tolerância / Tentativas de Busca
		index = self.hashing(key)
		print('index {}'.format(index))
		if index < len(self.table): # Previne "list index out of range"	
			if self.table[index].key == key:
				return self.table[index]
		else:
			# Continuar busca caso haja colisões
			if self.method == 'encadeado':
				collision = self.collision(index)
				if collision is True:
					elem = self.searchInList(key,index) if self.searchInList(key,index) is not None else None
						
			elif self.method == 'duplo':
				collision = self.collision(index)
				while collision:
					if trySearch >= TRY:
						break
					else:
						trySearch += 1 # mais uma tentativa
						index = self.hashing2(key,trySearch)
						collision = self.collision(index)
					return self.table[index] if tryInsert < TRY else None
		return None
	
	def searchInList(self,key,index): # Retorna TupleForHash
	# Recebe índice de colisão e chave de pesquisa
		listaCol = self.table[index].listaCol
		for element in listaCol:
			if element.key == key:
				return element
		return None

	#0.6. Adiciona ocorrência da palavra
	def addCounter(self,key): # Independe se o elemento está na hashtable ou lista de colisões
		if self.findTable(key) is not None:
			# Elemento já inserido -> Incrementar qnt de ocorrencias
			print('add ocorrencia de chave existente.')
			elem = self.findTable(key)
			if elem.counter > 0:
				elem.counter += 1
				return elem.counter
			else:
				print('Contador com Erros. {} ocorrências'.format(elem.counter))
		else: 
			# Inserir elemento
			print('add nova chave.')
			self.insertTable(key,'BUZY')
			# Nova checagem/busca + retorno (não excedeu tentativas)
			return -1 if self.findTable(key) is None else self.findTable(key).counter
		
if __name__ == '__main__':
	
	flag = True;
	while (flag):
		size = int(input('\nDefina o tamanho da tabela Hash.\t'))
		method = input('\nDefina o Método.(Escreva\'encadeado\' ou \'duplo\')\n').lower()
		flag = (False if size > 0 else True) and (True if method == 'encadeado' or method == 'duplo' else False) 
	hastable = HashTable(size,method)
	
	# Definir operações
		# inserir nova palavra na tabela hash (inserir em local vazio, tratar colisão)
		# consultar elemento na tabela hash (checar a posição imediata, depois quando houver colisão)
		# Adicionar ocorrência
	
	sys.exit(0)
	