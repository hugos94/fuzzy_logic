import numpy as np
import matplotlib.pyplot as plt

def main():
	min_u = 0.0
	max_u = 10.0

	min_A = 1
	max_A = 3
	min_B = 2
	max_B = 4

	pontos = 1000

	discretizacao = 2

	funcao_caracteristica = np.arange(min_u, max_u, discretizacao)
	universo_discurso = [0,1,1,1,0]

	plotGraph(min_u, max_u, funcao_caracteristica, universo_discurso)

def plotGraph(min_u, max_u, funcao_caracteristica, universo_discuro):
	plt.plot(funcao_caracteristica, universo_discurso, 'ro')
	plt.axis([min_u-1, max_u+1, 0, 1.5])
	plt.show()

if __name__ == '__main__':
	main()
