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
# HEURISTIK STRAIGHT-LINE DISTANCE
# Menuju Bucharest
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
# HEURISTIK TIDAK ADMISSIBLE
# Nilai heuristik dikali 2
# ==========================================================

h_tidak_admissible = {
    kota: nilai * 2
    for kota, nilai in h_sld.items()
}


# ==========================================================
# A* SEARCH
# ==========================================================

def a_star(graph, start, goal, h):

    frontier = [(h[start], 0, start)]

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

                heapq.heappush(
                    frontier,
                    (
                        new_g + h[neighbor],
                        new_g,
                        neighbor
                    )
                )

    return None, None, expanded


# ==========================================================
# MENJALANKAN A* DENGAN HEURISTIK TIDAK ADMISSIBLE
# ==========================================================

start = 'Arad'
goal = 'Bucharest'

path, cost, expanded = a_star(
    graph,
    start,
    goal,
    h_tidak_admissible
)


# ==========================================================
# HASIL
# ==========================================================

print()
print("=" * 75)
print("A* DENGAN HEURISTIK TIDAK ADMISSIBLE")
print("=" * 75)

print("Kasus               :", start, "->", goal)
print("Lintasan             :", " -> ".join(path))
print("Total biaya          :", cost)
print("Node dieksplorasi    :", expanded)

if cost == 418:
    print("Optimal?             : Ya")
else:
    print("Optimal?             : Tidak")

print("Biaya optimal UCS    : 418")

print("=" * 75)