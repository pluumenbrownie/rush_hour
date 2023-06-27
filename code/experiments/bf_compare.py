import matplotlib.pyplot as plt
import pandas as pd

def bf_plot():
    # Read the data from the csv file
    data_6x6_1 = pd.read_csv("results/breadth_first_moves_6x6_1.csv", header=0, names=['moves'])
    data_6x6_2 = pd.read_csv("results/breadth_first_moves_6x6_2.csv", header=0, names=['moves'])
    data_6x6_3 = pd.read_csv("results/breadth_first_moves_6x6_3.csv", header=0, names=['moves'])
    data_9x9_4 = pd.read_csv("results/breadth_first_moves_9x9_4.csv", header=0, names=['moves'])
    data_9x9_5 = pd.read_csv("results/breadth_first_moves_9x9_5.csv", header=0, names=['moves'])

    # Define the names of the algorithms and the scores
    boards = ['6x6_1', '6x6_2', '6x6_3', '9x9_4', '9x9_5']
    scores = [data_6x6_1['moves'][0], data_6x6_2['moves'][0], data_6x6_3['moves'][0],
              data_9x9_4['moves'][0], data_9x9_5['moves'][0]]

    # Make the bar plot
    plt.bar(boards, scores)
    plt.xlabel('Boards')
    plt.ylabel('Total moves')
    plt.title('Optimal score of the breadth-first algorithm')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust spacing to prevent label overlapping
    plt.savefig('results/output_breadth_first_scores.png')

# Call the function
bf_plot()
