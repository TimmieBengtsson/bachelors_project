from cmath import nan
import pandas as pd
from turtle import width
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot as plt
from textwrap import wrap

# set theme and style
sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
seq_col_brew = sns.color_palette("flag_r", 4)
sns.set_palette(seq_col_brew)

def corr_plot(series1, series2, corr_length):
    if len(series1) > len(series2):
        tail_length = len(series2)
        start_date = series2.iloc[0]['date'] + \
            pd.to_timedelta(corr_length, unit='W')
    else:
        tail_length = len(series1)
        start_date = series1.iloc[0]['date'] + \
            pd.to_timedelta(corr_length, unit='W')

    series1 = series1.tail(tail_length)
    series2 = series2.tail(tail_length)

    series1.reset_index(inplace=True, drop=True)
    series2.reset_index(inplace=True, drop=True)

    col_name1 = 'last_price'
    col_name2 = 'last_price'
    col_name = 'last_price'
    if 'yield' in series1.columns:
        col_name1 = 'yield'
        col_name = 0
    if 'yield' in series2.columns:
        col_name2 = 'yield'
        col_name = 0

    corr = series1[col_name1].rolling(corr_length).corr(series2[col_name2])
    corr = pd.DataFrame(corr)
    corr['date'] = series1['date']
    corr['corr'] = corr[col_name]
    corr = corr.drop(col_name, axis=1)

    corr = corr[corr['date'] > start_date]

    fig, axs = plt.subplots(1, 1)
    title1 = str(corr_length/52) + ' years rolling correlation:' + ' ' + series1.iloc[1, 0] + '; ' + series2.iloc[1, 0]
    fig = px.line(corr, x="date", y="corr", ax=axs, title = 'xx')

    axs.set_title("\n".join(wrap(title1, 50)))
    fig.update_layout(xaxis_title='Date', yaxis_title='Correlation')

    return fig, axs
