# Enhanced MediAgents

A practical framework that helps doctors and healthcare providers make better decisions by combining multiple AI agents that work together. Each agent specializes in different aspects of medical decision-making, from analyzing symptoms to checking medical research and ensuring ethical compliance.

## What Does It Do?

MediAgents takes a patient's information (symptoms, age, medical history) and:
1. Analyzes symptoms and suggests possible diagnoses
2. Checks medical research databases to validate its suggestions
3. Ensures all recommendations follow medical ethics guidelines
4. Provides clear explanations for each recommendation

What makes it different:
- Multiple agents work in parallel, making it faster than traditional systems
- Uses probability-based decision making to express confidence levels
- Connects to medical knowledge databases for evidence-based suggestions
- Explains its decisions in clear, human-readable language

## Key Features

- **Parallel Processing**: Multiple agents work simultaneously for faster results
- **Evidence-Based**: Integrates with medical research databases
- **Ethical Checks**: Built-in verification of medical ethics compliance
- **Clear Explanations**: Every decision comes with an understandable explanation
- **Data Validation**: Robust checking of all input data
- **Extensible**: Easy to add new capabilities or knowledge sources

## Installation

```bash
# Clone the repository
git clone https://github.com/salilp42/GENAI.git
cd GENAI

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```python
from mediagents.agents import ChiefMedicalOfficerAgent
from mediagents.knowledge import MedicalKnowledgeGraph

# Initialize knowledge graph
kg = MedicalKnowledgeGraph()

# Create orchestrator
cmo = ChiefMedicalOfficerAgent(kg)

# Example patient data
patient_data = {
    "patient_id": "1234",
    "symptoms": ["fever", "cough"],
    "age": 65,
    "medical_history": ["hypertension", "flu last year"]
}

# Run the pipeline
final_decisions, explanations = await cmo.run_pipeline(patient_data)
```

## Project Structure

```
GENAI/
├── mediagents/
│   ├── agents/          # Agent implementations
│   ├── models/          # Data models and validation
│   ├── knowledge/       # Knowledge graph implementation
│   └── utils/           # Metrics and utilities
└── tests/               # Test suite
```

## Components

### Main Agents
- **Diagnostician**: Analyzes symptoms and suggests diagnoses
- **Research**: Checks medical databases for supporting evidence
- **Ethics**: Ensures recommendations follow medical guidelines
- **Validation**: Verifies consistency with medical knowledge
- **Explainability**: Creates clear explanations for decisions

### Technical Features
- Asynchronous processing for better performance
- Probability-based confidence scoring
- Medical knowledge graph integration
- Data validation and error handling
- Metrics collection for performance monitoring

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This code is a conceptual demonstration and not a medical device. Use at your own risk. Certain functionalities (e.g., real PubMed calls, Neo4j integration, advanced ML) are stubbed or simplified for illustration.

## Author

- **Salil Patel** - *Initial work* - [salilp42](https://github.com/salilp42)

## Acknowledgments

- LangChain for providing the foundation for agent interactions
- The medical informatics community for inspiration
- Open-source community for various dependencies

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT License

Copyright (c) 2024 Salil Patel
