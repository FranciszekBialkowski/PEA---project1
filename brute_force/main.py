import timeit

def visit_city(city, visited, cost):
    global min_cost, shortest_path
    if len(visited) > 0:                                # jeżeli nie jest to pierwsze wywołanie metody
        cost += matrix[visited[-1]][city]               # zwiększ aktualną sumę wag krawędzi
    visited.append(city)                                # dodaj aktualny wierzchołek do listy już odwiedzonych

    if len(visited) < size:                             # jeżeli są jeszcze nieodwiedzone wierzchołki
        for next_city in range(size):
            if next_city not in visited:                # dla każdego nieodwiedzonego wierzchołka
                visit_city(next_city, visited, cost)        # wywołaj metodę visit_city
                visited.pop()                           # po zakończeniu każdego wywołania usuń ostatni wierzchołek
                                                            # z listy odwiedzonych

    else:
        cost += matrix[city][visited[0]]                # dodaj na koniec listy wierzchołek startowy
        visited.append(visited[0])                          # i zwiększ odpowiednio koszt

        if cost < min_cost:                             # jeżeli długość tego cyklu Hamiltona jest mniejsza od aktualnie najkrótszego, to zapisz nowe, lepsze rozwiązanie
            min_cost = cost
            shortest_path = visited.copy()
        visited.pop()


def read_from_file(file_name):
    global size, matrix, shortest_path, min_cost
    min_cost = float('inf')
    shortest_path = []
    matrix.clear()
    with open(f"problems/{file_name}") as f:
        size = int(f.readline())
        for line in f.readlines():
            matrix.append(line.split())

    matrix = [[int(x) for x in line] for line in matrix]


def test():
    global shortest_path, min_cost
    with open("program.INI", "r") as config_file:
        config_data = config_file.read().splitlines()

    with open(config_data[-1], "w") as result_file:
        for line in config_data:
            line = line.split(" ", 3)
            if len(line) > 1:
                result_file.write(f"{line[0]};{line[1]};{line[2]};{line[3]}\n")
                line = " ".join(line)
                line = line.split(" ")
                print(line)
                read_from_file(line[0])
                repeat = int(line[1])
                for i in range(repeat):
                    time = timeit.timeit(lambda: visit_city(0, [], 0), number=1)
                    path = " ".join(str(x) for x in shortest_path)
                    result_file.write(f"{time * 1000:.3f};{min_cost};[{path}]\n")

size = 0
matrix = []
min_cost = float('inf')
shortest_path = []

test()