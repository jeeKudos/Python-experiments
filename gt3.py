from collections import defaultdict
import numpy as np
def getAllConnectedGroups(graph):
	alreadySeen= set()
	result=[]
	for node in graph:
		if node not in alreadySeen:
			connectedGroup,alreadySeen=getConnectedGroup(node,alreadySeen)
			result.append(connectedGroup)
	return result

def getConnectedGroup(node,alreadySeen):
	result=[]
	nodes=set([node])
	while nodes:
		node=nodes.pop()
		alreadySeen.add(node)
		nodes=nodes or set(graph[node])-set(alreadySeen)
		result.append(node)
	return result,alreadySeen

#graph={0:{0,1,2,3},1:set(),2:{1,2},3:{3,4,5},4:{3,4,5},5:{4,3},6:{7,8},7:{6},8:{7}}
graph= defaultdict(list)

n=int(raw_input("Enter number of nodes: "))
for i in range (1,n+1):
	data=map(int,raw_input("Enter nodes to which "+str(i)+" is connected: ").split())
	if len(data)==0:
			graph[i]=set()
	else:
		for j in data:
			graph[i].append(j)

result=getAllConnectedGroups(graph)
for comp in result:
	print comp
