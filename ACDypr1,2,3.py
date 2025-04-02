# # from collections import deque
# #
# #
# # # Создание графа
# # class Graph:
# #     def __init__(self):
# #         self.graph = {}
# #
# #     def add_vertex(self, vertex):
# #         if vertex not in self.graph:
# #             self.graph[vertex] = []
# #
# #     def add_edge(self, v1, v2):
# #         # Добавляем рёбра в обе стороны, так как граф неориентированный
# #         self.graph[v1].append(v2)
# #         self.graph[v2].append(v1)
# #
# #     def bfs(self, start_vertex):
# #         # Создаем очередь для BFS и множество посещённых вершин
# #         queue = deque([start_vertex])
# #         visited = set([start_vertex])
# #
# #         while queue:
# #             # Извлекаем вершину из очереди
# #             vertex = queue.popleft()
# #             print(vertex, end=' ')
# #
# #             # Итерируем по соседям текущей вершины
# #             for neighbor in self.graph[vertex]:
# #                 if neighbor not in visited:
# #                     visited.add(neighbor)
# #                     queue.append(neighbor)
# #
# #
# # # Создаем неориентированный граф
# # g = Graph()
# #
# # # Добавляем вершины
# # vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# # for v in vertices:
# #     g.add_vertex(v)
# #
# # # Добавляем рёбра
# # edges = [
# #     ('A', 'B'), ('A', 'H'),
# #     ('B', 'A'), ('B', 'C'), ('B', 'G'), ('B', 'F'),
# #     ('C', 'B'), ('C', 'D'), ('C', 'F'),
# #     ('D', 'C'), ('D', 'F'), ('D', 'E'),
# #     ('E', 'D'), ('E', 'F'),
# #     ('F', 'B'), ('F', 'C'), ('F', 'D'), ('F', 'E'), ('F', 'G'),
# #     ('G', 'B'), ('G', 'F'), ('G', 'H'),
# #     ('H', 'A'), ('H', 'G')
# # ]
# #
# # for v1, v2 in edges:
# #     g.add_edge(v1, v2)
# #
# # # Поиск в ширину с началом в вершине A
# # print("Порядок обхода в ширину (BFS):")
# # g.bfs('F')
#
#
# class Graph:
#     def __init__(self):
#         self.graph = {}
#         self.pre = {}
#         self.post = {}
#         self.clock = 0
#         self.topological_order = []
#
#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []
#
#     def add_edge(self, v1, v2):
#         # Добавляем направленное ребро
#         self.graph[v1].append(v2)
#
#     def dfs(self, vertex, visited):
#         # Помечаем вершину как посещённую и записываем pre-значение
#         visited.add(vertex)
#         self.pre[vertex] = self.clock
#         self.clock += 1
#
#         # Обходим всех соседей
#         for neighbor in self.graph[vertex]:
#             if neighbor not in visited:
#                 self.dfs(neighbor, visited)
#
#         # Записываем post-значение и добавляем вершину в топологический порядок
#         self.post[vertex] = self.clock
#         self.clock += 1
#         self.topological_order.append(vertex)
#
#     def topological_sort(self):
#         visited = set()
#         self.clock = 0
#         self.topological_order = []
#
#         # Выполняем DFS для всех вершин
#         for vertex in self.graph:
#             if vertex not in visited:
#                 self.dfs(vertex, visited)
#
#         # Возвращаем обратный топологический порядок
#         return self.topological_order[::-1]
#
#     def find_sources_and_sinks(self):
#         sources = []
#         sinks = []
#
#         # Истоки — вершины без входящих рёбер
#         # Стоки — вершины без исходящих рёбер
#         in_degree = {v: 0 for v in self.graph}
#
#         # Подсчёт количества входящих рёбер для каждой вершины
#         for vertex in self.graph:
#             for neighbor in self.graph[vertex]:
#                 in_degree[neighbor] += 1
#
#         for vertex in self.graph:
#             # Истоки — вершины без входящих рёбер
#             if in_degree[vertex] == 0:
#                 sources.append(vertex)
#
#             # Стоки — вершины без исходящих рёбер
#             if len(self.graph[vertex]) == 0:
#                 sinks.append(vertex)
#
#         return sources, sinks
#
#
# # Создаем граф
# g = Graph()
#
# # Добавляем вершины
# vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# for v in vertices:
#     g.add_vertex(v)
#
# # Добавляем рёбра
# edges = [
#     ('A', 'C'), ('B', 'C'), ('C', 'D'),
#     ('C', 'E'), ('D', 'F'), ('E', 'F'),
#     ('F', 'G'), ('F', 'H')
# ]
# for v1, v2 in edges:
#     g.add_edge(v1, v2)
#
# # Выполняем топологическую сортировку
# topo_order = g.topological_sort()
# print("Топологическая сортировка:", topo_order)
#
# # Pre- и Post-значения всех вершин
# print("\nPre-значения:")
# for v in g.pre:
#     print(f"{v}: {g.pre[v]}")
#
# print("\nPost-значения:")
# for v in g.post:
#     print(f"{v}: {g.post[v]}")
#
# # Поиск истоков и стоков
# sources, sinks = g.find_sources_and_sinks()
# print("\nИстоки:", sources)
# print("Стоки:", sinks)


from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Первый шаг DFS, записываем порядок выхода вершин
    def dfs_first_pass(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_first_pass(neighbor, visited, stack)
        stack.append(v)

    # Второй шаг DFS для нахождения компонент на транспонированном графе
    def dfs_second_pass(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_second_pass(neighbor, visited, component)

    # Транспонирование графа
    def get_transposed_graph(self):
        g_transposed = Graph(self.V)
        for v in self.graph:
            for neighbor in self.graph[v]:
                g_transposed.add_edge(neighbor, v)
        return g_transposed

    # Поиск SCC (компонент сильной связности) алгоритмом Косарайю
    def kosaraju_scc(self):
        stack = []
        visited = {v: False for v in self.V}

        # Шаг 1: DFS и запись в стек по времени завершения
        for v in self.V:
            if not visited[v]:
                self.dfs_first_pass(v, visited, stack)

        # Шаг 2: Транспонирование графа
        g_transposed = self.get_transposed_graph()

        # Шаг 3: Очистка visited и выполнение DFS на транспонированном графе
        visited = {v: False for v in self.V}
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                g_transposed.dfs_second_pass(v, visited, component)
                sccs.append(component)

        return sccs


# Вершины графа
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# Создаем граф и добавляем рёбра
g = Graph(vertices)
edges = [
    ('A', 'B'), ('A', 'D'), ('B', 'E'), ('B', 'C'), ('C', 'F'),
    ('D', 'H'), ('E', 'A'), ('E', 'H'), ('F', 'I'), ('G', 'D'),
    ('H', 'I'), ('H', 'G'), ('H', 'F'), ('I', 'H')
]

for u, v in edges:
    g.add_edge(u, v)

# Найдем компоненты сильной связности
sccs = g.kosaraju_scc()
print("Компоненты сильной связности:", sccs)
