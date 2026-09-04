import heapq
from collections import deque

# ==========================================
# GRAPH PETA RUMANIA (AIMA Fig. 3.1)
# ==========================================

graph = {
    'Arad': {
        'Zerind': 75,
        'Sibiu': 140,
        'Timisoara': 118
    },

    'Zerind': {
        'Arad': 75,
        'Oradea': 71
    },

    'Oradea': {
        'Zerind': 71,
        'Sibiu': 151
    },

    'Sibiu': {
        'Arad': 140,
        'Oradea': 151,
        'Fagaras': 99,
        'RimnicuVilcea': 80
    },

    'Timisoara': {
        'Arad': 118,
        'Lugoj': 111
    },

    'Lugoj': {
        'Timisoara': 111,
        'Mehadia': 70
    },

    'Mehadia': {
        'Lugoj': 70,
        'Drobeta': 75
    },

    'Drobeta': {
        'Mehadia': 75,
        'Craiova': 120
    },

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

    'Fagaras': {
        'Sibiu': 99,
        'Bucharest': 211
    },

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

    'Giurgiu': {
        'Bucharest': 90
    },

    'Urziceni': {
        'Bucharest': 85,
        'Hirsova': 98,
        'Vaslui': 142
    },

    'Hirsova': {
        'Urziceni': 98,
        'Eforie': 86
    },

    'Eforie': {
        'Hirsova': 86
    },

    'Vaslui': {
        'Urziceni': 142,
        'Iasi': 92
    },

    'Iasi': {
        'Vaslui': 92,
        'Neamt': 87
    },

    'Neamt': {
        'Iasi': 87
    }
}

# ==========================================
# UNIFORM-COST SEARCH (UCS)
# ==========================================

def ucs(graph, start, goal):
    """
    Mencari lintasan dengan biaya total paling rendah
    menggunakan algoritma Uniform-Cost Search.
    """

    # Priority Queue
    # Format: (path_cost, node)
    frontier = [(0, start)]

    # Menyimpan parent setiap node
    parent = {}

    # Menyimpan biaya terbaik yang ditemukan
    best_cost = {
        start: 0
    }

    # Menghitung jumlah node yang dieksplorasi
    expanded = 0

    while frontier:

        # Mengambil node dengan biaya terkecil
        cost, node = heapq.heappop(frontier)

        # Lewati entry lama jika sudah ada
        # jalur yang lebih murah
        if cost > best_cost.get(node, float('inf')):
            continue

        expanded += 1

        # Jika tujuan ditemukan
        if node == goal:
            return reconstruct(parent, goal), cost, expanded

        # Memeriksa seluruh tetangga
        for neighbor, step_cost in graph.get(node, {}).items():

            # Menghitung biaya baru
            new_cost = cost + step_cost

            # Jika biaya baru lebih murah
            if new_cost < best_cost.get(
                neighbor,
                float('inf')
            ):

                # Simpan biaya terbaik
                best_cost[neighbor] = new_cost

                # Simpan parent
                parent[neighbor] = node

                # Masukkan ke priority queue
                heapq.heappush(
                    frontier,
                    (new_cost, neighbor)
                )

    # Jika tidak ditemukan
    return None, None, expanded

# ==========================================
# RECONSTRUCT PATH
# ==========================================

def reconstruct(parent, goal):
    """
    Membentuk kembali lintasan dari node awal
    sampai node tujuan berdasarkan dictionary parent.
    """

    path = [goal]

    while path[-1] in parent:
        path.append(parent[path[-1]])

    path.reverse()

    return path

# ==========================================
# MENJALANKAN UCS
# ==========================================

start = 'Arad'
goal = 'Bucharest'

path, cost, expanded = ucs(
    graph,
    start,
    goal
)


# ==========================================
# MENAMPILKAN HASIL
# ==========================================

if path:
    print("=== HASIL UNIFORM-COST SEARCH ===")
    print("Kota awal        :", start)
    print("Kota tujuan      :", goal)
    print("Lintasan UCS     :", " -> ".join(path))
    print("Total biaya      :", cost)
    print("Node dieksplorasi:", expanded)
else:
    print(
        "Tidak ditemukan lintasan dari",
        start,
        "ke",
        goal
)