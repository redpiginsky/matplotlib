import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import os

from IPython.display import HTML
from matplotlib.pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
csv_path = os.path.dirname(__file__) + '/data/test.csv'
df = pd.read_csv(csv_path, usecols=['name', 'group', 'year', 'value', 'country'])
fig, ax = plt.subplots(figsize=(15, 8))

def draw_barchart(year):

    colors = dict(zip(['China', 'Japan'], ['#adb0ff', '#ffb3ff']))
    group_lk = df.set_index('name')['country'].to_dict()

    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value, i, name, size = 14, weight='600', ha='right', va='bottom')
        ax.text(value, i - .25, group_lk[name], ha='right', va='baseline')
        ax.text(value, i, value, ha='left')
    ax.text(1, 0.4, str(year)+'年', transform=ax.transAxes, size=46, ha='right')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    plt.box(False)


animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1851, 1864))
HTML(animator.to_jshtml())
writer = animation.FFMpegWriter()
# animator.to_html5_video()
animator.save('sine_wave.gif', writer='pillow')


