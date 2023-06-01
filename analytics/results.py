import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore', np.RankWarning)
#plt.ylim(-2000, 39900)

def calculate_average(file_path):
    # Read the CSV file and use the second column as the index
    df = pd.read_csv(file_path, index_col=1)
    # Drop the first column
    df = df.drop(columns=['Unnamed: 0'])
    # Group the data by Model and calculate the mean
    df_mean = df.groupby('Model').mean()
    # Round the numbers to four decimal places for all columns except the Runtime [s] column
    df_mean = df_mean.round(decimals={'Accuracy': 3, 'Precision': 3, 'Recall': 3, 'F1score': 3, 'Runtime [s]': 0})
    # Order the models
    models_order = ['LogisticRegression', 'LinearSVC', 'MultinomialNB', 'RandomForestClassifier',
                    'GradientBoostingClassifier']
    df_mean = df_mean.reindex(models_order)
    df_mean.to_csv('results_average.csv')

def plot_f1score_runtime(file_path):
    # Load the csv file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Define a list of colors to use for each model
    colors = ["#1f77b4", '#ff7f0e', '#2ca02c', "#9467bd", "#bcbd22"]

    # Order the models as requested
    ordered_models = ['LogisticRegression', 'LinearSVC', 'MultinomialNB',
                      'RandomForestClassifier', 'GradientBoostingClassifier']

    # Plot F1score vs. Runtime for each model in the desired order
    for i, model in enumerate(ordered_models):
        group = df[df['Model'] == model]
        x = group['F1score']
        y = group['Runtime [s]']
        c = colors[i % len(colors)]  # cycle through colors if more models than colors
        plt.scatter(x, y, label=model, c=c)

    # Calculate and plot the line of best fit for all data
    x = df['F1score']
    y = df['Runtime [s]']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    corr_coef = df['F1score'].corr(df['Runtime [s]'])
    plt.plot(x, p(x), "red", label=f'Trendline (r = {corr_coef:.2f})')

    # Add legend, axis labels, and title to the plot
    plt.legend()
    plt.xlabel('F1score')
    plt.ylabel('Runtime [s]')
    plt.title('F1score vs. Runtime')
    plt.show()

if __name__ == '__main__':
    #calculate_average('results.csv')
    plot_f1score_runtime('results.csv')

