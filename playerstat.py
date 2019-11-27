import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from matplotlib.patches import Circle, Rectangle, Arc
from app import *

# insert search string
imported_search = playername_for_stat

playerid = ''

# Player : Player ID
players = {
    'Lebron James': '2544',
    'Alex Caruso': '1627936',
    'Anthony Davis': '203076',
    'Avery Bradley': '202340',
    'Kentavious Caldwell-Pope': '203484',
    'Kostas Antetokounmpo': '1628961',
    'Quinn Cook': '1626188',
    'DeMarcus Cousins': '202326',
    'Troy Daniels': '203584',
    'Danny Green': '201980',
    'Jared Dudley': '201162',
    'Talen Horton-Tucker': '1629659',
    'Kyle Kuzma': '1628398',
    'JaVale McGee': '201580',
    'Zach Norvell Jr.': '1629668',
    'Rajon Rondo': '200765',
}


def player_stat():

    # Look for ID depending on search
    for player in players:
        if imported_search == player.lower():
            playerid = players[player]

    # scraped api url
    player_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR;' +\
        'AMS=2014-15&ContextFilter;=&ContextMeasure;=FGA&DateFrom;=&D;'\
        'ateTo=&GameID;=&GameSegment;=&LastNGames;=0&LeagueID;=00&Loca;' +\
        'tion=&MeasureType;=Base&Month;=0&OpponentTeamID;=0&Outcome;=&' +\
        'PaceAdjust=N&PerMode;=PerGame&Period;=0&PlayerID;={}&Plu;'.format(playerid) +\
        'sMinus=N&Position;=&Rank;=N&RookieYear;=&Season;=2014-15&Seas;' +\
        'onSegment=&SeasonType;=Regular+Season&TeamID;=0&VsConferenc;' +\
        'e=&VsDivision;=&mode;=Advanced&showDetails;=0&showShots;=1&sh;' +\
        'owZones=0'

    # request api
    response = requests.get(player_url)
    # headers
    headers = response.json()['resultSets'][0]['headers']
    # shot chart data
    shots = response.json()['resultSets'][0]['rowSet']
    shot_df = pd.DataFrame(shots, columns=headers)

    # Court Drawing

    def draw_court(ax=None, color='black', lw=2, outer_lines=False):
        if ax is None:
            ax = plt.gca()
        hoop = Circle((0, 0), radius=7.5, linewidth=lw,
                      color=color, fill=False)
        backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
        outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                              fill=False)
        inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                              fill=False)
        top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                             linewidth=lw, color=color, fill=False)
        bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                                linewidth=lw, color=color, linestyle='dashed')
        restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                         color=color)
        corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                                   color=color)
        corner_three_b = Rectangle(
            (220, -47.5), 0, 140, linewidth=lw, color=color)
        three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                        color=color)
        center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                               linewidth=lw, color=color)
        center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                               linewidth=lw, color=color)
        court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                          bottom_free_throw, restricted, corner_three_a,
                          corner_three_b, three_arc, center_outer_arc,
                          center_inner_arc]

        if outer_lines:
            outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                    color=color, fill=False)
            court_elements.append(outer_lines)

        # Add court onto the axes
        for element in court_elements:
            ax.add_patch(element)

        return ax

    sns.set_style("white")
    sns.set_color_codes()
    plt.figure(figsize=(12, 11))
    plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)
    draw_court(outer_lines=True)

    # Descending values along the axis from left to right
    plt.xlim(300, -300)

    plt.savefig('static/img/shotchart.png')
