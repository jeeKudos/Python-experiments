import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
print("Enter the number of nodes in the graph")
n = int(input())
edges = []
arr = np.zeros((n,n))
a = nx.DiGraph()
a.add_nodes_from(list((range(n))))
print("Enter all edges in source target format")
while True:
    t = tuple(int(x.strip()) for x in input().split(' '))
    print("Any more edges(y/n)")
    check = input()
    edges.append(t)
    if (check =='n'):
        break
a.add_edges_from(edges)
nx.draw(a,with_labels=True)
print("Adjacency matrix ")
for edge in edges:
    # condition to check if the edge is in correct range to be added
    y=edge[0]
    z=edge[1]
    arr[y][z]=1
print (arr)
print("Adjacency list")
for i in range(n):
    print(i," ->")
    for j in range(n):
        if(arr[i][j]==1):
            print("\t",j)
incidence_matrix = np.zeros((len(a),a.number_of_edges()))
i=0;
for g in a.edges():
    incidence_matrix[g[0]][i] = incidence_matrix[g[0]][i] +1
    incidence_matrix[g[1]][i] = incidence_matrix[g[1]][i] -1
    i = i+1
print("Incidence matrix is ")
print(incidence_matrix) 