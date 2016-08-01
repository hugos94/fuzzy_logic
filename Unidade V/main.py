import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    global min_u, max_u, discourse_universe, label

    while (True):
        option = raw_input('Informe a questao a ser executada (6, 7, 8 ou sair): ')
        option = option.upper()

        if option == '6':
            print '\nQuestao 6: '
            create_discourse_universe()
            fuzzy_set_1 = read_fuzzy_set()
            fuzzy_set_2 = read_fuzzy_set()

            print 'Intersecao: '
            fuzzy_intersection(fuzzy_set_1, fuzzy_set_2)
            print 'Intersecao.\n'

            print 'Uniao: '
            fuzzy_union(fuzzy_set_1, fuzzy_set_2)
            print 'Uniao.\n'

            print 'Complemento: '
            op = raw_input('Escolha um entre os conjuntos fuzzy inseridos anteriormente (1 ou 2): ')
            if op == '1':
                fuzzy_set = set_fuzzy_1
            elif op == '2':
                fuzzy_set = set_fuzzy_2
            print '\nInforme os valores para o complemento: '
            a = raw_input('Digite um valor para treshold, entre 0 e 1: ')
            l = raw_input('Digite um valor para lambda, maior que -1: ')
            w = raw_input('Digite um valor para W, maior que 0: ')
            fuzzy_complement(fuzzy_set, a, l, w)
            print 'Complemento.\n'

        elif option == '7':
            break

        elif option == '8':
            break

        else:
            print 'Finalizando o programa...'
            break

def fuzzy_intersection(fuzzy_set_1, fuzzy_set_2, msg=True):
    fuzzy_set_1 = fill_set(fuzzy_set_1)
    fuzzy_set_2 = fill_set(fuzzy_set_2)

    fuzzy_set_minimum = {}
    fuzzy_set_product = {}
    fuzzy_set_lukasiewicz = {}
    fuzzy_set_drastic_product = {}

    for key in fuzzy_set_1:
        fuzzy_set_minimum[key] = min(fuzzy_set_1[key], fuzzy_set_2[key])
        fuzzy_set_product[key] = fuzzy_set_1[key] * fuzzy_set_2[key]
        fuzzy_set_lukasiewicz[key] = max(fuzzy_set_1[key] + fuzzy_set_2[key] - 1.0, 0.0)

        if fuzzy_set_1[key] == 1.0:
            fuzzy_set_drastic_product[key] = fuzzy_set_2[key]
        elif fuzzy_set_2[key] == 1.0:
            fuzzy_set_drastic_product[key] = fuzzy_set_1[key]
        else:
            fuzzy_set_drastic_product[key] = 0.0

    if msg:
        print 'Minimo: ' + fuzzy_set_sort(fuzzy_set_minimum)
        print 'Produto: ' + fuzzy_set_sort(fuzzy_set_product)
        print 'Lukasiewicz: ' + fuzzy_set_sort(fuzzy_set_lukasiewicz)
        print 'Produto Drastico: ' + fuzzy_set_sort(fuzzy_set_drastic_product)
    else:
        results = {}
        results['minimo'] = fuzzy_set_minimum
        results['produto'] = fuzzy_set_product
        results['lukasiewicz'] = fuzzy_set_lukasiewicz
        results['produto_drastico'] = fuzzy_set_drastic_product
        return results

def fuzzy_union(fuzzy_set_1, fuzzy_set_2, msg=True): # Retorna a uniao entre dois conjuntos fuzzy
    fuzzy_set_1 = fill_set(fuzzy_set_1)
    fuzzy_set_2 = fill_set(fuzzy_set_2)

    fuzzy_set_maximum = {}
    fuzzy_set_probabilistic_sum = {}
    fuzzy_set_lukasiewicz = {}
    fuzzy_set_drastic_sum = {}

    for key in fuzzy_set_1:
        fuzzy_set_maximum[key] = max(fuzzy_set_1[key], fuzzy_set_2[key])
        fuzzy_set_probabilistic_sum[key] = (fuzzy_set_1[key] + fuzzy_set_2[key]) - (fuzzy_set_1[key] * fuzzy_set_2[key])
        fuzzy_set_lukasiewicz[key] = min(fuzzy_set_1[key] + fuzzy_set_2[key], 1.0)

        if fuzzy_set_1[key] = 0.0:
            fuzzy_set_drastic_sum[key] = fuzzy_set_2[key]
        elif fuzzy_set_2[key] = 0.0:
            fuzzy_set_drastic_sum[key] = fuzzy_set_1[key]
        else:
            fuzzy_set_drastic_sum[key] = 1.0

    if msg:
        print 'Maximo: ' + fuzzy_set_sort(fuzzy_set_maximum)
        print 'Soma Probabilistica: ' + fuzzy_set_sort(fuzzy_set_probabilistic_sum)
        print 'Lukasiewicz: ' + fuzzy_set_sort(fuzzy_set_lukasiewicz)
        print 'Soma Drastica: ' + fuzzy_set_sort(fuzzy_set_drastic_sum)
    else:
        results = {}
        results['maximo'] = fuzzy_set_maximum
        results['soma_probabilistica'] = fuzzy_set_probabilistic_sum
        results['lukasiewicz'] = fuzzy_set_lukasiewicz
        results['soma_drastica'] = fuzzy_set_drastic_sum
        return results

