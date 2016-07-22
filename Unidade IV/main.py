import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    global min_u, max_u

    while(True):
        option = raw_input('Informe a questao a ser executada (7, 8, 9 ou sair): ')
        option = option.upper()

        if option == '7': # Questao 7
            print '\nQuestao 7:'
            fuzzy_set = fuzzy_input()
            alpha_value = float(raw_input('Informe um valor para alfa: '))
            print '\nAltura = ' + str(height_fuzzy_set(fuzzy_set))
            print 'Suporte = ' + str(suport_fuzzy_set(fuzzy_set))
            print 'Fronteiras = ' + str(boundaries_fuzzy_set(fuzzy_set))
            print 'Nucleo = ' + str(core_fuzzy_set(fuzzy_set))
            print 'Pontos de Crossover = ' + str(crossover_points(fuzzy_set))
            print 'Alfa-corte = ' + str(alpha_cut(fuzzy_set, alpha_value))
            print 'Cardinalidade = ' + str(fuzzy_cardinality(fuzzy_set))
            print 'Normalizacao = ' + str(normalization(fuzzy_set)) + '\n'

        elif option == '8': # Questao 8
            print '\nQuestao 8: '
            create_discourse_universe()
            print '\nInforme 2 Conjuntos Fuzzy: '
            fuzzy_set_1 = fuzzy_input()
            fuzzy_set_2 = fuzzy_input()
            print 'Igualdade: ' + str(equality(fuzzy_set_1, fuzzy_set_2))
            print 'Inclusao: ' + str(inclusion(fuzzy_set_1, fuzzy_set_2))

        elif option == '9': # Questao 9
            print '\n Questao 9:'
            create_discourse_universe()
            points = 20.0 # Quantidades de pontos de discretizacao
            discretization = (max_u - min_u) / points
            discourse_universe = np.arange(min_u, max_u + discretization, discretization)

            print 'F1 = (x, 1, 3, 5) - Pertinencia Triangular '
            operations(funcao_triangular(discourse_universe, 1.0, 3.0, 5.0))
            print 'F2 = (x, 1, 2, 4) - Pertinencia Triangular '
            operations(funcao_triangular(discourse_universe, 1.0, 2.0, 4.0))
            print 'F3 = (x, 1, 4, 6) - Pertinencia Triangular '
            operations(funcao_triangular(discourse_universe, 1.0, 4.0, 6.0))
            print 'F4 = (x, 3, 4, 5, 7) - Pertinencia Trapezoidal '
            operations(funcao_trapezoidal(discourse_universe, 3.0, 4.0, 5.0, 7.0))
            print 'F5 = (x, 1, 3, 2) - Pertinencia Gaussiana '
            operations(funcao_gaussiana(discourse_universe, 1.0, 2.0))

        else:
            print 'Finalizando o programa...'
            break;

def fuzzy_input():
    input_set = raw_input('Informe o conjunto fuzzy (Ex.: 0.4/3 + 0.1/4 + 0.6/5): ')
    input_set = input_set.replace(" + ", "|")
    input_set = input_set.split("|")
    fuzzy_set = {}
    for element in input_set:
        el = element.split('/')
        fuzzy_set[el[1]] = float(el[0])
    return fuzzy_set

def height_fuzzy_set(fuzzy_set): #Retorna a altura do conjunto fuzzy
    return max(fuzzy_set.values())

def suport_fuzzy_set(fuzzy_set): #Retorna o conjunto suporte do conjunto fuzzy
    elements = []
    for key in fuzzy_set.keys():
        if fuzzy_set[key] != 0.0:
            elements.append(key)
    return elements

def boundaries_fuzzy_set(fuzzy_set): # Retorna as fronteiras do conjunto fuzzy
    elements = []
    for key in fuzzy_set.keys():
        if fuzzy_set[key] > 0.0 and fuzzy_set[key] < 1.0:
            elements.append(key)
    return elements

def core_fuzzy_set(fuzzy_set): # Retorna o nucleo do conjunto fuzzy
    elements = []
    for key in fuzzy_set.keys():
        if fuzzy_set[key] == 1.0:
            elements.append(key)
    return elements

def crossover_points(fuzzy_set): # Retorna os pontos de crossover
    elements = []
    for key in fuzzy_set.keys():
        if fuzzy_set[key] == 0.5:
            elements.append(key)
    return elements

def alpha_cut(fuzzy_set, alpha_value): # Realiza o alfa corte do conjunto fuzzy a partir de um alfa especificado
    if alpha_value < 0.0 or alpha_value > 1.0:
        return 'Valor alfa invalido!'
    else:
        elements = []
        for key in fuzzy_set.keys():
            if fuzzy_set[key] >= alpha_value:
                elements.append(key)
        return elements

def fuzzy_cardinality(fuzzy_set): # Retorna a cardinalidade do conjunto fuzzy
    fuzzy_cardinality = 0.0
    for key in fuzzy_set.keys():
        fuzzy_cardinality += fuzzy_set[key]
    return fuzzy_cardinality

