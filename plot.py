# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# # Function to read CSV files and plot line graphs
# def plot_progress(files):
#     # Initialize a figure
#     fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(20, 20))
#     fig.suptitle('Algorithm Progress Comparison', fontsize=20)

#     # Flatten the axes for easy iteration
#     axes = axes.flatten()

#     for i, file in enumerate(files):
#         # Read CSV file into a pandas DataFrame
#         df = pd.read_csv(file)

#         # Iterate over each header value and plot a line graph
#         for j, header in enumerate(df.columns):
#             ax = axes[j]
#             ax.plot(df[header], label=os.path.basename(os.path.dirname(file)))

#             # Set subplot title and labels
#             ax.set_title(header)
#             # ax.set_xlabel('Epochs')
#             # ax.set_ylabel(header)

#     # Add a single legend for all subplots
#     handles, labels = axes[0].get_legend_handles_labels()
#     fig.legend(handles, labels, loc='upper right')

#     # Adjust layout and show the plot with added padding
#     plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)
#     plt.show()

# # Directory containing the CSV files
# directory = './results'

# # Get all CSV files in the directory
# files = [os.path.join(directory, subdir, 'progress.csv') for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]

# # Call the function to plot the progress
# plot_progress(files)
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='valid')
    return y_smooth

# Function to read CSV files and plot line graphs for a specific header
def plot_header(files, header_to_plot=None):
    # Initialize a figure
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle('Algorithm Progress Comparison', fontsize=20)

    for file in files:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(file)

        # Plot a line graph for the specified header
        label = str(file).split('/')[1]
        if header_to_plot in df.columns:
            ys =smooth( df[header_to_plot], 10)
            ax.plot(ys, label=label)

    # Set plot title and labels
    ax.set_title(header_to_plot)
    ax.set_xlabel('Epochs')
    ax.set_ylabel(header_to_plot)

    # Add a legend
    ax.legend()

    # Adjust layout and show the plot
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Directory containing the CSV files
directory = './results3'
import pathlib
# Get all CSV files in the directory
files = pathlib.Path(directory).glob('**/progress.csv')
# print([str(x) for x in files])
# files = [os.path.join(directory, subdir, 'progress.csv') for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]

# Specify the header to plot
header_to_plot = 'Eval success ratio'  # Change this to the desired header

# Call the function to plot the specified header
plot_header(files, header_to_plot)
