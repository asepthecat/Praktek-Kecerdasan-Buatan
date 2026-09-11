import heapq
from collections import deque

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
# MENGHITUNG TOTAL BIAYA LINTASAN
# ==========================================================

def hitung_biaya(graph, path):
    total = 0

    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]

    return total


# ==========================================================
# 1. BREADTH-FIRST SEARCH (BFS)
# ==========================================================

def bfs(graph, start, goal):
    frontier = deque([start])
    parent = {}
    reached = {start}
    expanded = 0

    while frontier:
        node = frontier.popleft()
        expanded += 1

        if node == goal:
            return reconstruct(parent, goal), expanded

        for neighbor in graph.get(node, {}):
            if neighbor not in reached:
                reached.add(neighbor)
                parent[neighbor] = node
                frontier.append(neighbor)

    return None, expanded


# ==========================================================
# 2. DEPTH-FIRST SEARCH (DFS)
# ==========================================================

def dfs(graph, start, goal):
    frontier = [start]
    parent = {}
    reached = {start}
    expanded = 0

    while frontier:
        node = frontier.pop()
        expanded += 1

        if node == goal:
            return reconstruct(parent, goal), expanded

        for neighbor in graph.get(node, {}):
            if neighbor not in reached:
                reached.add(neighbor)
                parent[neighbor] = node
                frontier.append(neighbor)

    return None, expanded


# ==========================================================
# 3. UNIFORM-COST SEARCH (UCS)
# ==========================================================

def ucs(graph, start, goal):
    frontier = [(0, start)]
    parent = {}
    best_cost = {start: 0}
    expanded = 0

    while frontier:
        cost, node = heapq.heappop(frontier)

        if cost > best_cost.get(node, float('inf')):
            continue

        expanded += 1

        if node == goal:
            return reconstruct(parent, goal), cost, expanded

        for neighbor, step_cost in graph.get(node, {}).items():
            new_cost = cost + step_cost

            if new_cost < best_cost.get(
                neighbor,
                float('inf')
            ):
                best_cost[neighbor] = new_cost
                parent[neighbor] = node

                heapq.heappush(
                    frontier,
                    (new_cost, neighbor)
                )

    return None, None, expanded


# ==========================================================
# 4. FUNGSI HEURISTIK SLD
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
# 5. GREEDY BEST-FIRST SEARCH
# ==========================================================

def greedy_best_first(graph, start, goal, h):
    frontier = [(h[start], start)]
    parent = {}
    reached = {start}
    expanded = 0

    while frontier:
        _, node = heapq.heappop(frontier)
        expanded += 1

        if node == goal:
            return reconstruct(parent, goal), expanded

        for neighbor in graph.get(node, {}):
            if neighbor not in reached:
                reached.add(neighbor)
                parent[neighbor] = node

                heapq.heappush(
                    frontier,
                    (h[neighbor], neighbor)
                )

    return None, expanded


# ==========================================================
# 6. A* SEARCH
# ==========================================================

def a_star(graph, start, goal, h):
    frontier = [(h[start], 0, start)]
    parent = {}
    best_cost = {start: 0}
    expanded = 0

    while frontier:
        f, g, node = heapq.heappop(frontier)

        if g > best_cost.get(node, float('inf')):
            continue

        expanded += 1

        if node == goal:
            return reconstruct(parent, goal), g, expanded

        for neighbor, step_cost in graph.get(node, {}).items():
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
# MENJALANKAN SEMUA ALGORITMA
# ==========================================================

start = 'Neamt'
goal = 'Pitesti'


# BFS
bfs_path, bfs_expanded = bfs(graph, start, goal)
bfs_cost = hitung_biaya(graph, bfs_path)


# DFS
dfs_path, dfs_expanded = dfs(graph, start, goal)
dfs_cost = hitung_biaya(graph, dfs_path)


# UCS
ucs_path, ucs_cost, ucs_expanded = ucs(
    graph, start, goal
)


# Greedy
greedy_path, greedy_expanded = greedy_best_first(
    graph, start, goal, h_sld
)
greedy_cost = hitung_biaya(graph, greedy_path)


# A*
astar_path, astar_cost, astar_expanded = a_star(
    graph, start, goal, h_sld
)


# ==========================================================
# MENENTUKAN OPTIMAL
# ==========================================================

optimal_cost = ucs_cost


def status_optimal(cost):
    if cost == optimal_cost:
        return "Ya"
    else:
        return "Tidak"


# ==========================================================
# HASIL
# ==========================================================

print()
print("=" * 75)
print("PERBANDINGAN LIMA ALGORITMA SEARCH")
print("Kasus:", start, "->", goal)
print("=" * 75)

print()

print("1. BFS")
print("   Lintasan           :", " -> ".join(bfs_path))
print("   Total biaya        :", bfs_cost)
print("   Node dieksplorasi  :", bfs_expanded)
print("   Optimal?           :", status_optimal(bfs_cost))

print()

print("2. DFS")
print("   Lintasan           :", " -> ".join(dfs_path))
print("   Total biaya        :", dfs_cost)
print("   Node dieksplorasi  :", dfs_expanded)
print("   Optimal?           :", status_optimal(dfs_cost))

print()

print("3. UCS")
print("   Lintasan           :", " -> ".join(ucs_path))
print("   Total biaya        :", ucs_cost)
print("   Node dieksplorasi  :", ucs_expanded)
print("   Optimal?           :", status_optimal(ucs_cost))

print()

print("4. Greedy Best-First")
print("   Lintasan           :", " -> ".join(greedy_path))
print("   Total biaya        :", greedy_cost)
print("   Node dieksplorasi  :", greedy_expanded)
print("   Optimal?           :", status_optimal(greedy_cost))

print()

print("5. A*")
print("   Lintasan           :", " -> ".join(astar_path))
print("   Total biaya        :", astar_cost)
print("   Node dieksplorasi  :", astar_expanded)
print("   Optimal?           :", status_optimal(astar_cost))

print()
print("=" * 75)
print("BIAYA OPTIMAL =", optimal_cost)
print("=" * 75)