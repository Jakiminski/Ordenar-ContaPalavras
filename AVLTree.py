# AVL Tree

class AVLNode(object):#(1/5) (NENHUM BUG)
	# 1.1. Construtor

	def __init__(self,key,height=int(0),father=None,leftSon=None,rightSon=None):
		self.key = key # A palavra lida é a própria chave 
		self.counter = 1 # conta ocorrências de key no arquivo
		self.height = height # Altura do nó

		self.father = father # Nó-Pai
		# Nós-Filhos maior e menor
		self.leftSon, self.rightSon = leftSon, rightSon

		pass

	# 1.2. Inserção de nó

	def insertNode(self,key):
		# Inserir nó	
		if key < self.key: # Checar filho à esquerda 
			if self.leftSon is None:
			# Não há filho à esquerda
				node = AVLNode(key)
				self.leftSon = node
				node.father = self
			else:
			# Há filho à esquerda (recursão)
				self.leftSon.insertNode(key)
		else: # Checar filho à direita
			if self.rightSon is None:
			# Não há filho à direita
				node = AVLNode(key)
				self.rightSon = node
				node.father = self
			else:
			# Há filho à direita (recursão)
				self.rightSon.insertNode(key)
		pass
	
	# 1.3. Balanceamento (AVL)

	def balance(self):
		# Checar balanceamento
		fator = self.balanceFactor()
		print('Fator = {}'.format(fator))
		# Executar balanceamento
		if fator > 1:
			if self.leftSon.balanceFactor() > 0:
				print('Executando a rotação à direita (R).')
				self.rotateRight()
			else:
				print('Executando dupla rotação à direita (LR).')
				self.rotateLR()
		elif fator < -1:
			if self.rightSon.balanceFactor() < 0:
				print('Executando rotação à esquerda (L).')
				self.rotateLeft()
			else:
				print('Executando dupla rotação à esquerda (RL).')
				self.rotateRL()
		pass

	#1.4 Busca

	def findNode(self,key):
		if self.key is not None:
			if key < self.key:
				# A chave encontrada é maior, se existir (recursão)
				if self.leftSon:
					return self.leftSon.findNode(key)
				else:
			 		return None
			elif key > self.key:
				# A chave encontrada é menor, se existir (recursão)
				if self.rightSon:
					return self.rightSon.findNode(key)
				else:
					return None
			else: # Encontrou a chave existente
				print('Chave Encontrada! {}'.format(self.key))
		else:
			print('Chave não encontrada.')
		
		return self

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

	# 1.6. Rotações para balanceamento (rotateLeft,rotateRight,rotateLR,rotateRL)

	def rotateLeft(self): # Rotação do nó "O filho se torna o pai, e o pai se torna o filho" (Kal-El)
		if self is not None:
			# node é filho direito para fazer a rotação
			node = self.rightSon
			node.father = self.father
			# adotar filho de node 
			if node.leftSon is not None: node.leftSon.father = self
			self.rightSon = node.leftSon 
			# apadrinhado
			self.father, node.leftSon = node, self
			# atualizar altura dos nós e suas subárvores
			self.altura()
			node.altura()
		return self

	def rotateRight(self): # Rotação do nó
		if self is not None:
			# node é filho esquerdo para fazer a rotação
			node = self.leftSon
			node.father = self.father
			# adotar filho de node 
			if node.rightSon is not None: node.rightSon.father = self
			self.leftSon = node.rightSon 
			# apadrinhado
			self.father, node.rightSon = node, self
			# atualizar altura dos nós e suas subárvores
			self.altura()
			node.altura()
		return self
	
	def rotateLR(self): # Rotação Dupla-Direita
		if self is not None:
			self.leftSon.rotateLeft()
			return self.rotateRight()
		else: 
			return None

	def rotateRL(self): # Rotação Dupla-Esquerda
		if self is not None:
			self.rightSon.rotateRight()
			return self.rotateLeft()
		else:
			return None
	
	# 1.7. Outras funcionalidades (altura,menor, maior, removeMenor, addCount)
	
	def altura(self): # Altura da árvore = 1 + altura da maior subárvore
		if self is None:
			return -1
		else:
			# Definir subárvore de maior altura
			heightL = self.leftSon.altura() if self.leftSon is not None else -1
			heightR = self.rightSon.altura() if self.rightSon is not None else -1
			maior = heightL if heightL>=heightR else heightR
			self.height = maior + 1 # Atribuir altura relativa do nó
			return maior + 1 # altura >= 0

	def balanceFactor(self): # Fator de balanceamento
		altura = (self.leftSon.altura() if self.leftSon is not None else -1) - (self.rightSon.altura() if self.rightSon is not None else -1)
		return altura

	def menor(self): # MENOR CHAVE
		if self.leftSon is None:
			return self
		else: 
			return self.leftSon.menor()

	def maior(self): # MAIOR CHAVE
		if self.rightSon is None:
			return self
		else: 
			return self.rightSon.menor()

	def removeMenor(self): # REMOVE MENOR CHAVE
		if self.leftSon is None:
			# Não há elemento menor que o nó atual
			return self.rightSon # devolve o outro filho no lugar, se existir
		else:
			self.leftSon = self.leftSon.removeMenor() # Procura recursivamente o menor
		return self

	def addCount(self,key):
		if self.findNode(key) is not None:
			node = self.findNode(key)
			if node.counter > 0:
				node.counter += 1
				return node.counter
			else:
				print('Contador menor que 0.')
		else: return int(-1)

############################## MAIN #####################################
# TESTES VIA TERMINAL
if __name__ == '__main__':

	entrada = input('Chave String:\t')
	print('Criando Árvore com chave (raíz) \'{}\'...'.format(entrada))
	arvore = AVLNode(entrada)
	
	while True:
		option = int(input('\n\n[1]Inserir(node = chave + [valor])\n[2]Buscar(chave)\n[3]Imprimir Árvore\n[5]Adicionar Ocorrência\t\n'))

		if option == 1:
			key = input('Inserir Chave String\t')
			arvore.insertNode(key)

			if arvore.findNode(key) is not None:
				print('Checando balanceamento...')
				node = arvore.findNode(key)
				if node.father is not None:
					node.father.balance()
			input('Qualquer tecla.')

		elif option == 2:
			key = input('Buscar Nó por Chave String\t')
			if arvore.findNode(key) is not None: 
				node = arvore.findNode(key)
				print('Nó = {}'.format(node))
				print('Altura = {}'.format(node.height))
				print('\'{}\' tem {} ocorrências'.format(node.key,node.counter))
				print('Pai = \'{}\'\tFilhos = \'{}\',\'{}\''.format\
				(node.father.key if node.father is not None else 'None',\
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
		
		elif option == 5:
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