def fuzzy_complement(fuzzy_set, a, l, w, msg=True):
    fuzzy_set = fill_set(fuzzy_set)

    fuzzy_set_standard = {}
    fuzzy_set_threshold = {}
    fuzzy_set_sugeno = {}
    fuzzy_set_yager = {}

    for key in fuzzy_set:
        fuzzy_set_standard[key] = 1.0 - fuzzy_set[key]
        fuzzy_set_sugeno[key] = (1.0 - fuzzy_set[key]) / (1.0 + (float(l) * fuzzy_set[key]))
        fuzzy_set_yager[key] = math.pow(1.0 - math.pow(fuzzy_set[key], float(w)), 1.0 / float(w))

        if fuzzy_set[key] < float(a):
            fuzzy_set_threshold[key] = 1.0
        else:
            fuzzy_set_threshold[key] = 0.0

    if msg:
        print 'Complemento de 1: ' + fuzzy_set_sort(fuzzy_set_standard)
        print 'Treshold: ' + fuzzy_set_sort(fuzzy_set_threshold)
        print 'Sugeno: ' + fuzzy_set_sort(fuzzy_set_sugeno)
        print 'Yager: ' + fuzzy_set_sort(fuzzy_set_yager)
    else:
        results = {}
        results['padrao'] = fuzzy_set_standard
        results['threshold'] = fuzzy_set_threshold
        results['sugeno'] = fuzzy_set_sugeno
        results['yager'] = fuzzy_set_yager
        return results

def create_discourse_universe(): # Cria o universo de discurso
    global min_u, max_u
    fuzzy_set = raw_input('Informe o primeiro e o ultimo valor do Universo de Discurso (Ex.: 0-4): ')
    fuzzy_set = fuzzy_set.split('-')
    min_u = int(fuzzy_set[0])
    max_u = int(fuzzy_set[1])

def read_fuzzy_set(): # Le os valores do conjunto fuzzy
    input_set = raw_input('Informe o conjunto fuzzy (Ex.: 0.2/2 + 0.5/5 + 1.0/6 + 0.1/7): ')
    input_set = input_set.split(' + ')
    fuzzy_set = {}
    for element in input_set:
        el = element.split('/')
        fuzzy_set[el[1]] = float(el[0])
    return fuzzy_set

def fill_set(fuzzy_set): # Retorna um conjunto fuzzy com todos os elementos presentes no universo de discurso
    global min_u, max_u
    for key in range(min_u, max_u+1):
        if not str(key) in fuzzy_set.keys():
            fuzzy_set[str(key)] = 0.0
    return fuzzy_set

def fuzzy_set_sort(set_fuzzy): # Retorna o conjunto fuzzy ordenado
    keys = set_fuzzy.keys()
    keys.sort()
    msg = ''
    for key in keys:
        msg += str(set_fuzzy[key]) + '/' + key
        if key != key[-1]:
            msg += ' + '
    return msg

