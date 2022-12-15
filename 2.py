#алгоритм поиска в глубину, основан на методе set, множество уникальных элементов
visited = set()
def depth(graph, start):
    global visited
    visited.add(start)
    #print(start,visited)
    for next in list(graph[start]):
        print("Предполагаемый путь :",start,next,visited)
        if next not in visited:
            print("Путь :",start,next,visited)
            depth(graph, next)
    return visited


graph = {'0': ('1', '2', '3')[::-1],
         '1': ('0', '2')[::-1],
         '2': ('0', '1', '4')[::-1],
         '3': ('0'),
         '4': ('2')
        }
print('Поиск в глубину')
depth(graph, '0')
print('\n')

#алгоритм поиска в ширину
visited = set()
queue = []
def bfs(visited, graph, node):
    global queue
    visited.add(node)
    queue.append(node)
    while queue:
        start = queue.pop(0)
        
        for next in graph[start]:
            print("Предполагаемый путь :",start,next,visited)
            if next not in visited:
                print("Путь :",start,next,visited)
                visited.add(next)
                queue.append(next)

print('Поиск в ширину')
bfs(visited, graph, '0')

# Сложность алгоритмов
# V - колиество вершин, E - количество рёбер
# временаня сложность обоих алгоритмов O(V + E), т.к. происходит перебор всех вёбер и вершин    
