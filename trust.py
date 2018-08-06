import networkx as nx
#import matplotlib.pyplot as plt
def dfs(graph,G,start,end):
	tac=0
	if end in graph[start]:
		tac=G.get_edge_data(start,end)['weight']
	else:
		visited=[]
		visited.append(start)
		stack=[x for x in graph[start]]
		tax=G[start][graph[start][-1]]['weight']
		stack1=[G[start][x]['weight'] for x in graph[start]]
		#z=stack1.pop()
		#print z
		while stack and tac==0:
			node=stack.pop()
			print(node) 
			if node not in visited:
				if end in graph[node]:
					print(("in 19:",tax))
					tac=(tax*G[node][end]['weight'])+((1-tax)*(1-G[node][end]['weight']))
					break
				else:
					if not node in graph:
						tax=stack1.pop()
						print(("in 27:",tax))
					else:
						print("in 29")
						tax=(tax*G[node][graph[node][-1]]['weight'])+((1-tax)*(1-G[node][graph[node][-1]]['weight']))
						stack.extend(x for x in graph[node] if x not in visited)
						stack1.append(tax)
				visited.append(node)
			else:
				tax=stack1.pop()
			print(tax)
	print(tac)
file=open('input.txt')
lines=file.readlines()
G=nx.DiGraph()
graph={}
i=1
for line in lines:
        print (i)
	s=line.split()
	G.add_edge(s[0],s[1],weight=float(s[2]))
	if s[0] not in graph:
		graph[s[0]]=[]
	graph[s[0]].append(s[1])
	i=i+1
for key,items in list(graph.items()):
	#print key," ",items
	list=[]
	for s in items:
		list.append(G[key][s]['weight'])
	pairs=list(zip(list,items))
	pairs.sort()
	graph[key]=[x[1] for x in pairs]
print("\n\n")
print((G.get_edge_data('A','D')['weight']))
for key,items in list(graph.items()):
	print((key," ",items))
dfs(graph,G,'A','D')
"""pos=nx.spring_layout(G)
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_edges(G,pos,edgelist=elarge)
nx.draw_networkx_edges(G,pos,edgelist=esmall,edge_color='b',style='dashed')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.axis('off')
plt.show()"""
	
