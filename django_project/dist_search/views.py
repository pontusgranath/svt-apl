from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.spatial.distance import pdist, squareform
import json
import sqlite3

def calculate_inline_distance(request):
    con = sqlite3.connect('db.sqlite3')
    data = pd.read_sql('SELECT * FROM svt_statistics', con)
    data.set_index('Client ID (ns_vid)', inplace=True)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    matrix = np.matrix(data)
    columns = list(data.columns)
    res = squareform(pdist(matrix, 'hamming'))

    def distance(t1, t2):
        return res[columns.index(t1), columns.index(t2)]

    search = "Antikrundan" # TEMPORARY
    # search = request.POST.get('inline-search-title')

    dataframe = pd.DataFrame([(c, distance(search, c)) for c in columns], columns=['title', 'distance'])

    sorted_values = dataframe.sort_values('distance')[:5 + 1]

    to_list = sorted_values.values.tolist()

    context = {
        'inline_search': search,
        'inline_to_list': to_list,
        'inline_columns': columns
    }

    return render(request, 'dist_search/home.html', context)

def calculate_distance(request):
    con = sqlite3.connect('db.sqlite3')
    data = pd.read_sql('SELECT * FROM svt_statistics', con)
    data.set_index('Client ID (ns_vid)', inplace=True)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    matrix = np.matrix(data)
    columns = list(data.columns)
    res = squareform(pdist(matrix, 'hamming'))

    def distance(t1, t2):
        return res[columns.index(t1), columns.index(t2)]

    search = request.GET.get('search-title')
    try:
        dataframe = pd.DataFrame([(c, distance(search, c)) for c in columns], columns=['title', 'distance'])
    except ValueError:
        search = "Agenda"
        dataframe = pd.DataFrame([(c, distance(search, c)) for c in columns], columns=['title', 'distance'])

    try:
        amount_of_titles = int(request.GET.get('title-amount'))
    except ValueError:
        amount_of_titles = 5

    sorted_values = dataframe.sort_values('distance')[:amount_of_titles + 1]

    to_list = sorted_values.values.tolist()

    context = {
        'search': search,
        'to_list': to_list,
        'columns': columns
    }

    return render(request, 'dist_search/home.html', context)

def home(request):
    con = sqlite3.connect('db.sqlite3')
    data = pd.read_sql('SELECT * FROM svt_statistics', con)
    data.set_index('Client ID (ns_vid)', inplace=True)

    columns = list(data.columns)

    context = {'columns': columns}

    return render(request, 'dist_search/home.html', context)
