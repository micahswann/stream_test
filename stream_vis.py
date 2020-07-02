#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:57:07 2020

@author: micahswann
"""

# import libraries
import os
import plotly.io as pio
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import plot
#import plotly.express as px

# display results in browsers
pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

# set current working directory
os.chdir('/Users/micahswann/Documents/GitHub/stream_test')

# request user input of station ID
station = input('Enter a station ID (KCK, MCU, or SCS) : ')

# get station name
if station == 'KCK':
    name = 'Kelsey Creek'
elif station == 'MCU':
    name = 'Middle Creek'
else:
    name = 'Scotts Creek'

# load in flow data
path = '%s' % station
path += '_flow_DWR.csv'
df = pd.read_csv(path,
                 header=[0,], index_col=4, parse_dates=True)
flow = df;

# load in stage data
path = '%s' % station
path += '_stage_DWR.csv'
df = pd.read_csv(path,
                 header=[0,], index_col=4, parse_dates=True)
stage = df;

# creating scatter of flow data
flow_data = go.Scatter(x=flow.index,
                        y=flow.VALUE,
                        line=go.scatter.Line(color='blue', width = 0.8),
                           opacity=0.8,
                           name='Flow')

# creating secondary axis with scatter of stage data
stage_data = go.Scatter(x=stage.index,
                        y=stage.VALUE,
                        line=dict(color='red', width=0.8),
                        opacity=0.8,
                        name='Stage',
                        yaxis='y2')

layout = go.Layout(height=700, width=1000, font=dict(size=20),
                   title=name,
                   
                   xaxis=dict(title='Date',
                                        # Range selector with buttons
                                         rangeselector=dict(
                                             # Buttons for selecting time scale
                                             buttons=list([
                                                 # 1 month
                                                 dict(count=1,
                                                      label='1m',
                                                      step='month',
                                                      stepmode='backward'),
                                                 # 1 week
                                                 dict(count=7,
                                                      label='1w',
                                                      step='day',
                                                      stepmode='todate'),
                                                 # 1 day
                                                 dict(count=1,
                                                      label='1d',
                                                      step='day',
                                                      stepmode='todate'),
                                                 # 12 hours
                                                 dict(count=12,
                                                      label='12h',
                                                      step='hour',
                                                      stepmode='backward'),
                                                  # Entire Scale                                                     # Entire scale
                                                 dict(step='all')
                                             ])
                                         ),
                                         # Sliding for selecting time window
                                         rangeslider=dict(visible=True),
                                         # Type of xaxis
                                         type='date'),
                   yaxis=dict(title='Flow [cfs]', color='blue'),
                   # Add a second yaxis to the right of the plot
                   yaxis2=dict(title='Stage [ft]', color='red',
                                          overlaying='y',
                                          side='right')
                   )
                   
fig = go.Figure(data=[flow_data,stage_data],layout=layout)

fig.update_layout(
    title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    

plot(fig)


pio.renderers.default = 'svg'
pio.renderers.default = 'browser'
pio.write_html(fig, file='index.html', auto_open=True)
