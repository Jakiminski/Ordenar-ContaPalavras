from BSTree import *

class AVLNode(object):#(1/5) (NENHUM BUG)
	# 1.1. Construtor
	def __init__(self,key,height,father=None,leftSon=None,rightSon=None):
		self.key = key # A palavra lida é a própria chave 
		self.counter = 1 # conta ocorrências de key no arquivo
		self.father = father# Nó-Pai
		# Nós-Filhos maior e menor
		self.leftSon, self.rightSon = leftSon, rightSon
		self.height = height # Altura do nó
		pass

	# 1.4. Balanceamento (AVL)

	def insertNode(self,key):
		# Inserir nó	
		if key < self.key: # Checar filho à esquerda 
			if self.leftSon is None:
			# Não há filho à esquerda
				node = BinNode(key)
				self.leftSon = node
				node.father = self
			else:
			# Há filho à esquerda (recursão)
				self.leftSon.insertNode(key)
		else: # Checar filho à direita
			if self.rightSon is None:
			# Não há filho à direita
				node = BinNode(key)
				self.rightSon = node
				node.father = self
			else:
			# Há filho à direita (recursão)
				self.rightSon.insertNode(key)
		pass

	def balance(self):
		# Checar balanceamento
		print('FUNCIONAAAAAAAAAAA')
		dir(self)
		fator = self.balanceFactor()
		# Executar balanceamento
		if fator > 1:
			if self.leftSon.balanceFactor() > 0:
				self.rotateRight()
			else:
				self.rotateLR()
		elif fator < -1:
			if self.rightSon.balanceFactor() < 0:
				self.rotateLeft()
			else:
				self.rotateRL()
		pass


	# 1.5. Outras funcionalidades (rotateLeft,rotateRight,rotateLR,rotateRL)

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
		else: return None

	def rotateRL(self): # Rotação Dupla-Esquerda
		if self is not None:
			self.rightSon.rotateRight()
			return self.rotateLeft()
		else: return None
	

############################## MAIN #####################################
# TESTES VIA TERMINAL
if __name__ == '__main__':

	entrada = input('Chave String:\t')
	print('Criando Árvore com chave (raíz) \'{}\'...'.format(entrada))
	arvore = AVLNode(entrada)
	
	while True:
		option = int(input('[1]Inserir(node = chave + [valor])\n[2]Buscar(chave)\n[3]Remover(chave)\n[4]Imprimir Árvore\n[5]Adicionar Ocorrência\t\n'))

		if option == 1:
			arvore.insertNode(input('Inserir Chave String\t'))
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
			arvore.removeNode(input('Chave String para Remoção\t'))
			print('arvore = {}'.format(arvore))
			input('Qualquer tecla.')

		elif option == 4:
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
				print('Não encontrado.')
			input('Qualquer tecla.')

		else:
			print('opção [{}] inexistente'.format(option))
			break
