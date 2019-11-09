# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


import pandas as pd
import plotly.offline as py
import plotly.plotly as plt
import plotly
import plotly.graph_objs as go
import random
import warnings
import os
import numpy as np

warnings.filterwarnings('ignore')
df = pd.read_csv('items.csv')
df.shape
df.head(20)
def random_colors(number_of_colors):
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(number_of_colors)]
    return color

def simple_graph(dataframe,type_of_graph, top = 0):
   
    data_frame = df[dataframe].value_counts()
    layout = go.Layout()
  
    if type_of_graph == 'barh':
        top_category = get_list(df[dataframe].dropna())
        if top !=None:
            data = [go.Bar(
                x=top_category[0].head(top),
                y=top_category[1].head(top),
                marker=dict(color=random_colors(10), line=dict(color='rgb(8,48,107)',width=1.5,)),
                opacity = 0.6
        )]
        else:
            data = [go.Bar(
                x=top_category[0],
                y=top_category[1],
                marker=dict(color=random_colors(10), line=dict(color='rgb(8,48,107)',width=1.5,)),
                opacity = 0.6
            )]      

    elif type_of_graph == 'pie':
        data = [go.Pie(
            labels = data_frame.index,
            values = data_frame.values,
            marker = dict(colors = random_colors(20)),
            textfont = dict(size = 20)
        )]
    
    elif type_of_graph == 'pie_':
        data = [go.Pie(
            labels = data_frame.index,
            values = data_frame.values,
            marker = dict(colors = random_colors(20)),
            textfont = dict(size = 10)
        )]
        layout = go.Layout(legend=dict(orientation="h"), autosize=False,width=700,height=700)
        pass
    
    fig = go.Figure(data = data, layout = layout)
    i=dataframe+"_"+type_of_graph
    name="plot_"+str(i)+".jpg"
    if not os.path.exists('images'):
         os.mkdir('images')
    plotly.io.write_image(fig,'images/'+name)
    #py.plot(fig)
    #py.plot(fig)


# visiualisation de pourcentage des offres des stages par région avec bar chart
simple_graph('region','pie_')
#visualisation de pourcentage des offres des stages par recruteur avec bar chart
simple_graph('recruiter','pie_')
# visiualisation de pourcentage des offres des stages par titre de stage avec bar chart
simple_graph('title','pie_')




