from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.spatial.distance import pdist, squareform
import json
import sqlite3

def calculate_inline_distance(request):
    # Creates a connection to the database
    con = sqlite3.connect('db.sqlite3')
    # Gets the table named svt_statistics from the database
    data = pd.read_sql('SELECT * FROM svt_statistics', con)
    data.set_index('Client ID (ns_vid)', inplace=True)

    matrix = np.matrix(data)
    titles = list(data.columns)
    res = squareform(pdist(matrix, 'hamming'))

    # Calculates distance between 2 titles
    def distance(t1, t2):
        return res[titles.index(t1), titles.index(t2)]

    # Gets search result by fetching from the form
    inline_search = request.GET.get('inline-search-title')
    search = request.GET.get('search-title')
    amount_of_titles = int(request.GET.get('title-amount'))

    # Uses search result to create a data table with its respective headers
    inline_dataframe = pd.DataFrame([(c, distance(inline_search, c)) for c in titles], columns=['title', 'distance'])
    dataframe = pd.DataFrame([(c, distance(search, c)) for c in titles], columns=['title', 'distance'])

    # Sorts titles and sets an upper limit on how many should be displayed
    # + 1 is used since the first title always gets cut due to it being the searched title
    inline_sorted_titles = inline_dataframe.sort_values('distance')[:5 + 1]
    sorted_titles = dataframe.sort_values('distance')[:amount_of_titles + 1]

    # Creates a list / array from the sorted titles
    inline_list_of_titles = inline_sorted_titles.values.tolist()
    list_of_titles = sorted_titles.values.tolist()

    context = {
        'search': search,
        'titles': titles,
        'title_amount': amount_of_titles,
        'list_of_titles': list_of_titles,
        'inline_search': inline_search,
        'inline_list_of_titles': inline_list_of_titles,
    }

    return render(request, 'dist_search/home.html', context)

def calculate_distance(request):
    con = sqlite3.connect('db.sqlite3')
    data = pd.read_sql('SELECT * FROM svt_statistics', con)
    data.set_index('Client ID (ns_vid)', inplace=True)

    matrix = np.matrix(data)
    titles = list(data.columns)
    res = squareform(pdist(matrix, 'hamming'))

    def distance(t1, t2):
        return res[titles.index(t1), titles.index(t2)]

    search = request.GET.get('search-title')
    try:
        dataframe = pd.DataFrame([(c, distance(search, c)) for c in titles], columns=['title', 'distance'])
    except ValueError:
        search = "Agenda"
        dataframe = pd.DataFrame([(c, distance(search, c)) for c in titles], columns=['title', 'distance'])

    try:
        amount_of_titles = int(request.GET.get('title-amount'))
    except ValueError:
        amount_of_titles = 5

    sorted_titles = dataframe.sort_values('distance')[:amount_of_titles + 1]

    list_of_titles = sorted_titles.values.tolist()

    context = {
        'titles': titles,
        'search': search,
        'title_amount': amount_of_titles,
        'list_of_titles': list_of_titles,
    }

    return render(request, 'dist_search/home.html', context)

def home(request):
    con = sqlite3.connect('db.sqlite3')
    data = pd.read_sql('SELECT * FROM svt_statistics', con)
    data.set_index('Client ID (ns_vid)', inplace=True)

    titles = list(data.columns)

    context = {'titles': titles}

    return render(request, 'dist_search/home.html', context)
