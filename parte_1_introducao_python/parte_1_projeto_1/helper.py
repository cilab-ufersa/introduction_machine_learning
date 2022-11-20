import pandas as pd
import re
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML

def data_from_url(url):
    df = pd.read_html(url)[1]
    lol = df.to_numpy().tolist()
    return lol

def fetch_year(date_string):
    return int(re.findall("\d{4}", date_string)[0])

def barplot(list_of_2_element_list):
    d = {ya[0]:ya[1] for ya in list_of_2_element_list}
    plt.figure(figsize=(9,15))
    axes = plt.axes()
    axes.get_xaxis().set_visible(False)

    spines = axes.spines
    spines['top'].set_visible(False)
    spines['right'].set_visible(False)
    spines['bottom'].set_visible(False)
    spines['left'].set_visible(False)
    ax = plt.barh(*zip(*d.items()), height=.5)
    plt.yticks(list(d.keys()), list(d.keys()))
    plt.xticks(range(4), range(4))
    rectangles = ax.patches
    for rectangle in rectangles:
        x_value = rectangle.get_width()
        y_value = rectangle.get_y() + rectangle.get_height() / 2
        space = 5
        ha = 'left'
        label = "{}".format(x_value)
        if x_value > 0:
            plt.annotate(
                label,
                (x_value, y_value),
                xytext=(space, 0),
                textcoords="offset points",
                va='center',
                ha=ha)

    axes.tick_params(tick1On=False)
    plt.show()

def unique_countries(countries):
    s = pd.Series(countries)
    return list(s.unique())

def display_no_index(df):
    display(HTML(df.to_html(index=False)))
    
def print_pretty_table(countries_frequency):
    countries = df.Country.value_counts().index
    occurrences = df.Country.value_counts().values
    d = {"Country": countries, "Number of Occurrences": occurrences}
    display_no_index(pd.DataFrame(d))

df = pd.read_html("https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes")[1]
df = df[["Date", "Prison name", "Country", "Succeeded", "Escapee(s)"]]