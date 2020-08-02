# LETRA A
# dado u.adjacentes = linked list
# dado v.adjacentes = linked list
def existe_deleta_aresta_estrutura(u, v): # O(2n) - # O(n)
  exists = False
  for adjacente in u.adjacentes:
    if adjacente == v:
      exists = True
      aponta_ponteiro_para_proximo_adjacente(adjacente) # apontar ponteiro apontado para si(v na lista encadeada) para o filho de v em questão
  if exists:
    for adjacente v.adjacentes:
      if adjacente == u:
        aponta_ponteiro_para_proximo_adjacente(adjacente) # apontar ponteiro apontado para si(u na lista encadeada) para o filho de u em questão
    return 'Nós eram adjacentes. Aresta deletada.'
  else:
    return 'Nós não são adjacentes.'

def existe_deleta_aresta_matriz(u, v, matriz_adjacencias): # O(1)
  if matriz_adjacencias[u][v] >= 1:
    matriz_adjacencias[u][v] = 0
    matriz_adjacencias[v][u] = 0

# LETRA B
# Sendo um vetor, a parte de achar a aresta poderia ser feita via busca binaria, ja que estaria ordenado, sendo mais otimizado, ja que eh O(logn).
# Logo, a busca da adjacencia seria mais eficiente.
# Já na destruição da aresta, fica pior. Porque deletando um, todos os itens do vetor terao que ser realocados na memória para manter a contiguidade.
