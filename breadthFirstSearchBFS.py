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
# BREADTH-FIRST SEARCH (BFS)
# ==========================================

def bfs(graph, start, goal):
    """
    Mencari lintasan dari start ke goal
    menggunakan algoritma Breadth-First Search.
    """

    # Queue FIFO
    frontier = deque([start])

    # Menyimpan parent setiap node
    parent = {}

    # Node yang sudah ditemukan
    reached = {start}

    # Menghitung jumlah node yang dieksplorasi
    expanded = 0

    while frontier:

        # Mengambil node dari depan queue
        node = frontier.popleft()

        # Menambah jumlah node yang dieksplorasi
        expanded += 1

        # Jika tujuan ditemukan
        if node == goal:
            return reconstruct(parent, goal), expanded

        # Memeriksa seluruh tetangga
        for neighbor in graph.get(node, {}):

            if neighbor not in reached:

                # Tandai sebagai sudah ditemukan
                reached.add(neighbor)

                # Simpan parent
                parent[neighbor] = node

                # Masukkan ke belakang queue
                frontier.append(neighbor)

    # Jika tidak ditemukan
    return None, expanded


# ==========================================
# MENJALANKAN BFS
# ==========================================

start = 'Arad'
goal = 'Neamt'

path, expanded = bfs(graph, start, goal)


# ==========================================
# MENAMPILKAN HASIL
# ==========================================

if path:
    print("=== HASIL BREADTH-FIRST SEARCH ===")
    print("Kota awal       :", start)
    print("Kota tujuan     :", goal)
    print("Lintasan BFS    :", " -> ".join(path))
    print("Node dieksplorasi:", expanded)
else:
    print("Tidak ditemukan lintasan dari", start, "ke", goal)