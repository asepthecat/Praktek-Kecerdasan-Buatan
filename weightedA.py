import heapq

# ==========================================================
# GRAPH PETA RUMANIA
# ==========================================================

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {
        'Arad': 140,
        'Oradea': 151,
        'Fagaras': 99,
        'RimnicuVilcea': 80
    },
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {
        'Drobeta': 120,
        'RimnicuVilcea': 146,
        'Pitesti': 138
    },
    'RimnicuVilcea': {
        'Sibiu': 80,
        'Craiova': 146,
        'Pitesti': 97
    },
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {
        'RimnicuVilcea': 97,
        'Craiova': 138,
        'Bucharest': 101
    },
    'Bucharest': {
        'Fagaras': 211,
        'Pitesti': 101,
        'Giurgiu': 90,
        'Urziceni': 85
    },
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {
        'Bucharest': 85,
        'Hirsova': 98,
        'Vaslui': 142
    },
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


# ==========================================================
# RECONSTRUCT PATH
# ==========================================================

def reconstruct(parent, goal):
    path = [goal]

    while path[-1] in parent:
        path.append(parent[path[-1]])

    path.reverse()
    return path


# ==========================================================
# HEURISTIK SLD MENUJU BUCHAREST
# ==========================================================

h_sld = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'RimnicuVilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


# ==========================================================
# WEIGHTED A*
# f(n) = g(n) + W * h(n)
# ==========================================================

def weighted_a_star(graph, start, goal, h, W):

    frontier = [(h[start] * W, 0, start)]

    parent = {}

    best_cost = {
        start: 0
    }

    expanded = 0

    while frontier:

        f, g, node = heapq.heappop(frontier)

        if g > best_cost.get(
            node,
            float('inf')
        ):
            continue

        expanded += 1

        if node == goal:
            return (
                reconstruct(parent, goal),
                g,
                expanded
            )

        for neighbor, step_cost in graph.get(
            node,
            {}
        ).items():

            new_g = g + step_cost

            if new_g < best_cost.get(
                neighbor,
                float('inf')
            ):

                best_cost[neighbor] = new_g

                parent[neighbor] = node

                new_f = new_g + W * h[neighbor]

                heapq.heappush(
                    frontier,
                    (
                        new_f,
                        new_g,
                        neighbor
                    )
                )

    return None, None, expanded


# ==========================================================
# KASUS
# ==========================================================

start = 'Arad'
goal = 'Bucharest'


# ==========================================================
# A* BIASA (W = 1)
# ==========================================================

path_1, cost_1, expanded_1 = weighted_a_star(
    graph,
    start,
    goal,
    h_sld,
    1
)


# ==========================================================
# WEIGHTED A* (W = 1.5)
# ==========================================================

path_15, cost_15, expanded_15 = weighted_a_star(
    graph,
    start,
    goal,
    h_sld,
    1.5
)


# ==========================================================
# WEIGHTED A* (W = 2)
# ==========================================================

path_2, cost_2, expanded_2 = weighted_a_star(
    graph,
    start,
    goal,
    h_sld,
    2
)


# ==========================================================
# HASIL
# ==========================================================

print()
print("=" * 80)
print("PERBANDINGAN A* DAN WEIGHTED A*")
print("=" * 80)

print("Kasus:", start, "->", goal)

print()

print("A* (W = 1)")
print("Lintasan          :", " -> ".join(path_1))
print("Total biaya       :", cost_1)
print("Node dieksplorasi :", expanded_1)

print()

print("Weighted A* (W = 1.5)")
print("Lintasan          :", " -> ".join(path_15))
print("Total biaya       :", cost_15)
print("Node dieksplorasi :", expanded_15)

print()

print("Weighted A* (W = 2)")
print("Lintasan          :", " -> ".join(path_2))
print("Total biaya       :", cost_2)
print("Node dieksplorasi :", expanded_2)

print()
print("=" * 80)