import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    input_file = os.path.join("..", "outputs", "analysis_results.csv")
    df = pd.read_csv(input_file)
    plt.figure()
    plt.bar(df["dimension"].astype(str), df["probability"])
    plt.title("Probability of Returning to Origin by Dimension")
    plt.xlabel("Dimension")
    plt.ylabel("Probability")
    output_path = os.path.join("..", "outputs", "return_probability.png")
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    main()