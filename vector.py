from node2vec import Node2Vec
import networkx as nx

# Create a graph
G = nx.fast_gnp_random_graph(n=100, p=0.5)

# Create a Node2Vec model
node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)

# Learn embeddings
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Get embeddings for a node
node_id = 0
embedding = model.wv[str(node_id)]
