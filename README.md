# Agentic Chart Generator

An AI-powered chart generation system that uses LLMs to create and refine matplotlib visualizations from natural language instructions.

## Overview

This project implements an **agentic workflow** for data visualization using a **Reflection pattern**:

1. **Generate** — An LLM receives an instruction and generates Python matplotlib code
2. **Execute** — The generated code is extracted and executed against a DataFrame
3. **Reflect** — An LLM critiques the generated chart image and provides improved code based on the critique
4. **Iterate** — The reflection loop can be run multiple times to progressively refine the visualization

The reflection pattern enables self-correction: the agent reviews its own output, identifies issues, and generates an improved version.

## Project Structure

```
agentic-chart-generator/
├── charts/                 # Generated chart outputs
│   ├── chart_v1.png
│   └── chart_v2.png
├── prompts/                # LLM prompt templates
│   ├── create_chart_prompt.py
│   └── reflect_chart_prompt.py
├── services/               # API clients
│   ├── minimax_client.py   # Primary LLM client (code generation)
│   └── openrouter_client.py # Secondary LLM client (reflection)
├── generate_chart_code.py  # Chart generation pipeline
├── reflect_chart.py        # Chart reflection pipeline
├── utils.py                # Utility functions
├── main.py                 # Entry point
├── coffee_sales.csv        # Sample dataset
└── requeriments.txt        # Dependencies
```

## Requirements

- Python 3.9+
- Two LLM API providers (one for generation, one for reflection)

## Installation

```bash
pip install -r requeriments.txt
```

## Data Format

The system expects a DataFrame with these columns:

| Column        | Type       | Description                    |
| ------------- | ---------- | ------------------------------ |
| `date`        | datetime64 | Transaction date (pre-parsed)  |
| `time`        | string     | Time in HH:MM format           |
| `cash_type`   | string     | 'card' or 'cash'               |
| `card`        | string     | Card identifier                |
| `price`       | float      | Transaction price              |
| `coffee_name` | string     | Coffee product name            |
| `quarter`     | int        | Quarter (1-4, pre-computed)    |
| `month`       | int        | Month (1-12, pre-computed)     |
| `year`        | int        | Year (e.g. 2024, pre-computed) |

## Usage

```bash
python main.py
```

The pipeline will:

1. Load and prepare data from `coffee_sales.csv`
2. Generate initial chart code via the primary LLM
3. Execute the code and save to `charts/chart_v1.png`
4. Run reflection via the secondary LLM to critique and improve the chart
5. Execute improved code and save to `charts/chart_v2.png`

## Key Functions

### `generate_chart_code(out_path)`

Sends a visualization instruction to the primary LLM and returns matplotlib code wrapped in `<execute_python>` tags.

### `reflect_chart(chart_path, out_path, code)`

Uses the secondary LLM to analyze the existing chart image alongside the original code, then returns improved code with critique feedback.

### `extract_and_run_code(llm_output, df)`

Extracts Python code from LLM response and executes it against the provided DataFrame.

### `load_and_prepare_data(path)`

Loads a CSV, parses dates, and adds `year`, `month`, `quarter` columns.

## Important Constraints

- The `date` column is **datetime64** — never use string concatenation with `time`
- Always use integer columns (`year`, `quarter`) for filtering
- Always call `plt.close()` after saving figures
- Never call `plt.show()` in generated code

## Dependencies

- `requests`
- `python-dotenv`
- `pandas`
- `matplotlib`
