# statistical-simulation-multi-dimensional-random-walk-probabilities

## Project Overview

This project investigates the behavior of random walks in various spatial dimensions (1D, 2D, 3D) through Monte Carlo simulations, specifically focusing on the **probability of returning to the origin** within a fixed number of steps.


## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_simulation.py            # Simulates random walks and saves raw results
│   ├── 02_analyze_results.py       # Analyzes simulation results and computes probabilities
│   └── 03_plot_results.py          # Visualizes the results using bar plots
├── outputs/
│   ├── simulation_results.csv      # CSV of raw trial results
│   ├── analysis_results.csv        # Summary probabilities per dimension
│   └── return_probability.png      # Visualization of return probabilities
├── requirements.txt
└── README.md
```

---

## Usage

### 1. Setup the Project:
Clone the repository.  
Ensure you have Python installed.  
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 2. Run the Simulation:
This generates raw results of return-to-origin trials for 1D, 2D, and 3D walks.
```bash
python scripts/01_simulation.py
```

### 3. Analyze the Results:
This computes return probabilities from the simulation data.
```bash
python scripts/02_analyze_results.py
```

### 4. Plot the Results:
This generates a bar plot comparing return probabilities across dimensions.
```bash
python scripts/03_plot_results.py
```

All outputs are saved in the `outputs/` directory.

---

## Requirements

- Python 3.7+
- numpy
- pandas
- matplotlib

To install all dependencies:
```bash
pip install -r requirements.txt
```