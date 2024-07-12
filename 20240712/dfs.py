graph = {
    'A' : ['B','C'], 'B' : ['A','D','E'],
    'C' : ['A','F'], 'D' : ['B'],
    'E' : ['B','F'], 'F' : ['C','E']
}
visited = set() #to mark the visited nodes 
#DFS uses stack to do traversal 
def dfs(graph, start):
    global visited 
    stack = [start] #python list can become the stack | append-to add | pop-to remove LIFO
    
    while stack:
        node = stack.pop()      
        if node not in visited: #after removed from stack [cond: not visited before]
            visited.add(node)     #   -> marking as visited 
            print(node, end=' ')  #   -> visited 
            #add neighbours to the stack if not visited before 
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)
#test 
dfs(graph,'A')
'''
visited:A C F E B D      print:A C F E B D        stack: x
'''