import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def histogram_plot(series1):
    returns = series1['last_price'].pct_change(periods=1)
    returns = pd.DataFrame(returns)
    returns['date'] = series1['date']
    # returns = returns[returns['date'] > '1970-06-29']
    # returns = returns[returns['date'] < '1997-06-29']

    returns = returns.rename(columns={'last_price': 'return'})
    # returns['log(return)'] = np.log(returns['return'])

    title1 = str(series1.iloc[0]['name']) + ' weekly returns, ' + str(series1.iloc[0]
                     ['date'])[0:10] + ' to ' + str(series1.iloc[len(series1)-1]['date'])[0:10]
    fig = sns.histplot(returns, x="return", kde=True,
                       stat='probability', bins=300).set(title=title1)

    plt.ylabel("")
    plt.xlabel("")

    return fig
