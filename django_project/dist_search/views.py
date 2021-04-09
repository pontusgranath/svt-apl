from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.spatial.distance import pdist, squareform
from django.views.decorators.csrf import csrf_exempt

def calculate_distance(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    matrix = np.matrix(data)
    columns = list(data.columns)
    res = squareform(pdist(matrix, 'hamming'))

    def distance(t1, t2):
        return res[columns.index(t1), columns.index(t2)]

    search = request.POST.get('search-title')
    try:
        dataframe = pd.DataFrame([(c, distance(search, c)) for c in columns], columns=['title', 'distance'])
    except ValueError:
        search = "Agenda"
        dataframe = pd.DataFrame([(c, distance(search, c)) for c in columns], columns=['title', 'distance'])

    try:
        amount_of_titles = int(request.POST.get('title-amount'))
    except ValueError:
        amount_of_titles = 5

    sorted_values = dataframe.sort_values('distance')[:amount_of_titles + 1]

    to_list = sorted_values.values.tolist()

    sub_title_dict = {}
    sub_title_distance_dict = {}

    index = 0
    for sub_title in to_list[1:]:
        # Selects only title from list with both title and distance
        sub_title = sub_title[0]

        dataframe = pd.DataFrame([(c, distance(sub_title, c)) for c in columns], columns=['title', 'distance'])

        sub_sorted_values = dataframe.sort_values('distance')[:6]

        sub_to_list = sub_sorted_values.values.tolist()

        titleList = []
        distanceList = []

        for item in sub_to_list:
            titleList.append(item[0])
            distanceList.append(item[1])

        titleList.pop(0)
        distanceList.pop(0)
        
        sub_title_dict[index] = titleList
        sub_title_distance_dict[index] = distanceList

        index += 1

    context = {
        'search': search,
        'to_list': to_list,
        'columns': columns,
        'sub_title_dict': sub_title_dict,
        'sub_title_distance_dict': sub_title_distance_dict,
    }

    return render(request, 'dist_search/home.html', context)

def home(request):
    data = pd.read_csv('Data-Table 1.csv', sep=';')
    data.set_index('Client ID (ns_vid)', inplace=True)

    columns = list(data.columns)

    context = {'columns': columns}

    return render(request, 'dist_search/home.html', context)
