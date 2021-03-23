from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.spatial.distance import pdist, squareform

def calculate_distance(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    m = np.matrix(data)
    columns = list(data.columns)
    res = squareform(pdist(m, 'hamming'))

    def distance(t1, t2):
        return res[columns.index(t1), columns.index(t2)]

    search = request.POST('search-title')
    d = pd.DataFrame([(c, distance(search,c)) for c in columns], columns=['title', 'distance']) 

    sorted_values = d.sort_values('distance')

    return sorted_values

def home(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    columns = list(data.columns)

    c = {'columns': columns}

    return render(request, 'dist_search/home.html', c)
