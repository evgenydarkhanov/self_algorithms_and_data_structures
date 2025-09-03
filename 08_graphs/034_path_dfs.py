# неориентированный граф задан списком смежности
# найдём путь между вершинами с помощью DFS

from typing import (
    Any,
    Dict,
    List,
    Optional
)


def path_dfs(
    graph: Dict[Any, List[Any]],
    start: Any,
    end: Any
):

    # (vertex, [path])
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()
        for node in graph[vertex]:
            if node not in path:
                if node == end:
                    # yield --> all paths
                    # return --> first path
                    yield path + [node]
                else:
                    stack.append((node, path + [node]))
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
                                                                 
    print(list(path_dfs(graph, 'a', 'c')))
    print(list(path_dfs(graph, 'e', 'd')))
