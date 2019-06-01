# Utilitarios (2/4)

import sys #.argv, .executable and .exit([int or obj])
import os # .system, .name ( for OperationalSystem), 
import random #.seed(),.randint(),.randrange(),.shuffle(obj)


# 1. OPTIONS

#1.0. Limpa console/terminal # LAMBDA FUNCTION
def clear():
	os.system('cls' if os.name=='nt' else 'clear') # cls for Windows, clear for other OS
	pass

#1.1. Imprime opções de escolha da estrutura de dados
def options_show(boo):
		if boo: 
			print('Insira:\n\'hash_lista\', \'hash_duplo\', \'avl\', \'redblack\' ou \'arvore_b\'.')
		else:
			print('Iniciando...')
		pass

#1.2. Checa Se imprime as opcoes ou continua loop
#Retorna um boolean para controle de loop
def options_check(str1):
	if (str1.lower() == 'hash_lista') or (str1.lower() == 'hash_duplo'):
		return False #parar o loop
	elif (str1.lower() == 'avl') or (str1.lower() == 'redblack') or (str1.lower() == 'arvore_b'):
		return False #parar o loop
	else: 
		return True # continuar o loop

#1.3. Conversor de string para valor numérico 
def stringToNumber(word):
	sumChar = 0 # somatório
	for letter in word:
		sumChar += ord(letter) # conversão de cada caractere
	return sumChar # valor final da soma

#1.4. Lê e recebe palavras do arquivo fonte (split, sprint)
def getWordList(string):
	print('Gerando lista de palavras... {}'.format(string))
	wordList = [] # lista vazia
	with open(string,'r') as file:
		lines = file.readlines()# lendo 1 linha por vez
		for line in lines:
			wordList.extend(strListNoCommaOrDot(line))
		print(wordList)
		return wordList

#1.5. Recebe texto e gera lista de palavras, sem pontuação e sem CASEUPPER
def strListNoCommaOrDot(string):
	Lista = string.split() # Separa as palavras, com delimitador ' ' (blankspace)
	wordList = [] # Lista de palavras
	for word in Lista:
	    wordList.append(word.strip('.,;_><+-="\'')) # Retira pontuações de cada palavra
	return wordList

#1.6. Escreve arquivo de saída
def outputFile(string):
	pass


# 2. QUICKSORT

'''
QuickSort para ordem crescente.
Args: altera o vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: Divisão(Dividir para conquistar)
[NÃO ESTÁVEL] -- O(n log n) 
	

'''
def quickSort(vet,inicio,fim):
	# inicio e fim são índices da partição
	if inicio<fim:
		# PASSO BASE: método particiona
		index = particionaAleatorio(vet,inicio,fim) # índice do pivô

		# PASSO RECURSIVO
		quickSort(vet,inicio,index-1) #elementos à esquerda do pivô
		quickSort(vet,index+1,fim) #elementos à direita do pivô
	return vet

'''
Particionamento, excluindo o pivô um nível acima da pilha de execução
Args: vetor e índices de início e fim de cada partição
Returns: O índice do pivô na lista/vetor
'''
def particionaFim(vet,inicio,fim):
	i = inicio-1 #index do menor elemento
	pivot = vet[fim] #pivô
	for j in range(inicio,fim):
		if vet[j]<=pivot:
			i += 1
			vet[i],vet[j] = vet[j],vet[i] #swap
	vet[i+1],vet[fim] = vet[fim],vet[i+1] #swap
	return i+1 #será índice do pivô no vetor

def particionaAleatorio(vet,inicio,fim):
	# Número aleatório DA PARTIÇÃO
	random.seed()
	i = random.randint(inicio,fim) #index do pivô (vet[i])
	# trocar o pivô e o último elemento
	vet[i],vet[fim] = vet[fim],vet[i]
	# executar outro método de partição
	return particionaFim(vet,inicio,fim)

'''
if __name__ == '__main__':

	vetor = [5,9,6,4,4,2,0,4,3,2,6,1]# lista indexada

	print('Antes: ')
	print(vetor)
	print('Aplicando o QuickSort.')
	vetor = quickSort(vetor,0,len(vetor)-1) #arg está implícito
	print('Após: ')
	print(vetor)
'''

# 3.INPUT FILE

# 4.OUTPUT FILE

#END Utilitários
