import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
seq_col_brew = sns.color_palette("flag_r", 4)
sns.set_palette(seq_col_brew)

# Rolling sigma of returns
def sigma_plot(series1, weeks):

    returns_series1 = series1['last_price'].pct_change(periods=1)
    returns_series1 = pd.DataFrame(returns_series1)
    std_returns_series1 = returns_series1.rolling(weeks).std()
    std_returns_series1['date'] = series1['date']
    std_returns_series1 = std_returns_series1.rename(columns={'last_price': 'std'})
    
    std_returns_series1 = std_returns_series1[std_returns_series1['date'] > '19900101']
    # px.line(std_returns_series1, x='date', y='std')

    title1 = str(weeks/52)[0:1] + ' year rolling standard deviation: ' + str(series1.iloc[0]['name'])

    fig, axs = plt.subplots(1, 1)
    sns.lineplot(
        std_returns_series1, x='date', y='std', legend=False, 
        linewidth=1.5, ax=axs
    ).set(title=title1)

    plt.legend(loc='lower left', labels=['3y rolling standard deviation'])
    plt.ylabel("")
    plt.xlabel("")

    return fig, axs
