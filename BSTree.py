import sys #argv, executable and exit([int or obj])

# BSTree (0/3)
	# 0.Binary-Search (Classe-Mãe) 
	# 1.AVL  (Herança) -- Checar Sobrecarga de Métodos
	# 2.Red Black (Herança)

class BinNode(object): #(5/7) (1/7 -- REMOÇÃO COM DEFEITO) (Balanceamento nas classes filhas AVLNode e RBNode)
	# 0.1.Construtor
	def __init__(self,key,counter=int(0),leftSon=None,rightSon=None):
		self.key = key # String com Chave de acesso (ID)
		self.counter = counter # Integer com Valor a consultar
		# Nós-Filhos maior e menor
		self.leftSon, self.rightSon = leftSon, rightSon 
		pass # IMPORTANTE: __init__ não têm valor de retorno

	# 0.2.Inserção de um nó existente
	def insertNode(self,key,counter=int(0)):
		if key < self.key: # Checar filho à esquerda 
			if self.leftSon is None:
			# Não há filho à esquerda
				node = BinNode(key,counter)
				self.leftSon = node
			else:
			# Há filho à esquerda (recursão)
				self.leftSon.insertNode(key,counter)
		else: # Checar filho à direita
			if self.rightSon is None:
			# Não há filho à direita
				node = BinNode(key,counter)
				self.rightSon = node
			else:
			# Há filho à direita (recursão)
				self.rightSon.insertNode(key,counter)
		pass

	# 0.3.Busca um nó na árvore (retorna o nó, caso encontre)
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
		# Encontrou a chave existente
		print('Chave Encontrada! {}'.format(self.key) if self is not None else 'Chave não encontrada.')
		return self

	# 0.4.Remoção de um nó na árvore (retorna o nó-filho, reorganizando a estrutura)
	def removeNode(self,key):
		if key < self.key:
			# A chave encontrada é maior (recursão)
			return self.leftSon.removeNode(key)
		elif key > self.key:
			# A chave encontrada é menor (recursão)
			return self.rightSon.removeNode(key)
		else:
			# Encontrou a chave existente
			# É preciso remover o nó e "remendar" a árvore
			if self.rightSon is None:
				return self.leftSon # filho não-nulo
			if self.leftSon is None:
				return self.rightSon # filho não-nulo, (ou None, caso folha)
			# copiar o nó substituto, ao invés de removê-lo - Nó tem 2 filhos
			temp = self.rightSon.menor() #encontra menor chave
			self.key, self.counter = temp.key, temp.counter
			self.rightSon.removeMenor() # Remove menor chave
		return self

	# 0.5.Balanceamento (AVL e RedBlack)

	# 0.6.Imprimir árvore (preOrder,inOrder,postOrder)
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
	
	# 0.7 Outras funcionalidades (menor, maior, removeMenor, addCount)
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
			if node.counter >= 0:
				node.counter += 1
				return node.counter
			else:
				print('Contador menor que 0.')
		else: return int(-1)
			


############################## MAIN #####################################
 # TESTES APENAS
if __name__ == '__main__':

	entrada = input('Chave String:\t')
	print('Criando Árvore com chave (raíz) \'{}\'...'.format(entrada))
	arvore = BinNode(entrada,int(input('Valor Numérico a inserir:\t')))

	while True:
		option = int(input('[1]Inserir(node = chave + [valor])\n[2]Buscar(chave)\n[3]Remover(chave)\n[4]Imprimir Árvore\n[5]Adicionar Ocorrência\t\n'))

		if option == 1:
			key = input('Inserir Chave String\t')
			counter = int(input('Inserir Valor numérico\t'))
			
			arvore.insertNode(key,counter)
			input('Qualquer tecla.')

		elif option == 2:
			key = input('Buscar Nó por Chave String\t')
			if arvore.findNode(key) is not None: 
				node = arvore.findNode(key)
				print('Nó = {}'.format(node))
				print('Chave = {}'.format(node.key))
				print('Valor = {} ocorrências'.format(node.counter))
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

		else: sys.exit('opção [{}] inexistente'.format(option))


