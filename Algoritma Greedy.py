# Fungsi untuk mencari rute terpendek
def find_shortest_path_greedy(graph, start_node):
    visited = set()  
    current_node = start_node  
    path = [current_node]  
    total_time = 0  

    # Perulangan sampai semua node dikunjungi
    while len(visited) < len(graph):
        visited.add(current_node)  
        neighbors = graph[current_node]  

        next_node = None  
        min_time = float('inf')  

        for neighbor, travel_time in neighbors.items():
            if neighbor not in visited and travel_time < min_time:
                next_node = neighbor
                min_time = travel_time

        if next_node is None:
            break

        path.append(next_node)
        total_time += min_time  
        current_node = next_node

    return path, total_time


# Representasi graf (graph)
graph = {
    "Masjid Al Khairiyah": {"Masjid Al Muaawanah": 5, "Masjid Syeikh Mahmudin": 10},
    "Masjid Al Muaawanah": {"Masjid Al Khairiyah": 5, "Masjid Maninjau": 8, "Masjid Al Ma'aruf": 7},
    "Masjid Syeikh Mahmudin": {"Masjid Al Khairiyah": 10, "Masjid Al Khair": 6},
    "Masjid Maninjau": {"Masjid Al Muaawanah": 8, "Masjid Islamic Center": 12},
    "Masjid Al Khair": {"Masjid Syeikh Mahmudin": 6, "Masjid Al Ma'aruf": 4},
    "Masjid Al Ma'aruf": {"Masjid Al Muaawanah": 7, "Masjid Al Khair": 4, "Masjid Islamic Center": 9},
    "Masjid Islamic Center": {"Masjid Maninjau": 12, "Masjid Al Ma'aruf": 9}
}

# Menentukan titik awal
start_node = "Masjid Al Khairiyah"

# Fungsi pencarian rute
path, total_time = find_shortest_path_greedy(graph, start_node)

# Hasil
print("Rute yang dipilih:", " -> ".join(path))
print("Total waktu tempuh:", total_time, "menit")
