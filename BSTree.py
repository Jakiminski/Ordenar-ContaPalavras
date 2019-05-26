import sys #argv, executable and exit([int or obj])
from util import clear
# BSTree (0/3)
	# 0.Binary-Search (Classe-Mãe) 
	# 1.AVL  (Herança) -- Checar Sobrecarga de Métodos
	# 2.Red Black (Herança)

class BinNode(object): #(4/7) (2/7 -- BUSCA e INSERÇÃO COM DEFEITO)
	# 0.1.Construtor
	def __init__(self,key,value=0,leftSon=None,rightSon=None):
		self.key = key # String com Chave de acesso (ID)
		self.value = value # Integer com Valor a consultar
		# Nós-Filhos maior e menor
		self.leftSon, self.rightSon = leftSon, rightSon 
		pass # IMPORTANTE: __init__ não têm valor de retorno

	# 0.2.Inserção de um nó existente
	def insertNode(self,key,value):
		if key < self.key: # Checar filho à esquerda 
			if self.leftSon is None:
			# Não há filho à esquerda
				node.__init__(key,value)
				self.leftSon = node
			else:
			# Há filho à esquerda (recursão)
				self.leftSon.insertNode(key,value)
		else: # Checar filho à direita
			if self.rightSon is None:
			# Não há filho à direita
				node.__init__(key,value)
				self.rightSon = node
			else:
			# Há filho à direita (recursão)
				self.rightSon.insertNode(key,value)
		pass

	# 0.3.Busca um nó na árvore (retorna o nó, caso encontre)
	def findNode(self,key):
		if key < self.key:
			# A chave encontrada é maior, se existir (recursão)
			return self.leftSon.findNode(key) if self.leftSon else None
		elif key > self.key:
			# A chave encontrada é menor, se existir (recursão)
			return self.rightSon.findNode(key) if self.rightSon else None
		else:
			# Encontrou a chave existente
			print('Chave Encontrada! {}'.format(self.key) if self is not None else 'Chave não encontrada.')
			
			return self

	# 0.4.Remoção de um nó na árvore (retorna o nó, caso encontre)
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
			temp = self.rightSon.menor()
			self.key, self.value = temp.key, temp.value
			self.rightSon.removeMenor()
		return self

	# 0.5.Balanceamento (AVL e RedBlack)

	# 0.6.Imprimir árvore (preOrder,inOrder,postOrder)
	def preOrder(self):
		print('\'{}\'\t{}'.format(self.key,self.value))
		if self.leftSon is not None:
			self.leftSon.preOrder()
		if self.rightSon is not None:
			self.rightSon.preOrder()	
		pass

	def inOrder(self):
		if self.leftSon is not None:
			self.leftSon.inOrder()
		print('\'{}\'\t{}'.format(self.key,self.value))
		if self.rightSon is not None:
			self.rightSon.inOrder()	
		pass
	
	def posOrder(self):
		if self.leftSon is not None:
			self.leftSon.preOrder()
		if self.rightSon is not None:
			self.rightSon.preOrder()	
		print('\'{}\'\t{}'.format(self.key,self.value))
		pass	
	
	# 0.7 Outras funcionalidades (menor, maior, removeMenor)
	def menor(self):
		return self if self.leftSon is None else self.leftSon.menor()

	def maior(self):
		return self if self.rightSon is None else self.rightSon.maior()

	def removeMenor(self):
		if self.leftSon is None:
			# Não há elemento menor que o nó atual
			return self.rightSon # devolve o outro filho no lugar, se existir
		self.leftSon = self.leftSon.removeMenor() # Procura recursivamente o menor
		return self

############################## MAIN #####################################
 # TESTES APENAS
if __name__ == '__main__':

	entrada = input('Chave String.')
	print('Criando Árvore com chave (raíz) \'{}\'...'.format(entrada))
	arvore = BinNode(entrada,int(input('Valor Numérico a inserir')))

	while True:
		option = int(input('[1]Inserir(node = chave + [valor])\n[2]Buscar(chave)\n[3]Remover(chave)\n[4]Imprimir Árvore\n\n'))

		if option == 1:
			key = input('Inserir Chave String')
			value = int(input('Inserir Valor numérico'))
			
			arvore.insertNode(key,value)
			input('Qualquer tecla.')
			clear

		elif option == 2:
			node = arvore.findNode(input('Buscar Nó por Chave String'))
			print('Nó = {}'.format(node))
			print('Chave = {}'.format(node.key))
			print('Valor = {}'.format(node.value))
			input('Qualquer tecla.')
			clear

		elif option == 3:
			arvore.removeNode(input('Chave String para Remoção'))
			print('arvore = {}\n'.format(arvore))
			input('Qualquer tecla.')
			clear

		elif option == 4:
			print('PreOrder:')
			arvore.preOrder()
			print('InOrder:')
			arvore.inOrder()
			print('PosOrder:')
			arvore.posOrder()
			input('Qualquer tecla.')
			clear
		
		
		else: sys.exit('opção {} inexistente'.format(option))


