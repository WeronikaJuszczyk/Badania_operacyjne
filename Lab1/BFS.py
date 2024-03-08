from typing import Dict, List


def BFS(G: Dict[int, List[str]], s: int):
    No = []               # zmienna przechowującej wartości ponumerowanych wierzchołków w liście
    queue = []            # kolejka (FIFO)
    cycle_exists = False  # zmienna opisująca istnienie cykli
    is_consistent = True  # zmienna opisująca spójność grafu
    queue.append(s)       # dodanie do kolejki początkowy wierzchołek

    while queue:                     # dopóki kolejka nie jest pusta
        v = queue.pop(0)             # pobranie z kolejki pierwszy wierzchołek

        if v not in No:              # jeśli wierzchołek nie został ponumerowany:
            No.append(v)             # dodaj wierzchołek do listy:
            neighbour_visited = 0    # liczba sąsiadów 'v', którzy są ponumerowani

        for neighbour in G[v]:       # umieszczanie w kolejce sąsiadów v
            if neighbour in No:
                neighbour_visited += 1      # zwiększanie o 1 liczbę sąsiadów odwiedzonych
                if neighbour_visited > 1:
                    cycle_exists = True     # wtedy graf jest cykliczny
            else:
                queue.append(neighbour)  # dodanie nieponumerowanych sąsiadów v do kolejki

    # czy graf spójny
    if len(No) < len(G.keys()):   # gdy liczba wierzchołków ponumerowynych jest mniejsza od liczby kluczy w słowniku to
        is_consistent = False     # graf nie spójny

    return No, cycle_exists, is_consistent


graph = {
    '1': ['2','3','7'],
    '2': ['1', '3','6'],
    '3': ['6','7'],
    '4': ['1','5'],
    '5': ['4'],
    '6': ['2','3','4'],
    '7': ['1','3'],
    '8': ['9','10'],
    '9': ['8','10'],
    '10': ['8','9']
}

No = BFS(graph,'1')[0]
print("Lista kolejnych wierzchołków: ",No)

cycle_exist = BFS(graph,'1')[1]
print("Istnienie cyklu: ", cycle_exist)

is_consistent = BFS(graph,'1')[2]
print("Spójność cyklu: ", is_consistent)


