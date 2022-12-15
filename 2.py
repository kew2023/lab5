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

#depth(graph, '0')

#алгоритм поиска в ширину

def width(, graph, start):
    visited.add(start)
    queue.append(start)
    
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        
        for next in graph[s]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
    
queue = []

width(visited, graph, '0')
