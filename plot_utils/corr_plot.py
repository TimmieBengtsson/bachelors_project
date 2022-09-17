from cmath import nan
import pandas as pd
from turtle import width
import plotly.express as px
import seaborn as sns

def corr_plot (series1, series2, corr_length):
    if len(series1) > len(series2):
        tail_length = len(series2)
        start_date = series2.iloc[0]['date'] + pd.to_timedelta(corr_length, unit='W')
    else:
        tail_length = len(series1)
        start_date = series1.iloc[0]['date'] + pd.to_timedelta(corr_length, unit='W')

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
    fig = px.line(corr, x="date", y="corr", title = str(corr_length/52) + ' years rolling correlation:'  + ' ' + series1.iloc[1,0] + '; ' + series2.iloc[1,0] ,width=600, height=400)
    fig.update_layout(xaxis_title='Date', yaxis_title='Correlation')
    
    return fig
