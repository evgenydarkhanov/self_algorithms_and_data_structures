# неориентированный граф задан списком смежности
# найдём путь между вершинами с помощью DFS

from collections import deque
from typing import (
    Any,
    Dict,
    List,
    Optional
)


def path_bfs(
    graph: Dict[Any, List[Any]],
    start: Any,
    end: Any
):

    # (vertex, [path])
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()
        for node in graph[vertex]:
            if node not in path:
                if node == end:
                    # yield --> all paths
                    # return --> first path
                    return path + [node]
                else:
                    queue.append((node, path + [node]))
            else:
                continue


if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'f'],
        'd': ['b'],
        'e': ['b', 'f'],
        'f': ['c', 'e'],
    }
                                                                 
    print(list(path_bfs(graph, 'a', 'c')))
    print(list(path_bfs(graph, 'e', 'd')))
