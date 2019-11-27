import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def draftgraphing():
    draft_df = pd.read_csv(
        "static/data/draft_data_1966_to_2014.csv", index_col=0)

    # Draft Winners
    draft_df['Draft_Yr'] == 1
    draft_df[draft_df['Draft_Yr'] == 1966]['WS_per_48'].mean()
    WS48_yrly_avg = draft_df.groupby('Draft_Yr').WS_per_48.mean()
    sns.set_style("white")
    plt.figure(figsize=(12, 9))

    # get the x and y values
    x_values = draft_df.Draft_Yr.unique()
    y_values = WS48_yrly_avg

    title = ('Average Career Win Shares Per 48 minutes by Draft Year (1966-2014)')
    plt.title(title, fontsize=20)

    plt.ylabel('Win Shares Per 48 minutes', fontsize=18)

    plt.xlim(1966, 2014.5)
    plt.ylim(0, 0.08)

    plt.grid(axis='y', color='grey', linestyle='--', lw=0.5, alpha=0.5)
    plt.tick_params(axis='both', labelsize=14)
    sns.despine(left=True, bottom=True)

    plt.plot(x_values, y_values)

    plt.savefig('static/img/draftwinners.png')

    # Draft Players
    players_drafted = draft_df.groupby('Draft_Yr').Pk.count()

    sns.set_style("white")
    plt.figure(figsize=(12, 9))

    x_values = draft_df.Draft_Yr.unique()
    y_values = players_drafted

    title = ('The Number of players Drafted in each Draft (1966-2014)')
    plt.title(title, fontsize=20)
    plt.ylabel('Number of Players Drafted', fontsize=18)

    plt.xlim(1966, 2014.5)
    plt.ylim(0, 250)

    plt.grid(axis='y', color='grey', linestyle='--', lw=0.5, alpha=0.5)
    plt.tick_params(axis='both', labelsize=14)
    sns.despine(left=True, bottom=True)

    plt.plot(x_values, y_values)

    plt.savefig('static/img/draftplayers.png')
