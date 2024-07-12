from collections import deque 
graph = {
    'A' : ['B','C'], 'B' : ['A','D','E'],
    'C' : ['A','F'], 'D' : ['B'],
    'E' : ['B','F'], 'F' : ['C','E']
}
visited = set() #to mark the visited nodes

#BFS uses queue to do traversal| 
def bfs(graph, start):
    global visited 
    #"add to queue" + "mark as visited"
    queue = deque([start]) #queue is defined using deque 
    visited.add(start)

    while queue:
        #"remove from queue" + "do visit"
        node = queue.popleft()
        print(node,end=' ')

        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                #"add to queue" + "mark as visited"
                queue.append(neighbour)
                visited.add(neighbour)
#test
bfs(graph,'A')
'''
visited: A B C D E F  print: A B C D E F queue: x
'''


