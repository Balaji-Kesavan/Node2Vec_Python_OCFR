Node2Vec is available in various libraries, including:

Python's node2vec package: A straightforward implementation.
Gensim: Often used for training Word2Vec models, which can be adapted to train Node2Vec embeddings.

In Node2Vec, we start at a dot (node) and take a walk along the lines (edges) to visit other dots. But how we choose where to walk next can vary.
If we want to get a good sense of what’s happening right around our starting dot, we take short hops to nearby dots (this is like doing a breadth-first search or BFS).
If we’re more curious about what’s going on in the broader area, we might wander further away (this is more like a depth-first search or DFS).
Node2Vec gives us a dial, with parameters p and q, to control how we balance between these two approaches. Do we stay close to home, or do we explore the city?
