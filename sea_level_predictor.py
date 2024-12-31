import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,12))
    ax = plt.scatter(x, y, label="Original Data")

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(x, y)
    x_all = range(1880, 2051)
    y_all = [slope_all * x + intercept_all for x in x_all]
    plt.plot(x_all, y_all, 'red', label='Best Fit Line (All Data)')

    # Create second line of best fit
    recent = df[df["Year"] >= 2000]
    recent_x = recent["Year"]
    recent_y = recent["CSIRO Adjusted Sea Level"]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_x, recent_y)

    x_recent = range(2000, 2051)
    y_recent = [slope_recent * x + intercept_recent for x in x_recent]
    plt.plot(x_recent, y_recent, color='green', label='Best Fit Line (2000 Onwards)')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()