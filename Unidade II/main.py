import numpy as np
import matplotlib.pyplot as plt

global min_u, max_u, discourse_universe, label

def main():
	global min_u, max_u, discourse_universe, label

	min_u = 0.0
	max_u = 10.0

	min_a = 1
	max_a = 3
	min_b = 2
	max_b = 4

	points = 1000
	discretization = (max_u - min_u )/ points

	discourse_universe = np.arange(min_u, max_u + discretization, discretization)

	# Cria lista com o menor e maior valor de cada conjunto
	set_a = [min_a, max_a]
	set_b = [min_b, max_b]

	while (True):

		option = raw_input('Informa a letra da questao a ser iniciada (a-e) ou exit (para finalizar): ')
		option = option.upper()

		if option == 'A':
			print 'Questao A\n'
			label = 'Conjunto A:'
			set_mapping(set_a)
			label = 'Conjunto B:'
			set_mapping(set_b)

		elif option == 'B':
			print 'Questao B\n'
			value = input('Informe um valor:')
			belongs_to_set('A', set_a, value)
			belongs_to_set('B', set_b, value)

		elif option == 'C':
			print 'Questao C\n'
			titulo = 'Conjunto A U B'
			union(set_a, set_b)

		elif option == 'D':
			print 'Questao D\n'
			label = 'Conjunto A "intersecao" B'
			intersection(set_a, set_b)

		elif option == 'E':
			print 'Questao E\n'
			label = 'Complemento de A:'
			complement(set_a)
			label = 'Complemento de B:'
			complement(set_b)

		elif option == 'EXIT':
			print 'Finalizando programa...'
			break

		else:
			print 'Comando nao encontrado!'

def union(set_a, set_b):
	union_set = []
	characteristic_function_a = set_mapping(set_a,True)
	characteristic_function_b = set_mapping(set_b,True)

	for i in range(len(discourse_universe)):
		value = max(characteristic_function_a[i], characteristic_function_b[i])
		union_set.append(value)

	plot_graph(union_set)

def intersection(set_a, set_b):
	intersection_set = []
	characteristic_function_a = set_mapping(set_a,True)
	characteristic_function_b = set_mapping(set_b,True)

	for i in range(len(discourse_universe)):
		value = min(characteristic_function_a[i], characteristic_function_b[i])
		intersection_set.append(value)

	plot_graph(intersection_set)

def complement(set_x):
	complement_set = []
	characteristic_function = set_mapping(set_x,True)

	for i in range(len(discourse_universe)):
		value = 1 - characteristic_function[i]
		complement_set.append(value)

	plot_graph(complement_set)

def belongs_to_set(set_label, set_x, value):

	if not set_x:
		print "Conjunto vazio!"
	else:
		if min_u <= value and max_u >= value:
			if set_x[0] <= value and set_x[1] >= value:
				print 'O valor informado pertence ao conjunto ', set_label ,' [', set_x[0], ',', set_x[1], ']'
			else:
				print 'O valor informado nao pertence ao conjunto ', set_label ,' [', set_x[0], ',', set_x[1], ']'
		else:
			print 'O valor informado nao pertence ao Universo de Discurso!'

def set_mapping(set_x, retorno=False):
	if not set_x:
		print "Conjunto Vazio!"
	else:
		characteristic_function = []

		for i in range(len(discourse_universe)):
			if discourse_universe[i] >= set_x[0] and discourse_universe[i] <= set_x[1]:
				characteristic_function.append(1)
			else:
				characteristic_function.append(0)
	if retorno:
		return characteristic_function

	plot_graph(characteristic_function)

def plot_graph(characteristic_function):
	plt.plot(discourse_universe, characteristic_function, 'ro', color='green')

	plt.xticks(np.arange(min_u, max_u+2, 1.0))
	plt.yticks(np.arange(0,2.5, 1))

	axes = plt.gca()
	axes.set_xlabel('Universo de Discurso')
	axes.set_ylabel('Funcao Caracteristica')
	axes.set_title(label)

	plt.show()

if __name__ == '__main__':
	main()
