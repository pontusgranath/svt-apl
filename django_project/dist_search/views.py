from django.shortcuts import render
import pandas as pd

def home(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    columns = list(data.columns)

    c = {'columns': columns}

    return render(request, 'dist_search/home.html', c)
