# RedBlack Tree

class RBNode(object):
	# 1.1. Construtor

	def __init__(self,key,color='RED',parent=None,leftSon=None,rightSon=None):
		self.key = key.lower() # A palavra lida é a própria chave  em Lowercase
		self.counter = 1 # conta ocorrências de key no arquivo
		self.color = color.upper() # Cor 'BLACK' ou 'RED' em UpperCase
		self.parent = parent # Nó-Pai
		# Nós-Filhos maior e menor
		self.leftSon, self.rightSon = leftSon, rightSon
		if self.parent is None:
			self.coloring()
		pass

	# 1.2. Inserção de nó

	def insertNode(self,key):
		# Inserir nó
		node = None	
		if key.lower() < self.key: # Checar filho à esquerda 
			if self.leftSon is None:
			# Não há filho à esquerda
				node = RBNode(key)
				self.leftSon = node
				node.parent = self
			else:
			# Há filho à esquerda (recursão)
				self.leftSon.insertNode(key)
		else: # Checar filho à direita
			if self.rightSon is None:
			# Não há filho à direita
				node = RBNode(key)
				self.rightSon = node
				node.parent = self
			else:
			# Há filho à direita (recursão)
				self.rightSon.insertNode(key)
			
		# Checar Propriedades (Cores e Rotação)
		if node is not None:
			node.coloring()
		pass
	
	#1.4 Busca

	def findNode(self,key):
		if self.key is not None:
			if key.lower() < self.key:
				# A chave encontrada é maior, se existir (recursão)
				if self.leftSon:
					return self.leftSon.findNode(key)
				else:
			 		return None
			elif key.lower() > self.key:
				# A chave encontrada é menor, se existir (recursão)
				if self.rightSon:
					return self.rightSon.findNode(key)
				else:
					return None
			else: # Encontrou a chave existente
				return self
		else:
			print('Chave não encontrada.')
			return None

	# 1.5. Imprimir árvore (preOrder,inOrder,posOrder)
	def preOrder(self):
		print('\'{}\'\t{}'.format(self.key,self.counter))
		if self.leftSon is not None:
			self.leftSon.preOrder()
		if self.rightSon is not None:
			self.rightSon.preOrder()	
		pass

	def inOrder(self):
		if self.leftSon is not None:
			self.leftSon.inOrder()
		print('\'{}\'\t{}'.format(self.key,self.counter))
		if self.rightSon is not None:
			self.rightSon.inOrder()	
		pass
	
	def posOrder(self):
		if self.leftSon is not None:
			self.leftSon.preOrder()
		if self.rightSon is not None:
			self.rightSon.preOrder()	
		print('\'{}\'\t{}'.format(self.key,self.counter))
		pass	

	# 1.6. Balanceamento (rotateLeft,rotateRight,coloring)

	def rotateLeft(self): # Rotação do nó "O filho se torna o pai, e o pai se torna o filho" (Kal-El)
		if self is not None:
			# node é filho direito para fazer a rotação
			node = self.rightSon
			node.parent = self.parent
			# adotar filho de node 
			if node.leftSon is not None: node.leftSon.parent = self
			self.rightSon = node.leftSon 
			# apadrinhado
			self.parent, node.leftSon = node, self
		return self

	def rotateRight(self): # Rotação do nó
		if self is not None:
			# node é filho esquerdo para fazer a rotação
			node = self.leftSon
			node.parent = self.parent
			# adotar filho de node 
			if node.rightSon is not None: node.rightSon.parent = self
			self.leftSon = node.rightSon 
			# apadrinhado
			self.parent, node.rightSon = node, self
		return self

	def coloring(self): # Muda cor do nó
		if self.parent is None:
			self.color = 'BLACK'
		else:
			if self.parent.color is 'BLACK':
				pass
			if self.uncle() is not None:
				if self.uncle().color is 'RED':
					# Tio Vermelho --> Pai e Tio Pretos e Avô Vermelho
					self.parent.color = 'BLACK'
					self.uncle().color = 'BLACK'
					grandpa = self.grandpa()
					grandpa.color = 'RED'
					grandpa.coloring() # Colorir recursivamente
			else:
				node = None
				if self.parent is not None and self.grandpa() is not None:
					if self.key > self.parent.key and self.key <= self.grandpa().key:
						self.parent.rotateLeft()
						node = self.leftSon
					else:
						self.parent.rotateRight()
						node = self.rightSon

				if node is not None:
					node.parent.color = 'BLACK'
					if node.grandpa() is not None:
						node.grandpa().color = 'RED'

					if node.key <= node.parent.key and node.key <= node.grandpa().key:
						node.grandpa().rotateRight()
					else:
						node.grandpa().rotateLeft()
		pass


	# 1.7. Outras funcionalidades (grandpa,uncle,addCount)

	def grandpa(self): # Encontrar o avô
		if self.parent is not None: # Se tem um pai, pode haver um avô
			dad = self.parent
			return dad.parent
		else:
			return None

	def uncle(self): # Encontrar o tio de um nó
		# Comparando chave para determinar se o tio está à esquerda ou direita
		if self.grandpa() is not None:
			if self.key > self.grandpa().key:
				return self.grandpa().leftSon
			else:
				return self.grandpa().rightSon
		else: 
			return None

	def addCounter(self,key): # Adiciona ocorrência da palavra
		if self.findNode(key) is not None:
			# Elemento já inserido -> Incrementar qnt de ocorrencias
			node = self.findNode(key)
			if node.counter > 0:
				node.counter += 1
				return node.counter
			else:
				print('Contador com Erros. {} ocorrências'.format(node.counter))
		else:
			# Inserir elemento (coloring incluso)
			self.insertNode(key)
			return -1 if self.findNode(key) is None else self.findNode(key).counter

