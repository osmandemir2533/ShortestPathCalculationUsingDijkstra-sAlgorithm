import networkx as nx
import matplotlib.pyplot as plt


def read_graph(filename):
    G = nx.Graph()
    with open(filename, 'r') as f:
        for line in f:
            node1, node2, weight = line.split()
            G.add_edge(node1, node2, weight=int(weight))
    return G


def dijkstra_all_shortest_paths(G, source):
    lengths, paths = nx.single_source_dijkstra(G, source)
    return lengths, paths


def dijkstra_shortest_path(G, source, target):
    return nx.dijkstra_path(G, source, target), nx.dijkstra_path_length(G, source, target)


def visualize_graph(G, source, paths, target_path):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Çizilecek tüm yolları belirle
    for target, path in paths.items():
        if target != source:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='gray', width=1)

    # Kaynak ve hedef arasındaki en kısa yolu kırmızı ile çiz
    path_edges = list(zip(target_path, target_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.show()


def main():
    filename = 'graph.txt'
    source = input("Kaynak düğümü girin (örn. A): ")
    target = input("Hedef düğümü girin (örn. F): ")

    G = read_graph(filename)
    lengths, paths = dijkstra_all_shortest_paths(G, source)
    target_path, target_length = dijkstra_shortest_path(G, source, target)

    print(f"{source} düğümünden diğer düğümlere olan en kısa mesafeler:")
    for target_node in lengths:
        print(f"{source} -> {target_node} : {lengths[target_node]}")

    print(f"\n{source} ile {target} arasındaki en kısa yol: {target_path} ve uzunluğu: {target_length}")

    visualize_graph(G, source, paths, target_path)


if __name__ == "__main__":
    main()
