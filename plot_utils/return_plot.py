import pandas as pd
from turtle import width
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
seq_col_brew = sns.color_palette("flag_r", 4)
sns.set_palette(seq_col_brew)


def return_plot(series1, return_period):
    returns = series1['last_price'].pct_change(periods=return_period)
    returns = pd.DataFrame(returns)
    returns['date'] = series1['date']

    returns = returns[returns['date'] > '19920101']

    returns = returns.rename(columns={'last_price': 'return'})

    title1 = str(return_period/52)[0:1] + ' year rolling return:' + ' ' + series1.iloc[1, 0]
    fig, axs = plt.subplots(1,1)
    sns.lineplot(returns, y='return', x='date', linewidth=1,
                       legend=False, linestyle='-', ax=axs)

    axs.set_title("\n".join(wrap(title1, 60)))

    plt.legend(loc='lower left', labels=['1y rolling return'])
    plt.ylabel("")
    plt.xlabel("")

    return fig, axs
