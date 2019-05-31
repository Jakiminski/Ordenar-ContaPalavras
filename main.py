# Imports
import sys ##argv, executable and exit([int or obj])
from util import *
from AVLTree import AVLNode
from RBTree import RBNode

# Não-Constantes Globais
MAX_TAM_HASH =  23 # Num primo entre as potencias de 2: 16 e 32  



if __name__ == '__main__' and len(sys.argv)>1:
	
	'''
	i = 0
	for arg in sys.argv: 
		print('sys.argv[{}]: {}'.format(i,arg))
		i += 1
	print('len(sys.argv) = {}\n\n'.format(len(sys.argv)))
	'''

	# I/O com Arquivos

	#Entrada: Leitura de um arquivo de texto qualquer, contabilizando as palavras
	fileInput = 'input/' + sys.argv[1].lower()
	
	#Saida: Escrever em arquivo, em ordem crescente, uma lista de ocorrências de cada palavra
	fileOutput = 'output/' + sys.argv[1].lower()
	
	# Exemplo: 'poema1.txt' ou 'mysourcecode.txt'
	print('Arquivo de entrada: {}\nArquivo de saída: {}'.format(fileInput,fileOutput))
	
	wordList = util.getWordList()

	'''	## Anexar palavra à cada estrutura
	for word in wordList:
	'''

	# Selecionar modo
	flag = True;
	while (flag):
		optionStr = str(input('Escolha como armazenar as palavras:\n'))
		flag = options_check(optionStr)
		options_show(flag)

	# Executar modo escolhido (0/5 modos)
	if optionStr.lower() == 'hash_list':# Hash com lista-encadeada
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(1/3)
		#Criar Tabela
		size = int(input('Defina o tamanho do Hash. '))
		size = size if size>MAX_TAM_HASH else 1
		tabela = HashTable(size,'encadeado')
		#Fazer a contagem e armazenar na tabela e/ou lista-encadeada
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))

	elif optionStr.lower() == 'double_hash':# Hash Duplo
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(1/3)
		#Criar Tabela
		size = int(input('Defina o tamanho do Hash. '))
		size = size if size>MAX_TAM_HASH else 1
		tabela = HashTable(size,'duplo')
		#Fazer a contagem e armazenar na tabela
		#Exibir Saida
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	elif optionStr.lower() == 'avl':# Árvore AVL
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(1/3)
		#Criar Árvore AVL
		key = wordList[0]
		arvore = AVLNode(key)
		#Fazer a contagem e armazenar na árvore (wordList[1:len(wordList)])
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	elif optionStr.lower() == 'redblack':# Árvore Rubro-Negra
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(1/3)
		#Criar Árvore Rubro-Negra
		key = wordList[0]
		arvore = RBNode(key)
		#Fazer a contagem e armazenar na árvore (wordList[1:len(wordList)])
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	elif optionStr.lower() == 'b_tree':# Árvore B
		print("\nTO DO:\tArvore B\n")
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(0/3)
		#Criar Árvore B
		#Fazer a contagem e armazenar na árvore
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	else:# Erro
		sys.exit('ERRO: Não há Estrutura de Dados com o tipo informado. {}.'.format(optionStr))

	sys.exit(0)

# END MAIN
