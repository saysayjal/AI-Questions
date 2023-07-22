import queue 
adj_list={
    "a":["b","c","d"],
    "b":["e","f"],
    "c":["g","h"],
    "d":["i"],
    "e":[],
    "f":[],
    "g":[],
    "h":[],
    "i":[]
}

visited=[];
queue=[];
traversed_output=[];

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m=queue.pop(0);
        traversed_output.append(m);
        
        for neighbor in graph[m]:
            
            if neighbor not in visited:
                visited.append(neighbor);
                queue.append(neighbor);
    print("our traverse output=",traversed_output);
print("Breadth First Search");
rootnode=input("Enter the root node: ");
bfs(visited,adj_list,rootnode);