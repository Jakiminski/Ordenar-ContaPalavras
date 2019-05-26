from BSTree import BSNode

class AVLNode(BinNode):#(1/5) (NENHUM BUG)
	# 1.1. Construtor
	def __init__(self,height=int(0)):
		BinNode.__init__(key,counter,father,leftSon,rightSon) #Super
		self.height = height # Altura do nó
		pass

	# 1.2. Inserção de um nó

	# 1.3. Remoção de um nó na árvore (retorna o nó-filho, reorganizando a estrutura)

	# 1.4. Balanceamento (AVL)

	# 1.5. Outras funcionalidades (rotateLeft,rotateRight,rotateLR,rotateRL)
	