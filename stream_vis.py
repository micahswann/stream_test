#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:57:07 2020

@author: micahswann
"""

import os
import plotly.io as pio
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell
from plotly.offline import plot

InteractiveShell.ast_node_interactivity = 'all'
pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

# set current working directory
os.chdir('/Users/micahswann/Documents/GitHub/stream_test')

df = pd.read_csv('Kelsey_DWR.csv', 
                 header=[0,], index_col=0)
df.index = pd.to_datetime(df.index)

kel = df;
stream_data = go.Scatter(x=kel.index,
                        y=kel.flow)

layout = go.Layout(title='Kelsey', xaxis=dict(title='Date'),
                   yaxis=dict(title='(cfs)'))

fig = go.Figure(data=[stream_data],layout=layout)


plot(fig)











pio.renderers.default = 'svg'
pio.renderers.default = 'browser'
#pio.write_html(fig, file='index.html', auto_open=True)
