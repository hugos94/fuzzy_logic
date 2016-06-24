import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
	global min_u, max_u, discourse_universe, label

	# value minimo e maximo do universo de discurso
	min_u = 0.0
	max_u = 50.0

	# Cria value de incremento de acolordo com o total de points da discretization
	points = 1000
	discretization = (max_u - min_u) / points

	# Cria lista com 1000 points de discretization no intervalo do universo de discurso
	discourse_universe = np.arange(min_u, max_u + discretization, discretization)

	# Cria matriz com o grau de pertinence, para cada conjunto Fuzzy, de cada value do Universo de Discurso
	pertinence_degree = [[],[],[],[],[]]
	for x in discourse_universe:
		pertinence_degree[0].append(pertinence_a(x))
		pertinence_degree[1].append(pertinence_b(x))
		pertinence_degree[2].append(pertinence_c(x))
		pertinence_degree[3].append(pertinence_d(x))
		pertinence_degree[4].append(pertinence_e(x))


	while (True):
		option = raw_input('Informe o exercicio (b ou c) ou sair (para finalizar programa): ')
		option = option.upper()

		if option == 'B':
			print 'LETRA B:\n'
			label = 'Conjuntos Fuzzy'
			plot_graph(pertinence_degree)

		elif option == 'C':
			print 'LETRA C:\n'
			value = input('Informe um valor para a temperatura: ')
			if value < min_u or value > max_u:
				print 'O valor informado nao pertencente ao Universo de Discurso!'
				continue
			label = 'Conjuntos Fuzzy ativos para a temperatura = ' + str(value)
			new_pertinence_degree = belongs_to_set(pertinence_degree, value)
			plot_graph(new_pertinence_degree)
		elif option == 'SAIR':
			print 'Encerrando o programa...'
			break
		else:
			print 'Comando nao valido!'


def pertinence_a(value):
	if value < 5:
		return 1
	elif value >= 5 and value < 15:
		return (15.0 - value) / 10.0
	else:
		return 0


def pertinence_b(value):
	if value < 5:
		return 0
	elif value >= 5 and value < 15:
		return (value - 5.0) / 10.0
	elif value >= 15 and value <= 25:
		return (25.0 - value) / 10.0
	else:
		return 0


def pertinence_c(value):
	if value < 15:
		return 0
	elif value >= 15 and value < 25:
		return (value - 15.0) / 10.0
	elif value >= 25 and value <= 35:
		return (35.0 - value) / 10.0
	else:
		return 0


def pertinence_d(value):
	if value < 25:
		return 0
	elif value >= 25 and value < 35:
		return (value - 25.0) / 10.0
	elif value >= 35 and value <= 45:
		return (45.0 - value) / 10.0
	else:
		return 0


def pertinence_e(value):
	if value >= 45:
		return 1
	elif value >= 35 and value < 45:
		return (value - 35.0) / 10.0
	else:
		return 0


def belongs_to_set(pertinence_degree, value):
	""
	new_pertinence_degree = []

	a = pertinence_a(value)
	b = pertinence_b(value)
	c = pertinence_c(value)
	d = pertinence_d(value)
	e = pertinence_e(value)

	if a == 0:
		new_pertinence_degree.append([])
	else:
		new_pertinence_degree.append(pertinence_degree[0])

	if b == 0:
		new_pertinence_degree.append([])
	else:
		new_pertinence_degree.append(pertinence_degree[1])

	if c == 0:
		new_pertinence_degree.append([])
	else:
		new_pertinence_degree.append(pertinence_degree[2])

	if d == 0:
		new_pertinence_degree.append([])
	else:
		new_pertinence_degree.append(pertinence_degree[3])

	if e == 0:
		new_pertinence_degree.append([])
	else:
		new_pertinence_degree.append(pertinence_degree[4])

	return new_pertinence_degree


def plot_graph(pertinence_degree):
	if pertinence_degree is None:
		print 'Conjunto(s) vazio(s)!!'
		return

	legenda = []
	for i,funcao in enumerate(pertinence_degree):
		if not funcao:
			continue
		elif i == 0:
			color = 'gray'
			label = 'F_A -> Muito Baixa'
		elif i == 1:
			color = 'yellow'
			label = 'F_B -> Baixa'
		elif i == 2:
			color = 'red'
			label = 'F_C -> Media'
		elif i == 3:
			color = 'blue'
			label = 'F_D -> Alta'
		elif i == 4:
			color = 'black'
			label = 'F_E -> Muito Alta'

		plt.plot(discourse_universe, funcao, color=color)
		legenda.append(mpatches.Patch(color=color, label=label))

	plt.legend(handles=legenda)

	plt.xticks(np.arange(min_u, max_u+2, 1.0))
	plt.yticks(np.arange(0, 2.5, 1))

	axes = plt.gca()
	axes.set_title(label)
	axes.set_xlabel('Temperatura:')
	axes.set_ylabel('Grau de Pertinencia:')

	plt.show()


if __name__ == '__main__':
    main()
