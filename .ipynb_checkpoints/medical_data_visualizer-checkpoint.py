import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
# 2
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars= ['cardio'], value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    print(df_cat)
    

    # 7
    catplot = sns.catplot(
        x='variable', y='count', hue='value', col='cardio',
        data= df_cat, kind='bar', height= 5, aspect= 1
    )


    # 8
    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
