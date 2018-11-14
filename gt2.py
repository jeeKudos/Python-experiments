#shortest path problem for evacuation routes during flood based on water level

from collections import defaultdict

class Graph():
        def __init__(self):
                self.edges=defaultdict(list)
                self.waterLevel={}
        def addEdge(self,fromNode,toNode,waterLevel):
                self.edges[fromNode].append(toNode)
                self.edges[toNode].append(fromNode)
                self.waterLevel[(fromNode,toNode)]=waterLevel
                self.waterLevel[(toNode,fromNode)]=waterLevel
graph=Graph()
edges=[('Vellayambalam','Kowdiar',2),('Kowdiar','Museum',3),('Museum','Thampanoor',5),('Thampanoor','East Fort',1),('Museum','Statue',2),('Museum','Palayam',3),('Statue','Palayam',4),('Palayam','Pattom',7),('Palayam','Kesavadasapuram',2),('Pattom','PMG',1),('PMG','Plamoodu',1),('Plamoodu','Kesavadasapuram',2),('Plamoodu','Ulloor',4),('Museum','Ulloor',3),('Ulloor','Chavadimukku',1)]

for edge in edges:
        graph.addEdge(*edge)

def dijsktra(graph,initial,end):
	sp={initial:(None,0)}
	currentNode= initial
	visited=set()

	while currentNode!=end:
		visited.add(currentNode)
		destinations=graph.edges[currentNode]
		weightToCurrentNode=sp[currentNode][1]
		for nextNode in destinations:
			waterLevel=graph.waterLevel[(currentNode,nextNode)]+weightToCurrentNode
			if nextNode not in sp:
				sp[nextNode]=(currentNode,waterLevel)
			else:
				currentShortestWeight=sp[nextNode][1]
				if currentShortestWeight>waterLevel:
					sp[nextNode]=(currentNode,waterLevel)
		nextDestinations={node:sp[node] for node in sp if node not in visited}
		if not nextDestinations:
			return "Route not possible"
		currentNode=min(nextDestinations,key=lambda k:nextDestinations[k][1])
	path=[]
	while currentNode is not None:
		path.append(currentNode)
		nextNode=sp[currentNode][0]
		currentNode=nextNode
	path=path[::-1]
	return path

a=raw_input("Enter starting point: ")
b=raw_input("Enter your destination: ")
path=dijsktra(graph,a,b)
print path
