graph = {
    'A' : ['B','C'], 'B' : ['A','D','E'],
    'C' : ['A','F'], 'D' : ['B'],
    'E' : ['B','F'], 'F' : ['C','E']
}
visited = set() #to mark the visited nodes 
#DFS uses stack to do traversal 
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1] 
    for neighbour in neighbours:
        if neighbour not in visited: 
            dfs(graph, neighbour)
#test 
dfs(graph,'A')

'''
def dfs(graph, node):
    global visited 

    visited.add(node)     #   -> marking as visited 
    print(node, end=' ')  #   -> visited 
    #add neighbours to the stack if not visited before 
    neighbours = graph[node]
    neighbours = neighbours[::-1] #reverse neighbours 
    for neighbour in neighbours:
        if neighbour not in visited: #base cond | to traverl further
            dfs(graph, neighbour)


visited:A C F E B D| printed:A C F E B D

call stack
--------------------------

dfs@6(graph, 'D') ---
dfs@5(graph, 'B') ---
dfs@4(graph, 'E') ---
dfs@3(graph, 'F') ---
dfs@2(graph, 'C') ---
dfs@main(graph,'A') ---
--main()---         ---
--------------------------

call stack frames: state of local vars, returning place
1.@--main()---
    dfs(graph,'A') #<<<
    return>>>
2.dfs@main(graph,'A')
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1]   Cy By 
    for neighbour in neighbours:    
        if neighbour not in visited: 
            dfs@2(graph, neighbour) #<<<
    return>>>
3. dfs@2(graph, 'C')
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1] Fy Ay
    for neighbour in neighbours:   A 
        if neighbour not in visited: 
            dfs@3(graph, neighbour='F') #<<<
    return>>>
4. dfs@3(graph, 'F')
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1] Ey Cy
    for neighbour in neighbours:   
        if neighbour not in visited: 
            dfs@4(graph, neighbour='E') #<<< 
    return>>>
5. dfs@4(graph, 'E')
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1] Fy By
    for neighbour in neighbours:  
        if neighbour not in visited: 
            dfs@5(graph, neighbour='B') #<<<
    return>>>
6. dfs@5(graph, 'B')
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1] Ey Dy Ay
    for neighbour in neighbours: A
        if neighbour not in visited: 
            dfs@6(graph, neighbour='D') #<<<
    return >>>

7. dfs@6(graph, 'D')
def dfs(graph, node):
    global visited 

    visited.add(node)     
    print(node, end=' ')  
    
    neighbours = graph[node]
    neighbours = neighbours[::-1] By
    for neighbour in neighbours:  
        if neighbour not in visited: 
            dfs(graph, neighbour)
    return>>>
'''