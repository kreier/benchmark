# GPT-4 Generated Code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating DataFrame from the provided data
data = {
    "Chip": ["M1", "M1", "M1 Pro", "M1 Pro", "M1 Max", "M1 Max", "M1 Ultra", "M2", "M2 Pro", "M2 Pro", "M2 Max", "M2 Max", "M2 Ultra", "M2 Ultra", "M3", "M3 Pro", "M3 Pro", "M3 Max"],
    "BW (GB/s)":     [68, 68, 200, 200, 400, 400, 800, 100, 200, 200, 400, 400, 800, 800, 100, 150, 150, 400],
    "GPU Cores":     [7, 8, 14, 16, 24, 32, 48, 10, 16, 19, 30, 38, 60, 76, 10, 14, 18, 40],
    "F16 PP (t/s)":  [None, None, None, 302.14, 453.03, 599.53, 875.81, 201.34, 312.65, 384.38, 600.46, 755.67, 1128.59, 1401.85, None, None, 357.45, 779.17],
    "F16 TG (t/s)":  [None, None, None, 12.75, 22.55, 23.03, 33.92, 6.72, 12.47, 13.06, 24.16, 24.65, 39.86, 41.02, None, None, 9.89, 25.09],
    "Q8_0 PP (t/s)": [108.21, 117.25, 235.16, 270.37, 405.87, 537.37, 783.45, 181.4, 288.46, 344.5, 540.15, 677.91, 1003.16, 1248.59, 187.52, 272.11, 344.66, 757.64],
    "Q8_0 TG (t/s)": [7.92, 7.91, 21.95, 22.34, 37.81, 40.2, 55.69, 12.21, 22.7, 23.01, 39.97, 41.83, 62.14, 66.64, 12.27, 17.44, 17.53, 42.75],
    "Q4_0 PP (t/s)": [107.81, 117.96, 232.55, 266.25, 400.26, 530.06, 772.24, 179.57, 294.24, 341.19, 537.6, 671.31, 1013.81, 1238.48, 186.75, 269.49, 341.67, 759.7],
    "Q4_0 TG (t/s)": [14.19, 14.15, 35.52, 36.41, 54.61, 61.19, 74.93, 21.91, 37.87, 38.86, 60.99, 65.95, 88.64, 94.27, 21.34, 30.65, 30.74, 66.31]
}
df = pd.DataFrame(data)

# Helper function to plot and annotate multiple data series in the same plot
def plot_multi_series(ax, x, y_series, labels, xlabel, ylabel, title, poly_power=1):
    colors = ['r', 'g', 'b']  # Colors for different series
    for i, y in enumerate(y_series):
        # Sorting data for regression
        sorted_indices = np.argsort(x)
        x_sorted = x[sorted_indices]
        y_sorted = y[sorted_indices]

        # Masking NaN values
        mask = ~np.isnan(y_sorted)
        x_sorted = x_sorted[mask]
        y_sorted = y_sorted[mask]

        # Fitting a polynomial regression model
        coefficients = np.polyfit(x_sorted, y_sorted, poly_power)
        polynomial = np.poly1d(coefficients)

        # Creating a range of x-values for a smoother trendline
        x_range = np.linspace(x_sorted.min(), x_sorted.max(), 500)
        trendline = polynomial(x_range)

        # Plotting
        ax.scatter(x, y, color=colors[i], label=labels[i], s=20)
        ax.plot(x_range, trendline, f"{colors[i]}-", linewidth=1)  # Trendline in the same color

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()

    # Annotating points with the number of GPU cores and Bandwidth
    for i, txt in enumerate(df["Chip"]):
        ax.annotate(f"{df['GPU Cores'][i]} Cores, {df['BW (GB/s)'][i]} GB/s", (x[i], y_series[0][i]))


# Creating plots for PP vs Cores and TG vs Bandwidth
fig, axs = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle('PP vs GPU Cores and TG vs Bandwidth for F16, Q8_0, and Q4_0')

# PP vs GPU Cores
y_series_cores_pp = [df["F16 PP (t/s)"], df["Q8_0 PP (t/s)"], df["Q4_0 PP (t/s)"]]
plot_multi_series(axs[0], df["GPU Cores"], y_series_cores_pp,
                  ['F16 PP', 'Q8_0 PP', 'Q4_0 PP'], 'GPU Cores', 'Performance (t/s)',
                  'PP Performance vs GPU Cores', 1)

# TG vs Bandwidth
y_series_bw_tg = [df["F16 TG (t/s)"], df["Q8_0 TG (t/s)"], df["Q4_0 TG (t/s)"]]
plot_multi_series(axs[1], df["BW (GB/s)"], y_series_bw_tg,
                  ['F16 TG', 'Q8_0 TG', 'Q4_0 TG'], 'Bandwidth (GB/s)', 'Performance (t/s)',
                  'TG Performance vs Bandwidth', 2)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
