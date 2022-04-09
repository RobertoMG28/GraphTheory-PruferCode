
import networkx as nx
import matplotlib.pyplot as plt


def tree_to_prufer(tree: nx.Graph) -> list[int]:
    n = tree.number_of_nodes()       # Número de vértices
    assert n >= 2                    # Nos aseguramos de que el árbol posee más de dos vértices
    prufer = [None] * (n-2)          # Se inicializa el Código de Prüfer Asociado

    positions = nx.spring_layout(tree)             # Graficar el resultado inicial
    print("Inicialización:", "prufer: ", prufer)
    nx.draw(tree, with_labels=True, pos = positions)
    plt.axis("equal")
    plt.show()


    for i in range(n-2):
        degrees = list(tree.degree)  # Secuencia de Grados No ordenada

        leaves = []   # Lista de Hojas
        j = 0
        current_number_nodes = tree.number_of_nodes()  # O(n)

        # PEOR CASO: (n) + (n-1) + (n-2) + ... + (4) + (3)      con n-2 términos (Suma típica; O(n^2))
        while current_number_nodes > j:             # O(n)
            if degrees[j][1] == 1:
                leaves.append(degrees[j][0])       # O(1) el append
            j = j + 1

        v = min(leaves)    # O(n)
        list_neighbours = list(tree.adj[v].keys())     # O(1) Acceso a Dict, .keys O(1), list() O(n)
        u = list_neighbours[0]           # O(n)
        prufer[i] = u

        tree.remove_node(v)                         # O(n)

        print("Final de Iteración", i + 1, "prufer: ", prufer) # Graficar el resultado i-ésimo
        nx.draw(tree, with_labels=True, pos = positions)
        plt.axis("equal")
        plt.show()

    return prufer


def prufer_to_tree(prufer: list[int]) -> nx.Graph:
    n = len(prufer) + 2  # O(n-2) = O(n)
    tree = nx.Graph()
    nodes = [number for number in range(n)]  # O(n)
    tree.add_nodes_from(nodes)

    positions = nx.spring_layout(tree)
    print("Inicialización:", "prufer: ", prufer, "nodes: ", nodes)
    nx.draw(tree, with_labels=True, pos = positions)
    plt.axis("equal")
    plt.show()

    for i in range(0, n-2):
        j = prufer[0]  # O(n)

        set_nodes = set(nodes)  # O(n)
        set_prufer = set(prufer)  # O(n)

        set_difference = (set_nodes - set_prufer)  # O(n)
        k = min(set_difference)  # O(n)

        tree.add_edge(j, k)  # O(1)

        nodes.remove(k)  # O(n)
        prufer.pop(0)  # O(n)

        print("Final de Iteración", i + 1, "prufer: ", prufer, "nodes: ", nodes)
        nx.draw(tree, with_labels=True, pos = positions)
        plt.axis("equal")
        plt.show()

    # O(n)+O(n)+...+O(n) = O(n) Parte interior del bucle
    # (n-2) * O(n) = O(n^2)

    tree.add_edge(nodes[0], nodes[1]) # O(1)

    nx.draw(tree, with_labels=True, pos = positions)
    plt.axis("equal")
    plt.show()

    return tree




# Prufer to Tree

#prufer = [0, 2, 2, 1]
#tree = (prufer_to_tree(prufer))

# Tree to Prufer
tree = nx.Graph()
tree.add_edges_from([(0, 2), (0, 3), (1, 2), (1, 5), (2, 4)])
print(tree_to_prufer(tree))










