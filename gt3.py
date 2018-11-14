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
		nodes=nodes or graph[node]-alreadySeen
		result.append(node)
	return result,alreadySeen

#graph={0:{0,1,2,3},1:set(),2:{1,2},3:{3,4,5},4:{3,4,5},5:{4,3},6:{7,8},7:{6},8:{7}}
graph={}
n=int(raw_input("Enter number of nodes: "))
for i in range (1,n+1):
	a=raw_input("Enter nodes to which node "+str(i)+" is connected: ").split(' ')
	if a=='':
		a=set()
	graph[i-1]=a
	print a
result=getAllConnectedGroups(graph)
for comp in result:
	print comp