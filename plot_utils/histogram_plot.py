from ctypes import sizeof
from turtle import color
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from textwrap import wrap

# set theme and style
sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
seq_col_brew = sns.color_palette("flag_r", 4)
sns.set_palette(seq_col_brew)

def histogram_plot(series1):
    returns = series1['last_price'].pct_change(periods=1)
    returns = pd.DataFrame(returns)
    returns['date'] = series1['date']
    # returns = returns[returns['date'] > '1999-01-01']
    # returns = returns[returns['date'] < '1997-06-29']

    returns = returns.rename(columns={'last_price': 'return'})
    # returns['log(return)'] = np.log(returns['return'])

    title1 = str(series1.iloc[0]['name']) + ' weekly returns, ' + str(returns.iloc[0]
                                                                      ['date'])[0:10] + ' to ' + str(series1.iloc[len(series1)-1]['date'])[0:10]

    fig, axs = plt.subplots(1, 1)
    sns.histplot(returns, x="return",
                 kde=True, stat='probability', bins=300,
                 ax=axs, kde_kws=dict(bw_adjust=0.4), line_kws=dict(linewidth=1)
                 )
    # axs.set(title=title1)
    axs.set_title("\n".join(wrap(title1, 45)))

    plt.ylabel("")
    plt.xlabel("")

    return fig, axs
