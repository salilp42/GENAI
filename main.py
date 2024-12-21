#!/usr/bin/env python3
"""
Enhanced MediAgents: Main entry point
"""

import asyncio
import time
import logging

from mediagents.knowledge import MedicalKnowledgeGraph
from mediagents.agents import ChiefMedicalOfficerAgent
from mediagents.utils.metrics import MetricsCollector

async def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # Prepare knowledge graph
    kg = MedicalKnowledgeGraph()

    # Instantiate the orchestrator
    cmo = ChiefMedicalOfficerAgent(kg)

    # Example input
    patient_data = {
        "patient_id": "1234",
        "symptoms": ["fever", "cough"],
        "age": 65,
        "medical_history": ["hypertension", "flu last year"]
    }

    # Collect metrics
    metrics_collector = MetricsCollector()
    start = time.time()

    try:
        final_decisions, explanations = await cmo.run_pipeline(patient_data)
    except Exception as e:
        logging.error(f"Error: {e}")
        return

    # Record metrics
    total_latency = time.time() - start
    for dec in final_decisions:
        metrics_collector.record_metrics(
            agent_name="CMO",
            latency=total_latency,
            confidence=dec["confidence"],
            validation_success=True
        )

    # Print results
    print("=== ENHANCED MEDIAGENTS DECISION SUPPORT ===")
    print("Final Accepted Recommendations:")
    for d in final_decisions:
        print(f" - Diagnosis: {d['diagnosis']} | Confidence: {d['confidence']:.2f}")
        print(f"   Explanation: {d['explanation']}")
    print("\nAll Explanations:")
    for exp in explanations:
        print(" •", exp)

    # Summarize metrics
    metrics_collector.summarize()

    print("===========================================")

if __name__ == "__main__":
    asyncio.run(main())
