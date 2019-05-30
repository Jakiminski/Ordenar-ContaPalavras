# RedBlack Tree

class RBNode(object):#(0/5) (NENHUM BUG)
	# 1.1. Construtor
	def __init__(self,key,color='RED',father=None,leftSon=None,rightSon=None):
		self.key = key.lower() # A palavra lida é a própria chave  em Lowercase
		self.counter = 1 # conta ocorrências de key no arquivo
		self.color = color.upper() # Cor 'BLACK' ou 'RED' em UpperCase

		self.father = father # Nó-Pai
		# Nós-Filhos maior e menor
		self.leftSon, self.rightSon = leftSon, rightSon
		pass

	# 1.2. Inserção de nó

	def insertNode(self,key):

		# Inserir nó	
		if key.lower() < self.key: # Checar filho à esquerda 
			if self.leftSon is None:
			# Não há filho à esquerda
				node = RBNode(key)
				self.leftSon = node
				node.father = self
			else:
			# Há filho à esquerda (recursão)
				self.leftSon.insertNode(key)
		else: # Checar filho à direita
			if self.rightSon is None:
			# Não há filho à direita
				node = RBNode(key)
				self.rightSon = node
				node.father = self
			else:
			# Há filho à direita (recursão)
				self.rightSon.insertNode(key)

		# Corrigir Inserção (CASE 1 é raiz PRETA, pois não tem pai)
		if node.father is not None: # CASE 2,3,4
			# CASE 2 -- Tio é vermelho --> Recolorir Pai, Tio e Avô
			if node.father.father is not None: 
				grandpa = node.father.father
				
				
				if node.father is grandpa.leftSon: # Tio à direita
					uncle = grandpa.rightSon 
					
				elif node.father is grandpa.rightSon: # Tio à esquerda
					uncle = grandpa.leftSon
				else:
					uncle = None
				if uncle is not None:
					# RECOLORIR PAI, TIO e AVÔ
					if uncle.color is 'RED': 
						node.father.changeColor()
						uncle.changeColor()
						grandpa.changeColor()

			# CASE 3 -- Pai Vermelho --> 
			# CASE 4 -- 
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

	# 1.6. Rotações e mudança de Cor para balanceamento (rotateLeft,rotateRight, changeColor)

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

	def changeColor(self): # Muda cor do nó
		if self is not None:
			color = 'BLACK' if self.color is 'RED' else 'RED'
			self.color = color 
		pass

	# 1.7. Outras funcionalidades (altura,menor, maior, removeMenor, addCount)
	
	def altura(self): # Altura da árvore = 1 + altura da maior subárvore
		if self is None:
			return -1
		else:
			# Definir subárvore de maior altura
			heightL = self.leftSon.altura() if self.leftSon is not None else -1
			heightR = self.rightSon.altura() if self.rightSon is not None else -1
			maior = heightL if heightL>=heightR else heightR
			return maior + 1 # altura >= 0

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
		else: 
			return int(-1)

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