def normalization(fuzzy_set): # Normaliza o conjunto fuzzy
    height = height_fuzzy_set(fuzzy_set)
    if height == 0.0 or not fuzzy_set:
        return 'O conjunto fuzzy e vazio!'
    else:
        if height == 1.0:
            return 'O conjunto ja esta normalizado!'
        else:
            for key in fuzzy_set:
                fuzzy_set[key] = fuzzy_set[key] / height
            return fuzzy_set

def create_discourse_universe(): # Cria o Universo de Discurso
    global min_u, max_u
    input_set = raw_input('Informe o inicio e o final do Universo de Discurso (Ex.: 0-4): ')
    input_set = input_set.split('-')
    min_u = int(input_set[0])
    max_u = int(input_set[1])

def fill_set(fuzzy_set): # Retorna um conjunto fuzzy com todos os elementos presentes no universo de discurso
    global min_u, max_u
    for key in range(min_u, max_u+1):
        if not str(key) in fuzzy_set.keys():
            fuzzy_set[key] = 0.0
    return fuzzy_set

def equality(fuzzy_set_1, fuzzy_set_2): # Retorna o grau de igualdade entre dois conjuntos fuzzy

    msg = ''
    equality_degree = 0.0
    fuzzy_set_1 = fill_set(fuzzy_set_1)
    fuzzy_set_2 = fill_set(fuzzy_set_2)

    for key in fuzzy_set_1:
        if fuzzy_set_1[key] != fuzzy_set_2[key]:
            if abs(fuzzy_set_1[key] - fuzzy_set_2[key]) > equality_degree:
                equality_degree = abs(fuzzy_set_1[key] - fuzzy_set_2[key])

    if equality_degree == 0.0:
        return 'Os conjuntos fuzzy sao identicos! Grau de Igualdade = ' + str(1 - equality_degree)
    else:
        return 'Os conjuntos fuzzy sao diferentes! Grau de Igualdade = ' + str(1 - equality_degree)

def inclusion(fuzzy_set_1, fuzzy_set_2):
    global max_u, min_u
    discourse_universe_cardinality = float(max_u) - float(min_u) + 1.0
    inclusion_degree = 0.0

    fuzzy_set_1 = fill_set(fuzzy_set_1)
    fuzzy_set_2 = fill_set(fuzzy_set_2)

    for key in fuzzy_set_1:
        if fuzzy_set_1[key] <= fuzzy_set_2[key]:
            inclusion_degree += 1.0
        else:
            inclusion_degree += 1.0 - (fuzzy_set_1[key] - fuzzy_set_2[key])

    inclusion_degree = inclusion_degree / discourse_universe_cardinality

    if inclusion_degree == 1.0:
        return 'O conjunto 1 esta incluido no conjunto 2. Grau de Inclusao = ' + str(inclusion_degree)
    else:
        return 'O conjunto 1 nao esta incluido no conjunto 2. Grau de Inclusao = ' + str(inclusion_degree)

def funcao_triangular(discourse_universe, a, m, b):
    fuzzy_set = {}
    for x in discourse_universe:
        if x >= a and x < m:
            fuzzy_set[str(x)] = ((x-a)/(m-a))
        elif x >= m and x <= b:
            fuzzy_set[str(x)] = ((b-x)/(b-m))
        else:
            fuzzy_set[str(x)] = 0.0

    return fuzzy_set

def funcao_trapezoidal(discourse_universe, a, m, n, b):
    fuzzy_set = {}
    for x in discourse_universe:
        if x >= a and x < m:
            fuzzy_set[str(x)] = ((x-a)/(m-a))
        elif x >= m and x < n:
            fuzzy_set[str(x)] = 1.0
        elif x >= n and x <= b:
            fuzzy_set[str(x)] = ((b-x)/(b-n))
        else:
            fuzzy_set[str(x)] = 0.0

    return fuzzy_set

def funcao_gaussiana(discourse_universe, m, gama):
    fuzzy_set = {}
    for x in discourse_universe:
        potential = math.pow(x - m, 2)
        potential = potential / math.pow(gama, 2)
        fuzzy_set[str(x)] = math.exp(-1 * potential)
    return fuzzy_set

def operations(fuzzy_set):
    print 'Altura = ' + str(height_fuzzy_set(fuzzy_set))
    print 'Suporte = ' + str(suport_fuzzy_set(fuzzy_set))
    print 'Nucleo = ' + str(core_fuzzy_set(fuzzy_set))
    print 'Fronteiras = ' + str(boundaries_fuzzy_set(fuzzy_set))
    print 'Cardinalidade = ' + str(fuzzy_cardinality(fuzzy_set))
    print 'Pontos de crossover = ' + str(crossover_points(fuzzy_set))
    print 'Alfa-corte (= 0.0) = ' + str(alpha_cut(fuzzy_set, 0.0))
    print 'Alfa-corte (= 0.2) = ' + str(alpha_cut(fuzzy_set, 0.2))
    print 'Alfa-corte (= 0.4) = ' + str(alpha_cut(fuzzy_set, 0.4))
    print 'Alfa-corte (= 0.6) = ' + str(alpha_cut(fuzzy_set, 0.6))
    print 'Alfa-corte (= 0.8) = ' + str(alpha_cut(fuzzy_set, 0.8))
    print 'Alfa-corte (= 1.0) = ' + str(alpha_cut(fuzzy_set, 1.0))
    print '\n'


if __name__ == '__main__':
    main()
