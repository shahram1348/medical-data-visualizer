import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where(df.weight / (df.height/100)**2 > 25, 1, 0)

# 3 normalize cholesterol and gluc columns
df.cholesterol = np.where(df.cholesterol > 1 , 1, 0)
df.gluc = np.where(df.gluc > 1, 1, 0)


# 4
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')

    # Get the figure for the output
    fig = fig.figure

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] <= df['weight'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['ap_lo'] <= df['ap_hi'])
    ]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))



    # 14
    fig, ax = plt.subplots(figsize = (10, 10))

    # 15
    sns.heatmap(corr, vmin = 0, vmax = 0.25, fmt = '.1f', linewidth = 1, annot = True, square = True, mask = mask, cbar_kws = {'shrink': 0.6} )


    # 16
    fig.savefig('heatmap.png')
    return fig