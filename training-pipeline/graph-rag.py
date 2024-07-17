# Graph of Thought + GraphRAG

import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict

# 1. Knowledge Graph Construction

def create_knowledge_graph() -> nx.Graph:
    """Create a simple knowledge graph"""
    G = nx.Graph()
    G.add_edges_from([
        ('AI', 'Machine Learning'),
        ('Machine Learning', 'Deep Learning'),
        ('Deep Learning', 'Neural Networks'),
        ('AI', 'Natural Language Processing'),
        ('Natural Language Processing', 'Transformers'),
        ('Transformers', 'BERT'),
        ('Transformers', 'GPT')
    ])
    return G

# Sample usage
kg = create_knowledge_graph()
print(f"Created knowledge graph with {kg.number_of_nodes()} nodes and {kg.number_of_edges()} edges")

# Visualize the graph
plt.figure(figsize=(12, 8))
nx.draw(kg, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
plt.title("Simple AI Knowledge Graph")
plt.show()

# 2. Graph Neural Network (simplified representation)

def gnn_embedding(graph: nx.Graph) -> Dict[str, List[float]]:
    """
    Simulate GNN embedding. In a real implementation, this would use a proper GNN library.
    Here, we'll just return random embeddings for each node.
    """
    import random
    return {node: [random.random() for _ in range(10)] for node in graph.nodes()}

# Sample usage
node_embeddings = gnn_embedding(kg)
print("Sample node embedding:", node_embeddings['AI'])

# 3. Graph-based Retrieval

def retrieve_subgraph(graph: nx.Graph, query: str, depth: int = 2) -> nx.Graph:
    """Retrieve a subgraph based on a query node and depth"""
    if query not in graph:
        return nx.Graph()
    
    subgraph_nodes = nx.single_source_shortest_path_length(graph, query, cutoff=depth)
    return graph.subgraph(subgraph_nodes)

# Sample usage
query = 'Machine Learning'
subgraph = retrieve_subgraph(kg, query)
print(f"Retrieved subgraph with {subgraph.number_of_nodes()} nodes")

# Visualize the subgraph
plt.figure(figsize=(10, 6))
nx.draw(subgraph, with_labels=True, node_color='lightgreen', node_size=3000, font_size=10, font_weight='bold')
plt.title(f"Subgraph for query: {query}")
plt.show()

# 4. RAG-enhanced Generation

def generate_text(subgraph: nx.Graph, query: str) -> str:
    """
    Simulate text generation based on the subgraph.
    In a real implementation, this would use a language model with the graph information as context.
    """
    nodes = list(subgraph.nodes())
    return f"Generated text about {query} involving concepts: {', '.join(nodes)}"

# Sample usage
generated_text = generate_text(subgraph, query)
print("Generated text:", generated_text)

# Full pipeline example
def graph_rag_pipeline(query: str):
    kg = create_knowledge_graph()
    node_embeddings = gnn_embedding(kg)
    subgraph = retrieve_subgraph(kg, query)
    generated_text = generate_text(subgraph, query)
    return generated_text

# Run the pipeline
result = graph_rag_pipeline("Deep Learning")
print("Final generated text:", result)