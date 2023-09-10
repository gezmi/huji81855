import argparse
import pandas as pd
import matplotlib.pyplot as plt

def plot_scores(input_file, x_score, y_score, output_file):
    # Read the score file into a Pandas DataFrame
    df = pd.read_csv(input_file, sep='\s+', engine='python', skiprows=1)

    # Check if the specified x and y score names exist in the DataFrame
    if x_score not in df.columns or y_score not in df.columns:
        print("Error: Specified score names not found in the file.")
        return

    # Sort the DataFrame by y_score in descending order
    df = df.sort_values(by=y_score, ascending=True)

    # Calculate the number of rows to keep (top 10%)
    num_rows_to_keep = int(0.9 * len(df))

    # Slice the DataFrame to keep only the top 90% of values
    df = df.head(num_rows_to_keep)

    # Extract the x and y data
    x_data = df[x_score]
    y_data = df[y_score]

    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x_data, y_data, marker='o', color='blue', alpha=0.5)
    plt.title(f"Scatter Plot of {y_score} vs {x_score}")
    plt.xlabel(x_score)
    plt.ylabel(y_score)
    plt.grid(True)

    # Save the plot to the specified output file
    plt.savefig(output_file)

def main():
    parser = argparse.ArgumentParser(description="Generate a scatter plot from a score file.")
    parser.add_argument('-i', "--input_file", help="Path to the input score file (CSV format)")
    parser.add_argument('-x', "--x_score", help="Name of the score for the x-axis", default='rms')
    parser.add_argument('-y', "--y_score", help="Name of the score for the y-axis", default='total_score')
    parser.add_argument('-o', "--output_file", help="Path to save the plot (e.g., output.png)"
)

    args = parser.parse_args()

    if args.output_file is None:
        args.output_file=f'{args.x_score}_{args.y_score}.png'

    plot_scores(args.input_file, args.x_score, args.y_score, args.output_file)

if __name__ == "__main__":
    main()
