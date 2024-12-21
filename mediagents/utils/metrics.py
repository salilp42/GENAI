"""
Metrics collection utilities for monitoring agent performance.
"""

from dataclasses import dataclass
from typing import Dict, List
from collections import defaultdict
import logging

@dataclass
class AgentMetrics:
    latency: float
    confidence: float
    validation_success: bool

class MetricsCollector:
    def __init__(self):
        # store metrics keyed by agent name
        self.metrics: Dict[str, List[AgentMetrics]] = defaultdict(list)

    def record_metrics(self, agent_name: str, latency: float, confidence: float, validation_success: bool):
        self.metrics[agent_name].append(AgentMetrics(latency, confidence, validation_success))

    def summarize(self):
        for agent_name, data_points in self.metrics.items():
            avg_latency = sum(m.latency for m in data_points)/len(data_points)
            avg_confidence = sum(m.confidence for m in data_points)/len(data_points)
            val_success_rate = sum(m.validation_success for m in data_points)/len(data_points)
            logging.info(f"Agent: {agent_name} | Avg Latency={avg_latency:.3f}s, "
                         f"Avg Confidence={avg_confidence:.2f}, "
                         f"Validation Success={val_success_rate*100:.2f}%")
