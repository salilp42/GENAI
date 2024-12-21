"""
Knowledge Graph implementation for medical relationships.
"""

from collections import defaultdict
import networkx as nx

class MedicalKnowledgeGraph:
    """
    A simple directed graph to represent medical relationships 
    (e.g., 'Fever' -> 'Infection'), plus a dictionary of relations.
    """
    def __init__(self):
        self.graph = nx.DiGraph()
        self.relations = defaultdict(list)
        # Initialize a trivial example
        self.graph.add_node("Infection")
        self.graph.add_node("Fever")
        self.graph.add_edge("Fever", "Infection")
        self.relations["Fever"].append("Infection")

    def is_consistent(self, recommendation: str) -> bool:
        """
        Check if recommendation is in the graph or 
        if there's a path from symptoms to recommendation.
        """
        return recommendation in self.graph.nodes
