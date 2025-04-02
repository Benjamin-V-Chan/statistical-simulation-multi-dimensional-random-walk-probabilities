import pandas as pd
import os

def main():
    input_file = os.path.join("..", "outputs", "simulation_results.csv")
    output_file = os.path.join("..", "outputs", "analysis_results.csv")
    df = pd.read_csv(input_file)
    summary = df.groupby("dimension").agg(num_trials=("trial", "count"),
                                          num_returns=("returned", "sum")).reset_index()
    summary["probability"] = summary["num_returns"] / summary["num_trials"]
    summary.to_csv(output_file, index=False)
    print(summary)

if __name__ == "__main__":
    main()