#         if opcao == '6':
#
#             print '-- AGREGACAO --'
#             agregacao(conjunto_fuzzy_1, conjunto_fuzzy_2)
#             print '-- AGREGACAO --\n'
#             # ---------------------------- #
#         elif opcao == '7':
#             # Questao 7 ------------------ #
#             print '\n----: QUESTAO 7 :----'
#             min_U = 0
#             max_U = 10
#
#             # Letra a) ------------------- #
#             for pontos in [50.0, 500.0, 1000.0]:
#                 # Cria valor de incremento de acordo com o total de pontos da discretizacao
#                 discretizacao = (max_U - min_U) / pontos
#                 # Cria lista com 20 pontos de discretizacao no intervalo do universo de discurso
#                 universo_discurso = np.arange(min_U, max_U + discretizacao, discretizacao)
#
#                 f1 = funcao_triangular(universo_discurso, 1.0, 3.0, 5.0)
#                 f2 = funcao_triangular(universo_discurso, 1.0, 2.0, 4.0)
#                 f3 = funcao_triangular(universo_discurso, 1.0, 4.0, 6.0)
#                 f4 = funcao_trapezoidal(universo_discurso, 3.0, 4.0, 5.0, 7.0)
#                 f5 = funcao_gaussiana(universo_discurso, 1.0, 3.0)
#
#                 # PARA AS LETRAS b), c), d) E e) ----------------------------- #
#                 if pontos == 50.0:
#                     universo_discurso_letra_b = universo_discurso
#                     conjunto_fuzzy_letra_b = uniao(f1, f2, False)
#
#                     conjunto_fuzzy_letra_b['maximo'] = uniao(conjunto_fuzzy_letra_b['maximo'], f3, False)['maximo']
#                     conjunto_fuzzy_letra_b['soma_probabilistica'] = uniao(conjunto_fuzzy_letra_b['soma_probabilistica'], f3, False)['soma_probabilistica']
#                     conjunto_fuzzy_letra_b['lukasiewicz'] = uniao(conjunto_fuzzy_letra_b['lukasiewicz'], f3, False)['lukasiewicz']
#                     conjunto_fuzzy_letra_b['soma_drastica'] = uniao(conjunto_fuzzy_letra_b['soma_drastica'], f3, False)['soma_drastica']
#
#                     conjunto_fuzzy_letra_b['maximo'] = uniao(conjunto_fuzzy_letra_b['maximo'], f4, False)['maximo']
#                     conjunto_fuzzy_letra_b['soma_probabilistica'] = uniao(conjunto_fuzzy_letra_b['soma_probabilistica'], f4, False)['soma_probabilistica']
#                     conjunto_fuzzy_letra_b['lukasiewicz'] = uniao(conjunto_fuzzy_letra_b['lukasiewicz'], f4, False)['lukasiewicz']
#                     conjunto_fuzzy_letra_b['soma_drastica'] = uniao(conjunto_fuzzy_letra_b['soma_drastica'], f4, False)['soma_drastica']
#
#                     conjunto_fuzzy_letra_b['maximo'] = uniao(conjunto_fuzzy_letra_b['maximo'], f5, False)['maximo']
#                     conjunto_fuzzy_letra_b['soma_probabilistica'] = uniao(conjunto_fuzzy_letra_b['soma_probabilistica'], f5, False)['soma_probabilistica']
#                     conjunto_fuzzy_letra_b['lukasiewicz'] = uniao(conjunto_fuzzy_letra_b['lukasiewicz'], f5, False)['lukasiewicz']
#                     conjunto_fuzzy_letra_b['soma_drastica'] = uniao(conjunto_fuzzy_letra_b['soma_drastica'], f5, False)['soma_drastica']
#
#
#                     universo_discurso_letra_c = universo_discurso
#                     conjunto_fuzzy_letra_c = intersecao(f1, f2, False)
#
#                     conjunto_fuzzy_letra_c['minimo'] = intersecao(conjunto_fuzzy_letra_c['minimo'], f3, False)['minimo']
#                     conjunto_fuzzy_letra_c['produto'] = intersecao(conjunto_fuzzy_letra_c['produto'], f3, False)['produto']
#                     conjunto_fuzzy_letra_c['lukasiewicz'] = intersecao(conjunto_fuzzy_letra_c['lukasiewicz'], f3, False)['lukasiewicz']
#                     conjunto_fuzzy_letra_c['produto_drastico'] = intersecao(conjunto_fuzzy_letra_c['produto_drastico'], f3, False)['produto_drastico']
#
#                     conjunto_fuzzy_letra_c['minimo'] = intersecao(conjunto_fuzzy_letra_c['minimo'], f4, False)['minimo']
#                     conjunto_fuzzy_letra_c['produto'] = intersecao(conjunto_fuzzy_letra_c['produto'], f4, False)['produto']
#                     conjunto_fuzzy_letra_c['lukasiewicz'] = intersecao(conjunto_fuzzy_letra_c['lukasiewicz'], f4, False)['lukasiewicz']
#                     conjunto_fuzzy_letra_c['produto_drastico'] = intersecao(conjunto_fuzzy_letra_c['produto_drastico'], f4, False)['produto_drastico']
#
#                     conjunto_fuzzy_letra_c['minimo'] = intersecao(conjunto_fuzzy_letra_c['minimo'], f5, False)['minimo']
#                     conjunto_fuzzy_letra_c['produto'] = intersecao(conjunto_fuzzy_letra_c['produto'], f5, False)['produto']
#                     conjunto_fuzzy_letra_c['lukasiewicz'] = intersecao(conjunto_fuzzy_letra_c['lukasiewicz'], f5, False)['lukasiewicz']
#                     conjunto_fuzzy_letra_c['produto_drastico'] = intersecao(conjunto_fuzzy_letra_c['produto_drastico'], f5, False)['produto_drastico']
#
#
#                     universo_discurso_letra_d = universo_discurso
#                     conjunto_fuzzy_letra_d = {}
#
#                     conjunto_fuzzy_letra_d['f1'] = complemento(f1, 0.0, 0.0, 1.0, False)['padrao']
#                     conjunto_fuzzy_letra_d['f2'] = complemento(f2, 0.0, 0.0, 1.0, False)['padrao']
#                     conjunto_fuzzy_letra_d['f3'] = complemento(f3, 0.0, 0.0, 1.0, False)['padrao']
#                     conjunto_fuzzy_letra_d['f4'] = complemento(f4, 0.0, 0.0, 1.0, False)['padrao']
#                     conjunto_fuzzy_letra_d['f5'] = complemento(f5, 0.0, 0.0, 1.0, False)['padrao']
#
#
#                     universo_discurso_letra_e = universo_discurso
#                     conjunto_fuzzy_letra_e = agregacao(f1, f2, False)
#
#                     conjunto_fuzzy_letra_e['aritmetica'] = agregacao(conjunto_fuzzy_letra_e['aritmetica'], f3, False)['aritmetica']
#                     conjunto_fuzzy_letra_e['harmonica'] = agregacao(conjunto_fuzzy_letra_e['harmonica'], f3, False)['harmonica']
#                     conjunto_fuzzy_letra_e['geometrica'] = agregacao(conjunto_fuzzy_letra_e['geometrica'], f3, False)['geometrica']
#                     conjunto_fuzzy_letra_e['minimo'] = agregacao(conjunto_fuzzy_letra_e['minimo'], f3, False)['minimo']
#                     conjunto_fuzzy_letra_e['maximo'] = agregacao(conjunto_fuzzy_letra_e['maximo'], f3, False)['maximo']
#
#                     conjunto_fuzzy_letra_e['aritmetica'] = agregacao(conjunto_fuzzy_letra_e['aritmetica'], f4, False)['aritmetica']
#                     conjunto_fuzzy_letra_e['harmonica'] = agregacao(conjunto_fuzzy_letra_e['harmonica'], f4, False)['harmonica']
#                     conjunto_fuzzy_letra_e['geometrica'] = agregacao(conjunto_fuzzy_letra_e['geometrica'], f4, False)['geometrica']
#                     conjunto_fuzzy_letra_e['minimo'] = agregacao(conjunto_fuzzy_letra_e['minimo'], f4, False)['minimo']
#                     conjunto_fuzzy_letra_e['maximo'] = agregacao(conjunto_fuzzy_letra_e['maximo'], f4, False)['maximo']
#
#                     conjunto_fuzzy_letra_e['aritmetica'] = agregacao(conjunto_fuzzy_letra_e['aritmetica'], f5, False)['aritmetica']
#                     conjunto_fuzzy_letra_e['harmonica'] = agregacao(conjunto_fuzzy_letra_e['harmonica'], f5, False)['harmonica']
#                     conjunto_fuzzy_letra_e['geometrica'] = agregacao(conjunto_fuzzy_letra_e['geometrica'], f5, False)['geometrica']
#                     conjunto_fuzzy_letra_e['minimo'] = agregacao(conjunto_fuzzy_letra_e['minimo'], f5, False)['minimo']
#                     conjunto_fuzzy_letra_e['maximo'] = agregacao(conjunto_fuzzy_letra_e['maximo'], f5, False)['maximo']
#                 # PARA AS LETRAS b), c), d) E e) ----------------------------- #
#
#                 titulo = str(int(pontos)) + ' pontos de discretizacao'
#
#                 grau_pertinencia = [[], [], [], [], []]
#
#                 for c in universo_discurso:
#                     grau_pertinencia[0].append(f1[str(c)])
#                     grau_pertinencia[1].append(f2[str(c)])
#                     grau_pertinencia[2].append(f3[str(c)])
#                     grau_pertinencia[3].append(f4[str(c)])
#                     grau_pertinencia[4].append(f5[str(c)])
#
#                 desenha_grafico(grau_pertinencia)
#             # ---------------------------- #
#
#             # Letra b) ------------------- #
#             chaves = conjunto_fuzzy_letra_b.keys()
#
#             for c in chaves:
#                 titulo = 'S-norma ' + c
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso_letra_b:
#                     grau_pertinencia[0].append(conjunto_fuzzy_letra_b[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso_letra_b)
#             # ---------------------------- #
#
#             # Letra c) ------------------- #
#             chaves = conjunto_fuzzy_letra_c.keys()
#
#             for c in chaves:
#                 titulo = 'T-norma ' + c
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso_letra_c:
#                     grau_pertinencia[0].append(conjunto_fuzzy_letra_c[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso_letra_c)
#             # # ---------------------------- #
#
#             # Letra d) ------------------- #
#             chaves = conjunto_fuzzy_letra_d.keys()
#             chaves.sort()
#
#             for c in chaves:
#                 titulo = 'Complemento de um da funcao ' + c
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso_letra_d:
#                     grau_pertinencia[0].append(conjunto_fuzzy_letra_d[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso_letra_d)
#             # ---------------------------- #
#
#             # Letra e) ------------------- #
#             chaves = conjunto_fuzzy_letra_e.keys()
#             chaves.sort()
#
#             for c in chaves:
#                 titulo = 'Agregacao do tipo: ' + c
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso_letra_e:
#                     grau_pertinencia[0].append(conjunto_fuzzy_letra_e[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso_letra_e)
#             # ---------------------------- #
#         elif opcao == '8':
#             # Questao 8 ------------------ #
#             print '\n----: QUESTAO 8 :----'
#             min_U = 0
#             max_U = 10
#
#             # Cria valor de incremento de acordo com o total de pontos da discretizacao
#             pontos = 500.0
#             discretizacao = (max_U - min_U) / pontos
#             # Cria lista com 20 pontos de discretizacao no intervalo do universo de discurso
#             universo_discurso = np.arange(min_U, max_U + discretizacao, discretizacao)
#
#             f = funcao_triangular(universo_discurso, 4.0, 5.0, 6.0)
#             g = funcao_triangular(universo_discurso, 3.0, 5.0, 7.0)
#             h = funcao_trapezoidal(universo_discurso, 1.0, 3.0, 4.0, 6.0)
#
#             # Letra a) ------------------------------------------------------- #
#             titulo = str(int(pontos)) + ' pontos de discretizacao [Letra a)]'
#
#             grau_pertinencia = [[], [], [], [], []]
#
#             for c in universo_discurso:
#                 grau_pertinencia[0].append(f[str(c)])
#                 grau_pertinencia[1].append(g[str(c)])
#                 grau_pertinencia[2].append(h[str(c)])
#
#             desenha_grafico(grau_pertinencia)
#             # Letra a) ------------------------------------------------------- #
#
#             # Letra b) ------------------------------------------------------- #
#             if conjunto_eh_convexo(universo_discurso, f):
#                 print 'Conjunto F e convexo!'
#             else:
#                 print 'Conjunto F nao e convexo!'
#             if conjunto_eh_convexo(universo_discurso, g):
#                 print 'Conjunto G e convexo!'
#             else:
#                 print 'Conjunto G nao e convexo!'
#             if conjunto_eh_convexo(universo_discurso, h):
#                 print 'Conjunto H e convexo!'
#             else:
#                 print 'Conjunto H nao e convexo!'
#             # Letra b) ------------------------------------------------------- #
#
#             # Letra c) ------------------------------------------------------- #
#             conjunto_fuzzy = intersecao(f, g, False)
#
#             conjunto_fuzzy['minimo'] = intersecao(conjunto_fuzzy['minimo'], h, False)['minimo']
#             conjunto_fuzzy['produto'] = intersecao(conjunto_fuzzy['produto'], h, False)['produto']
#             conjunto_fuzzy['lukasiewicz'] = intersecao(conjunto_fuzzy['lukasiewicz'], h, False)['lukasiewicz']
#             conjunto_fuzzy['produto_drastico'] = intersecao(conjunto_fuzzy['produto_drastico'], h, False)['produto_drastico']
#
#             chaves = conjunto_fuzzy.keys()
#             chaves.sort()
#
#             for c in chaves:
#                 titulo = 'Agregacao do tipo: ' + c.upper() + ' [Letra c)]'
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso:
#                     grau_pertinencia[0].append(conjunto_fuzzy[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso)
#             # Letra c) ------------------------------------------------------- #
#
#             # Letra d) ------------------------------------------------------- #
#             conjunto_fuzzy = uniao(f, g, False)
#
#             conjunto_fuzzy['maximo'] = uniao(conjunto_fuzzy['maximo'], h, False)['maximo']
#             conjunto_fuzzy['soma_probabilistica'] = uniao(conjunto_fuzzy['soma_probabilistica'], h, False)['soma_probabilistica']
#             conjunto_fuzzy['lukasiewicz'] = uniao(conjunto_fuzzy['lukasiewicz'], h, False)['lukasiewicz']
#             conjunto_fuzzy['soma_drastica'] = uniao(conjunto_fuzzy['soma_drastica'], h, False)['soma_drastica']
#
#             chaves = conjunto_fuzzy.keys()
#             chaves.sort()
#
#             for c in chaves:
#                 titulo = 'Agregacao do tipo: ' + c.upper() + ' [Letra d)]'
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso:
#                     grau_pertinencia[0].append(conjunto_fuzzy[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso)
#             # Letra d) ------------------------------------------------------- #
#
#             # Letra e) ------------------------------------------------------- #
#             print 'Cardinalidade do conjunto F = ' + str( cardinalidade(f) )
#             print 'Cardinalidade do conjunto G = ' + str( cardinalidade(g) )
#             print 'Cardinalidade do conjunto H = ' + str( cardinalidade(h) )
#             # Letra e) ------------------------------------------------------- #
#
#             # Letra f) ------------------------------------------------------- #
#             print 'F contido em G? -> ' + inclusao(f,g)
#             print 'F contido em H? -> ' + inclusao(f,h)
#             print 'G contido em F? -> ' + inclusao(g,f)
#             print 'G contido em H? -> ' + inclusao(g,h)
#             print 'H contido em F? -> ' + inclusao(h,f)
#             print 'H contido em G? -> ' + inclusao(h,g)
#             # Letra f) ------------------------------------------------------- #
#
#             # Letra g) ------------------------------------------------------- #
#             print 'F contido em G? -> ' + igualdade(f,g)
#             print 'G contido em F? -> ' + igualdade(g,f)
#             print 'H contido em F? -> ' + igualdade(h,f)
#             print 'H contido em G? -> ' + igualdade(h,g)
#             # Letra g) ------------------------------------------------------- #
#
#             # Letra h) ------------------------------------------------------- #
#             # Resposta na letra g).
#             # Letra h) ------------------------------------------------------- #
#
#             # Letra i) ------------------------------------------------------- #
#             # Resposta na letra f).
#             # Letra i) ------------------------------------------------------- #
#
#             # Letra j) ------------------------------------------------------- #
#             conjunto_fuzzy = agregacao(f, g, False)
#
#             conjunto_fuzzy['aritmetica'] = agregacao(conjunto_fuzzy['aritmetica'], h, False)['aritmetica']
#             conjunto_fuzzy['harmonica'] = agregacao(conjunto_fuzzy['harmonica'], h, False)['harmonica']
#             conjunto_fuzzy['geometrica'] = agregacao(conjunto_fuzzy['geometrica'], h, False)['geometrica']
#             conjunto_fuzzy['minimo'] = agregacao(conjunto_fuzzy['minimo'], h, False)['minimo']
#             conjunto_fuzzy['maximo'] = agregacao(conjunto_fuzzy['maximo'], h, False)['maximo']
#
#             chaves = conjunto_fuzzy.keys()
#             chaves.sort()
#
#             for c in chaves:
#                 titulo = 'Agregacao do tipo: ' + c.upper() + ' [Letra j)]'
#                 grau_pertinencia = [[]]
#                 for u in universo_discurso:
#                     grau_pertinencia[0].append(conjunto_fuzzy[c][str(u)])
#
#                 desenha_grafico(grau_pertinencia, universo_discurso)
#             # Letra j) ------------------------------------------------------- #
#
#             # Letra k) ------------------------------------------------------- #
#             conjunto_fuzzy = {}
#
#             conjunto_fuzzy['f1'] = complemento(f, 0.3, -0.5, 2.0, False)
#             conjunto_fuzzy['f2'] = complemento(f, 0.75, 1.0, 1.0, False)
#             del conjunto_fuzzy['f2']['padrao']
#             del conjunto_fuzzy['f2']['yager']
#
#             conjunto_fuzzy['g1'] = complemento(g, 0.3, -0.5, 2.0, False)
#             conjunto_fuzzy['g2'] = complemento(g, 0.75, 1.0, 1.0, False)
#             del conjunto_fuzzy['g2']['padrao']
#             del conjunto_fuzzy['g2']['yager']
#
#             conjunto_fuzzy['h1'] = complemento(h, 0.3, -0.5, 2.0, False)
#             conjunto_fuzzy['h2'] = complemento(h, 0.75, 1.0, 1.0, False)
#             del conjunto_fuzzy['h2']['padrao']
#             del conjunto_fuzzy['h2']['yager']
#
#
#             for chave in conjunto_fuzzy:
#                 chaves = conjunto_fuzzy[chave].keys()
#                 chaves.sort()
#
#                 for c in chaves:
#                     titulo = 'Complemento ' + c.upper() + ' da funcao ' + chave[0].upper() + ' [Letra k)]'
#                     grau_pertinencia = [[]]
#                     for u in universo_discurso:
#                         grau_pertinencia[0].append(conjunto_fuzzy[chave][c][str(u)])
#
#                     desenha_grafico(grau_pertinencia, universo_discurso)
#             # Letra k) ------------------------------------------------------- #
#
#             # ---------------------------- #
#         else:
#         	print 'Finalizando execucao...'
#         	break
#
#
#
#
# def agregacao(conjunto_fuzzy_1, conjunto_fuzzy_2, return_msg=True):
#     conjunto_fuzzy_1 = preenche_conjunto(conjunto_fuzzy_1)
#     conjunto_fuzzy_2 = preenche_conjunto(conjunto_fuzzy_2)
#     conjunto_fuzzy_aritmetica = {}
#     conjunto_fuzzy_harmonica = {}
#     conjunto_fuzzy_geometrica = {}
#     conjunto_fuzzy_minimo = {}
#     conjunto_fuzzy_maximo = {}
#
#     for chave in conjunto_fuzzy_1:
#         conjunto_fuzzy_aritmetica[chave] = (conjunto_fuzzy_1[chave] + conjunto_fuzzy_2[chave]) / 2.0
#         conjunto_fuzzy_geometrica[chave] = math.pow(conjunto_fuzzy_1[chave] * conjunto_fuzzy_2[chave], 1.0/2.0)
#         conjunto_fuzzy_minimo[chave] = min(conjunto_fuzzy_1[chave], conjunto_fuzzy_2[chave])
#         conjunto_fuzzy_maximo[chave] = max(conjunto_fuzzy_1[chave], conjunto_fuzzy_2[chave])
#
#         if conjunto_fuzzy_1[chave] == 0.0 and conjunto_fuzzy_2[chave] != 0.0:
#             conjunto_fuzzy_harmonica[chave] = 2.0 / ((1.0/conjunto_fuzzy_2[chave]) + 1.0)
#         elif conjunto_fuzzy_1[chave] != 0.0 and conjunto_fuzzy_2[chave] == 0.0:
#             conjunto_fuzzy_harmonica[chave] = 2.0 / ((1.0/conjunto_fuzzy_1[chave]) + 1.0)
#         elif conjunto_fuzzy_1[chave] == 0.0 and conjunto_fuzzy_2[chave] == 0.0:
#             conjunto_fuzzy_harmonica[chave] = 0.0
#         else:
#             conjunto_fuzzy_harmonica[chave] = 2.0 / ((1.0/conjunto_fuzzy_1[chave]) + (1.0/conjunto_fuzzy_2[chave]))
#
#     if return_msg:
#         print 'Aritmetica: ' + imprime_conjunto_fuzzy( conjunto_fuzzy_aritmetica )
#         print 'Harmonica: ' + imprime_conjunto_fuzzy( conjunto_fuzzy_harmonica )
#         print 'Geometrica: ' + imprime_conjunto_fuzzy( conjunto_fuzzy_geometrica )
#         print 'Minimo: ' + imprime_conjunto_fuzzy( conjunto_fuzzy_minimo )
#         print 'Maximo: ' + imprime_conjunto_fuzzy( conjunto_fuzzy_maximo )
#     else:
#         resultado = {}
#         resultado['aritmetica'] = conjunto_fuzzy_aritmetica
#         resultado['harmonica'] = conjunto_fuzzy_harmonica
#         resultado['geometrica'] = conjunto_fuzzy_geometrica
#         resultado['minimo'] = conjunto_fuzzy_minimo
#         resultado['maximo'] = conjunto_fuzzy_maximo
#         return resultado
#
#
# def funcao_triangular(universo_discurso, a, m, b):
#     conjunto_fuzzy = {}
#     for x in universo_discurso:
#         if x >= a and x < m:
#             conjunto_fuzzy[str(x)] = ((x-a)/(m-a))
#         elif x >= m and x <= b:
#             conjunto_fuzzy[str(x)] = ((b-x)/(b-m))
#         else:
#             conjunto_fuzzy[str(x)] = 0.0
#
#     return conjunto_fuzzy
#
#
# def funcao_trapezoidal(universo_discurso, a, m, n, b):
#     conjunto_fuzzy = {}
#     for x in universo_discurso:
#         if x >= a and x < m:
#             conjunto_fuzzy[str(x)] = ((x-a)/(m-a))
#         elif x >= m and x < n:
#             conjunto_fuzzy[str(x)] = 1.0
#         elif x >= n and x <= b:
#             conjunto_fuzzy[str(x)] = ((b-x)/(b-n))
#         else:
#             conjunto_fuzzy[str(x)] = 0.0
#
#     return conjunto_fuzzy
#
#
# def funcao_gaussiana(universo_discurso, m, gama):
#     conjunto_fuzzy = {}
#     for x in universo_discurso:
#         potencial = math.pow(x - m, 2)
#         potencial = potencial / math.pow(gama, 2)
#         conjunto_fuzzy[str(x)] = math.exp(-1 * potencial)
#
#     return conjunto_fuzzy
#
#
# def conjunto_eh_convexo(universo_discurso, conjunto_fuzzy):
#     for x1 in universo_discurso:
#         for x2 in universo_discurso:
#             # Cria valor de incremento de acordo com o total de pontos da discretizacao
#             discretizacao = 1.0 / 20.0
#             # Cria lista com 20 pontos de discretizacao no intervalo do universo de discurso
#             lambda_ = np.arange(0.0, 1.0 + discretizacao, discretizacao)
#             for l in lambda_:
#                 chave = str( (l*x1) + ((1-l)*x2) )
#                 if chave in conjunto_fuzzy.keys():
#                     if conjunto_fuzzy[chave] < min(conjunto_fuzzy[str(x1)], conjunto_fuzzy[str(x2)]):
#                         return False
#
#     return True
#
#
# def cardinalidade(conjunto_fuzzy):
#     cardinalidade = 0.0
#     for chave in conjunto_fuzzy.keys():
#         cardinalidade += conjunto_fuzzy[chave]
#
#     return cardinalidade
#
#
# def igualdade(conjunto_fuzzy_1, conjunto_fuzzy_2):
#     msg = ''
#     grau_de_igualdade = 0.0
#
#     for chave in conjunto_fuzzy_1:
#         if conjunto_fuzzy_1[chave] != conjunto_fuzzy_2[chave]:
#             if abs(conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave]) > grau_de_igualdade:
#                 grau_de_igualdade = abs(conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave])
#
#     if grau_de_igualdade == 0.0:
#         msg += 'Os conjuntos sao iguais. '
#     else:
#         msg += 'Os conjuntos nao sao iguais. '
#
#     msg += 'Grau de igualdade = ' + str(1 - grau_de_igualdade)
#
#     return msg
#
#
# def inclusao(conjunto_fuzzy_1, conjunto_fuzzy_2):
#     msg = ''
#     grau_de_inclusao = 0.0
#
#     for chave in conjunto_fuzzy_1:
#         if conjunto_fuzzy_1[chave] <= conjunto_fuzzy_2[chave]:
#             grau_de_inclusao += 1.0
#         else:
#             grau_de_inclusao += 1.0 - ( conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave] )
#
#     print grau_de_inclusao
#     print len(universo_discurso)
#     grau_de_inclusao = grau_de_inclusao / len(conjunto_fuzzy_1.keys())
#
#     if grau_de_inclusao == 1.0:
#         msg += 'O conjunto 1 esta incluido no conjunto 2. '
#     else:
#         msg += 'O conjunto 1 nao esta incluido no conjunto 2. '
#
#     msg += 'Grau de inclusao = ' + str(grau_de_inclusao)
#
#     return msg
#
#
# def desenha_grafico(grau_pertinencia, universo_discurso_diferente=False):
#     if grau_pertinencia is None:
#         print 'Conjunto(s) vazio(s)!!'
#         return
#
#     legenda = []
#     for i,funcao in enumerate(grau_pertinencia):
#         if not funcao:
#             continue
#         elif i == 0:
#             cor = 'red'
#             label = 'F_1'
#         elif i == 1:
#             cor = 'green'
#             label = 'F_2'
#         elif i == 2:
#             cor = 'blue'
#             label = 'F_3'
#         elif i == 3:
#             cor = 'orange'
#             label = 'F_4'
#         elif i == 4:
#             cor = 'black'
#             label = 'F_5'
#
#         if universo_discurso_diferente is False:
#             plt.plot(universo_discurso, funcao, 'ro', color=cor)
#         else:
#             plt.plot(universo_discurso_diferente, funcao, 'ro', color=cor)
#         legenda.append(mpatches.Patch(color=cor, label=label))
#
#     plt.legend(handles=legenda)
#
#     plt.xticks(np.arange(min_U, max_U+2, 1.0))
#     plt.yticks(np.arange(0, 2.5, 1))
#
#     axes = plt.gca()
#     axes.set_title(titulo)
#     axes.set_xlabel('')
#     axes.set_ylabel('Grau de pertinencia')
#
#     plt.show()


if __name__ == '__main__':
    main()
