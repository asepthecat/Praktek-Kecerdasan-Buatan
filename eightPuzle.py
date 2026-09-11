import heapq

# ==========================================================
# A* SEARCH UNTUK 8-PUZZLE
# ==========================================================

# State tujuan
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# ==========================================================
# HEURISTIK MANHATTAN DISTANCE
# ==========================================================

def manhattan_distance(state, goal=GOAL):
    distance = 0

    for i, tile in enumerate(state):

        # 0 adalah petak kosong, tidak dihitung
        if tile == 0:
            continue

        # Posisi sekarang
        current_row = i // 3
        current_col = i % 3

        # Posisi tujuan
        goal_index = goal.index(tile)
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        # Jarak horizontal + vertikal
        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# ==========================================================
# MENGHASILKAN STATE BERIKUTNYA
# ==========================================================

def get_neighbors(state):

    neighbors = []

    # Posisi petak kosong
    zero_index = state.index(0)

    row = zero_index // 3
    col = zero_index % 3

    # Gerakan yang mungkin
    moves = [
        (-1, 0),  # Atas
        (1, 0),   # Bawah
        (0, -1),  # Kiri
        (0, 1)    # Kanan
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Pastikan masih berada di dalam papan
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_index = new_row * 3 + new_col

            # Tukar posisi 0 dengan ubin
            new_state = list(state)

            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]

            neighbors.append(tuple(new_state))

    return neighbors


# ==========================================================
# RECONSTRUCT PATH
# ==========================================================

def reconstruct_path(parent, state):

    path = [state]

    while state in parent:
        state = parent[state]
        path.append(state)

    path.reverse()

    return path


# ==========================================================
# A* SEARCH
# ==========================================================

def a_star_8_puzzle(start, goal=GOAL):

    # Priority queue:
    # (f, g, state)
    frontier = [
        (manhattan_distance(start, goal), 0, start)
    ]

    parent = {}

    best_cost = {
        start: 0
    }

    expanded = 0

    while frontier:

        f, g, state = heapq.heappop(frontier)

        # Abaikan state yang bukan lagi biaya terbaik
        if g > best_cost.get(
            state,
            float('inf')
        ):
            continue

        expanded += 1

        # Jika mencapai goal
        if state == goal:
            path = reconstruct_path(
                parent,
                state
            )

            return path, g, expanded

        # Periksa semua kemungkinan gerakan
        for neighbor in get_neighbors(state):

            new_g = g + 1

            if new_g < best_cost.get(
                neighbor,
                float('inf')
            ):

                best_cost[neighbor] = new_g

                parent[neighbor] = state

                h = manhattan_distance(
                    neighbor,
                    goal
                )

                f = new_g + h

                heapq.heappush(
                    frontier,
                    (f, new_g, neighbor)
                )

    return None, None, expanded


# ==========================================================
# FUNGSI MENAMPILKAN PUZZLE
# ==========================================================

def print_puzzle(state):

    for i in range(0, 9, 3):

        print(
            state[i],
            state[i + 1],
            state[i + 2]
        )

    print()


# ==========================================================
# STATE AWAL
# ==========================================================

start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# ==========================================================
# MENJALANKAN A*
# ==========================================================

path, cost, expanded = a_star_8_puzzle(
    start,
    goal
)


# ==========================================================
# HASIL
# ==========================================================

print("=" * 60)
print("A* SEARCH - 8 PUZZLE")
print("=" * 60)

print("\nState Awal:")
print_puzzle(start)

print("State Tujuan:")
print_puzzle(goal)

print("Heuristik Manhattan Distance:",
      manhattan_distance(start, goal))

print("Jumlah langkah:", cost)

print("Node dieksplorasi:", expanded)

print("\nLintasan solusi:")

for i, state in enumerate(path):

    print("Langkah", i)
    print_puzzle(state)

print("=" * 60)