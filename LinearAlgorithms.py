import networkx as nx
import matplotlib.pyplot as plt

def Linear_Tree_to_Prufer(tree: nx.Graph):
    n = tree.number_of_nodes()
    prufer = [None] * (n-2)

    degree_sequence = list(tree.degree)  #Secuencia de Grados no Ordenada
    leaves = []
    for d in range(n):
        if degree_sequence[d][1] == 1:
            leaves.append(degree_sequence[d][0])
    # print(degree_sequence)

    degrees = [None] * n
    for element in degree_sequence:
        degrees[element[0]] = element[1]


    # Construcción de la lista f tal que f[v] es el vértice padre del nodo v
    f = [-2] * n
    f[n-1] = -1    # Root
    level_nodes = [n-1]
    while len(level_nodes) != 0:
        list_aux = level_nodes.copy()
        level_nodes = list()
        for i in list_aux:
            for j in tree.neighbors(i):
                if f[j] == -2:
                    f[j] = i
                    level_nodes.append(j)


    x = min(leaves)
    index = x

    for i in range(0, n-2):
        y = f[x]
        prufer[i] = y
        degrees[y] = degrees[y] - 1
        if y < index and degrees[y] == 1:
            x = y
        else:
            j = index + 1
            while degrees[j] != 1:
                j = j + 1
            x = j
            index = x


    return prufer


def Linear_Prufer_to_Tree(prufer_sequence: list[int]):

    n = len(prufer_sequence) + 2     # tree_nodes_len
    output_tree = nx.Graph()
    output_tree.add_nodes_from([number for number in range(0, n)])
    degree_sequence = [1] * n
    for element in prufer_sequence:   # O(n-2) = O(n)
        degree_sequence[element] = degree_sequence[element] + 1


    x = degree_sequence.index(1)
    index = x
    for i in range(0, n-2):
        y = prufer_sequence[i]
        output_tree.add_edge(x, y)
        degree_sequence[y] = degree_sequence[y] - 1
        if y < index and degree_sequence[y] == 1:
            x = y
        else:
            j = index + 1
            while degree_sequence[j] != 1:
                j = j + 1
            x = j
            index = x

    index = index + 1
    output_tree.add_edge(index, x)


    nx.draw(output_tree, with_labels=True)
    plt.axis("equal")
    plt.show()

    return output_tree

# Prufer to Tree

# prufer = [0, 2, 2, 1]
# tree = (Linear_Prufer_to_Tree(prufer))

# Tree to Prufer
tree = nx.Graph()
tree.add_edges_from([(0, 2), (0, 3), (1, 2), (1, 5), (2, 4)])
print(Linear_Tree_to_Prufer(tree))