############################## MAIN #####################################
# TESTES VIA TERMINAL
if __name__ == '__main__':

	entrada = input('Chave String:\t')
	print('Criando Árvore com chave (raíz) \'{}\'...'.format(entrada))
	arvore = RBNode(entrada,'BLACK')
	
	while True:
		option = int(input('\n\n[1]Inserir(node = chave + [valor])\n[2]Buscar(chave)\n[3]Imprimir Árvore\n[5]Adicionar Ocorrência\t\n'))

		if option == 1:
			key = input('Inserir Chave String\t')
			arvore.insertNode(key)

			if arvore.findNode(key) is not None:
				print('TODO : Checar balanceamento...')
			input('Qualquer tecla.')

		elif option == 2:
			key = input('Buscar Nó por Chave String\t')
			if arvore.findNode(key) is not None: 
				node = arvore.findNode(key)
				print('Nó = {}'.format(node))
				print('Altura = {}'.format(node.height))
				print('\'{}\' tem {} ocorrências'.format(node.key,node.counter))
				print('Pai = \'{}\'\tFilhos = \'{}\',\'{}\''.format\
				(node.parent.key if node.parent is not None else 'None',\
				node.leftSon.key if node.leftSon is not None else 'None',\
				node.rightSon.key if node.rightSon is not None else 'None'))
			else: 
				print('Não encontrado.')
			input('Qualquer tecla.')

		elif option == 3:

			print('PreOrder:')
			arvore.preOrder()
			print('InOrder:')
			arvore.inOrder()
			print('PosOrder:')
			arvore.posOrder()
			input('Qualquer tecla.')
		
		elif option == 4:
			key = input('Buscar Nó por Chave String\t')
			if arvore.findNode(key) is not None: 
				print('Chave \'{}\' tinha {} ocorrências'.format(key,arvore.findNode(key).counter))
				num = arvore.addCount(key)
				print('Chave \'{}\' agora tem {} ocorrências'.format(key,num))
			else: 
				print('Não encontrado. Criando novo nó com a chave \'{}\'...'.format(key))
				arvore.insertNode(key)

			input('Qualquer tecla.')

		else:
			print('opção [{}] inexistente'.format(option))
			break
