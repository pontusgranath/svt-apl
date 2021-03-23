from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.spatial.distance import pdist, squareform

def calculate_distance(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    m = np.matrix(data)
    columns = list(data.columns)
    res = squareform(pdist(m, 'hamming'))

    def distance(t1, t2):
        return res[columns.index(t1), columns.index(t2)]

    search = request.POST('search-title')
    d = pd.DataFrame([(c, distance(search,c)) for c in columns], columns=['title', 'distance']) 

    sorted_values = d.sort_values('distance')

    sorted_values = {'sorted_values': sorted_values}

    return sorted_values

def home(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    columns = list(data.columns)

    c = {'columns': columns}

    return render(request, 'dist_search/home.html', c)
