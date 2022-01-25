import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot x = 'Year', y = 'CSIRO Adjusted Sea Level'
    fig, axes = plt.subplots(figsize=(16, 7))
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit 1880 - 2050
    best_fit_line = linregress(x, y)

    # line y = mx + c, where m is the gradient and c is the intercept
    x_ = pd.Series([i for i in range(1880, 2051)])
    x_2 = pd.Series([i for i in range(2000, 2051)])

    y_ = y_line(x_, best_fit_line)
    plt.plot(x_, y_)

    # Create second line of best fit 2000 - 2050
    # fist truncate original data frame
    df = df[df['Year'] >= 2000]
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    best_fit_line_2 = linregress(x, y)
    y_2 = y_line(x_2, best_fit_line_2)
    plt.plot(x_2, y_2)

    # Add labels and title
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


def y_line(x, line):
    y = line.slope * x + line.intercept
    return y

draw_plot()