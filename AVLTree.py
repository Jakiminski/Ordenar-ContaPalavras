from BSTree import *

class AVLNode(BinNode):#(1/5) (NENHUM BUG)
	# 1.1. Construtor
	def __init__(self,key,height=int(0)):
		super(AVLNode,self).__init__(key) #Super
		self.height = height # Altura do nó
		pass

	# 1.2. Inserção de um nó

	# 1.3. Remoção de um nó na árvore (retorna o nó-filho, reorganizando a estrutura)

	# 1.4. Balanceamento (AVL)

	# 1.5. Outras funcionalidades (altura,balanceFactor,rotateLeft,rotateRight,rotateLR,rotateRL)

	def altura(self): # Altura da árvore = 1 + altura da maior subárvore
		if self is None:
			return -1
		else:
			# Definir subárvore de maior altura
			heightL = self.leftSon.altura()
			heightR = self.rightSon.altura()
			maior = heightL if heightL>=heightR else heightR
			self.height = maior + 1# Atribuir altura relativa do nó
			return maior + 1 # altura >= 0

	def balanceFactor(self): # Fator de balanceamento
		return self.leftSon.altura() - self.rightSon.altura()

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
	'''
	def rotateLR(): # Dupla-Direita
	def rotateRL(): # Dupla-Esquerda
	'''

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
