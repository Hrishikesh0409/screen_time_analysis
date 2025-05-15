import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV data
df = pd.read_csv('screen_time_data.csv')

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Pivot data for each metric
def plot_metric(metric, ylabel, filename):
    pivot_df = df.pivot(index='Date', columns='App', values=metric)
    pivot_df.plot(figsize=(12, 6), marker='o')
    plt.title(f'{metric} Over 30 Days')
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.legend(title='App')
    plt.tight_layout()
    plt.savefig(f'charts/{filename}')
    plt.clf()

# Plot each metric
plot_metric('ScreenTimeMinutes', 'Minutes', 'screen_time_chart.png')
plot_metric('Notifications', 'Notifications', 'notifications_chart.png')
plot_metric('TimesOpened', 'Times Opened', 'times_opened_chart.png')
