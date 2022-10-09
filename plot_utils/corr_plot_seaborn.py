from cmath import nan
import pandas as pd
from turtle import width
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap

# set theme and style
sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
seq_col_brew = sns.color_palette("flag_r", 4)
sns.set_palette(seq_col_brew)

# find which series is the shortest and set start date to that of the shortest series
def corr_plot_seaborn(series1, series2, corr_length):
    if len(series1) > len(series2):
        tail_length = len(series2)
        start_date = series2.iloc[0]['date'] + \
            pd.to_timedelta(corr_length, unit='W')
    else:
        tail_length = len(series1)
        start_date = series1.iloc[0]['date'] + \
            pd.to_timedelta(corr_length, unit='W')

    # set tail length as the shortest series
    series1 = series1.tail(tail_length)
    series2 = series2.tail(tail_length)

    series1.reset_index(inplace=True, drop=True)
    series2.reset_index(inplace=True, drop=True)
    
    # make it work for both yield and last_price columns
    col_name1 = 'last_price'
    col_name2 = 'last_price'
    col_name = 'last_price'
    if 'yield' in series1.columns:
        col_name1 = 'yield'
        col_name = 0
    if 'yield' in series2.columns:
        col_name2 = 'yield'
        col_name = 0

    # calc the rollling corr
    corr = series1[col_name1].rolling(corr_length).corr(series2[col_name2])

    # insert into dataframe, add dates and rename calucalted correlation column to corr
    corr = pd.DataFrame(corr)
    corr['date'] = series1['date']
    corr['corr'] = corr[col_name]
    corr = corr.drop(col_name, axis=1)

    # cutoff to startdate
    # corr = corr[corr['date'] > start_date]

    # set a title automatically
    title1 = str(corr_length/52)[0:1] + ' years rolling correlation:' + \
        ' ' + series1.iloc[1, 0] + '; ' + series2.iloc[1, 0]

    # plot it all
    fig, axs = plt.subplots(1,1)
    sns.lineplot(corr, y='corr', x='date',
                       linewidth=1.5, legend=False, ax=axs)

    axs.set_title("\n".join(wrap(title1, 60)))

    # add legend, remove labels and adjust y-axis
    plt.legend(loc='lower left', labels=['3y rolling correlation'])
    plt.ylabel("")
    plt.xlabel("")
    plt.ylim(-1.05, 1.05)

    return fig, axs
