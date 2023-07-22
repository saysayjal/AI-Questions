graph={
    "a"=["b","c"],
    "b"=["d","e"],
    "c"=["f","g"],
    "d"=[],
    "e"=[],
    "f"=[],
    "g"=[],
}

closed_list={}
traversed_output=[]
for node in graph.keys():
    closed_list[node]="not visited";

def dfs(u):
    closed_list[u]="visited";
    traversed_output.append(u);
    for v in graph[u]:
        if closed_list[v]!="visited":
            dfs(v);
    
    print("Depth First Search");
    start_node=input("Enter the start node: ");
    dfs(start_node);
    print("our traversed output is= ",traversed_output);
