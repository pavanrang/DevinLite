# DevinLite

DevinLite is a simplified AI-powered software development pipeline inspired by the concept of "Devin", an AI software engineer. This project demonstrates how multiple AI agents can collaborate to solve programming tasks, simulating a complete software development lifecycle.

## Overview

DevinLite uses the CrewAI framework to orchestrate a team of AI agents, each specializing in different aspects of software development:

1. Software Architect
2. Software Programmer
3. Software Tester
4. Software Reviewer

These agents work together to take a user-defined problem and produce a solution, including architecture design, implementation, testing, and code review.

## Features

- **AI-Driven Development**: Utilizes advanced language models to power each agent.
- **Full Development Lifecycle**: Covers architecture, implementation, testing, and review.
- **Flexible Problem Solving**: Can tackle a wide range of programming tasks based on user input.
- **Tool Integration**: Includes tools for file operations and web searches to assist the AI agents.

## Requirements

- Python 3.8+
- CrewAI
- LangChain
- Groq API key (or Anthropic API key if using the Anthropic version)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/DevinLite.git
   cd DevinLite
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API key:
   - For Groq: Set the `GROQ_API_KEY` environment variable
   - For Anthropic: Set the `ANTHROPIC_API_KEY` environment variable

## Usage

Run the main script and follow the prompts:

```
python main.py
```

You will be asked to input a problem you want to solve. DevinLite will then work through the development process and provide you with a solution.

## Project Structure

- `main.py`: The entry point of the application
- `agents.py`: Defines the AI agents and their roles
- `tasks.py`: Specifies the tasks for each stage of development
- `tools/`: Contains utility tools used by the agents

## Limitations

DevinLite is a simplified version and may not handle extremely complex tasks. It's designed as a demonstration and learning tool for AI-assisted software development.

## Contributing

Contributions to DevinLite are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the concept of Devin, the AI software engineer
- Built with CrewAI and LangChain

---

For any questions or issues, please open an issue on the GitHub repository.
