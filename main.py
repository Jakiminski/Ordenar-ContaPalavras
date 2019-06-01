# Imports
import sys ##argv, executable and exit([int or obj])
from util import *
from AVLTree import AVLNode
from RBTree import RBNode
from HashTable import HashTable

# Não-Constantes Globais
MAX_TAM_HASH =  3137 # Num primo entre as potencias de 2: 2048 e 4096  



if __name__ == '__main__' and len(sys.argv) > 1:
	
	i = 0
	for arg in sys.argv: 
		print('sys.argv[{}]: {}'.format(i,arg))
		i += 1
	print('len(sys.argv) = {}\n\n'.format(len(sys.argv)))
	
	# I/O com Arquivos

	#Entrada: Leitura de um arquivo de texto qualquer, contabilizando as palavras
	fileInput = 'input/' + sys.argv[1].lower()
	
	#Saida: Escrever em arquivo, em ordem crescente, uma lista de ocorrências de cada palavra
	fileOutput = 'output/' + sys.argv[1].lower()
	
	# Exemplo: 'poema1.txt' ou 'mysourcecode.txt'
	print('Arquivo de entrada: {}\nArquivo de saída: {}'.format(fileInput,fileOutput))
	
	wordList = getWordList(fileInput)
	print('Todas as palavras do arquivo \'{}\' foram lidas.'.format(fileInput))

	while True:
		optionStr = input('Escolha como armazenar as palavras:\n')
		flag = options_check(optionStr)
		options_show(flag)
		if flag is False:
			break

	# Executar modo escolhido (0/5 modos)
	if optionStr.lower() == 'hash_lista':# Hash com lista-encadeada
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(2/3)
		#Criar Tabela
		size = int(input('Defina o tamanho do Hash. '))
		size = size if size<=MAX_TAM_HASH else 1
		tabela = HashTable(size,'encadeado')

		#Fazer a contagem e armazenar na tabela e/ou lista-encadeada
		for word in wordList:
			tabela.addCounter(word)
		
		#Exibir Saída
		'''
		for i in range(len(tabela.table)):
			print(tabela.table[i].key)
			print(tabela.table[i].counter)
			print(tabela.table[i].status)
			print(tabela.table[i].listaCol)
		print('\'{}\' really works!'.format(optionStr.lower()))
		'''
	elif optionStr.lower() == 'hash_duplo':# Hash Duplo
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(2/3)
		#Criar Tabela
		size = int(input('Defina o tamanho do Hash. '))
		size = size if size>MAX_TAM_HASH else 1
		tabela = HashTable(size,'duplo')
		
		#Fazer a contagem e armazenar na tabela e/ou lista-encadeada
		for word in wordList:
			tabela.addCounter(word)
		
		#Exibir Saida
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	elif optionStr.lower() == 'avl':# Árvore AVL
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(1/3)
		#Criar Árvore AVL
		key = wordList[0]
		arvore = AVLNode(key)
		#Fazer a contagem e armazenar na árvore (wordList[1:])
		for word in wordList[1:]:
			occur = arvore.addCounter(word)
			if occur <= 0:
				print('ERRO: Chave \'{}\' não foi inserida.\n'.format(word))
		
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	elif optionStr.lower() == 'redblack':# Árvore Rubro-Negra
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(1/3)
		#Criar Árvore Rubro-Negra
		key = wordList[0]
		arvore = RBNode(key)
		#Fazer a contagem e armazenar na árvore (wordList[1:len(wordList)])
		for word in wordList[1:]:
			occur = arvore.addCounter(word)
			if occur <= 0:
				print('ERRO: Chave \'{}\' não foi inserida.\n'.format(word))
		
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))
	
	elif optionStr.lower() == 'arvore_b':# Árvore B
		for i in range(0,30): 
			print("\nTO DO:\tArvore B\n")
		# CHAMAR OBJETOS E SUBROTINAS ESPECÍFICAS(0/3)
		#Criar Árvore B
		#Fazer a contagem e armazenar na árvore
		#Exibir Saída
		print('\'{}\' really works!'.format(optionStr.lower()))
	

	else:# Erro
		sys.exit('ERRO: Não há Estrutura de Dados com o tipo informado. \'{}\'.'.format(optionStr))

	optionStr = input('Qualquer tecla para continuar.\t')
	sys.exit(0)

# END MAIN
