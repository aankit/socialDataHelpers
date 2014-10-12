# import nltk 
# nltk.data.path.append('./tweetEasy/nltk_data/') #this may need to change depending on when
# from nltk.corpus import stopwords

import queryTwitter, tweetEasy, community
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
q = 'common core'
c = 100
num_iterations = 25

commonCore = queryTwitter.SearchTwitter(q, c, num_iterations)
statuses = commonCore.runQuery()

search = tweetEasy.ParseSearch(statuses)
data = search.getDict('hashtags', 'screen_name')

def graph_add_node(n, color):
    if g.has_node(n):
        g.node[n]['weight']+=1
    else:
        g.add_node(n)
        g.node[n]['label'] = n
        g.node[n]['color'] = color
        g.node[n]['weight'] = 1
            
def graph_add_edge(n1, n2):
    if g.has_edge(n1, n2):
        g[n1][n2]['weight']+=1
    else:
        g.add_edge(n1,n2)
        g[n1][n2]['weight']=1

for k, v in data.items():
	graph_add_node(k, 1)
	for i in v: 
		graph_add_node(i, 0)
		graph_add_edge(k,i)

print g.number_of_nodes()
print g.number_of_edges()

#community detection
partition = community.best_partition(g)
modularity = community.modularity(partition, g)
values = [g.node[n]['color'] for n in g.nodes()]

nx.draw(g, cmap = plt.get_cmap('jet'), node_color=values, with_labels=True)
# nx.draw(g)
plt.show()

nx.write_gexf(g, '%s_tweet_graph.gexf' % q)
print '%s_tweet_graph.gexf' % q





