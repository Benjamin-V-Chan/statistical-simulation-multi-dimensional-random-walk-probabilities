# statistical-simulation-multi-dimensional-random-walk-probabilities

## Project Overview

This project investigates the behavior of random walks in various spatial dimensions (1D, 2D, 3D) through Monte Carlo simulations, specifically focusing on the **probability of returning to the origin** within a fixed number of steps.

### Mathematical Background

A **random walk** is a mathematical process that describes a path consisting of a succession of random steps. In $\( d \)$-dimensional Euclidean space $\( \mathbb{R}^d \)$, we define a symmetric random walk as a stochastic process $\( \{X_n\}_{n \geq 0} \)$, where each $\( X_n \in \mathbb{Z}^d \)$ and

$$X_0 = 0,$$
$$X_{n+1} = X_n + \epsilon_n,$$
with $\( \epsilon_n \in \{\pm e_1, \pm e_2, ..., \pm e_d\} \)$ where $\( \{e_i\} \)$ are standard basis vectors in $\( \mathbb{R}^d \)$, and each step is chosen uniformly at random.

The central question: What is the probability $\( P_d(n) \)$ that the walk returns to the origin within $\( n \)$ steps in $\( d \)$-dimensions?

### Theoretical Result

Let $\( P_d = \lim_{n \to \infty} P_d(n) \)$ be the limiting probability of return to the origin. Then:

- In 1D: $$P_1 = 1$$
- In 2D: $$P_2 = 1$$
- In 3D or higher: $$P_d < 1$$

This is a classic result in probability theory:

> A simple symmetric random walk is **recurrent** in 1 and 2 dimensions (returns to the origin with probability 1), and **transient** in 3 or more dimensions (positive probability of never returning).

### Proof Sketch (2D Case)
Let $\( S_n \)$ be the position after $\( n \)$ steps. The probability of returning to origin is:
$$P(S_{2n} = 0) \sim \frac{1}{\pi n}$$
so the expected number of returns is:
$$\sum_{n=1}^{\infty} P(S_{2n} = 0) \sim \sum_{n=1}^{\infty} \frac{1}{\pi n} = \infty$$
Thus, by the Borel-Cantelli Lemma, the walk returns infinitely often with probability 1.

In 3D:
$$P(S_{2n} = 0) \sim \frac{C}{n^{3/2}}$$
so:
$$\sum_{n=1}^{\infty} \frac{1}{n^{3/2}} < \infty$$
Thus the probability of **ever** returning to the origin is less than 1.

This project empirically demonstrates these theoretical results through high-volume simulations.

---

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