import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def read_data_from_file(file_path):
    x_values = []
    y_values = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into date and price using the '- Price: ' separator
            date_str, price_str = line.strip().split(' - Price: ')

            # Convert date string to datetime object
            x = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

            # Extract the numeric part of the price and convert to float
            y = float(price_str.split()[0])

            x_values.append(x)
            y_values.append(y)
    return x_values, y_values

def plot_line_graph(x, y):
    fig = plt.figure(figsize=(10, 6))  # Set the figure size to 10 inches wide and 6 inches tall
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.set_title('July Gold Price Trend')

    # Format x-axis date labels to show every single day
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # Set y-axis ticks to display whole numbers from 1920 to 1991 in groups of 5
    y_ticks = np.arange(1920, 1991, 5)
    ax.set_yticks(y_ticks)

    #Rotates X axis to make dates readable
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    file_path = '/Users/dave/Documents/Coding Projects/Java/Gold 2.0/price_changes.txt'
    x_values, y_values = read_data_from_file(file_path)
    plot_line_graph(x_values, y_values)

if __name__ == "__main__":
    main()





