from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

import pytz


# Create your views here.

def get_info(request):
    slack_name = request.GET.get('slack_name', 'Ogbunike Henry Chukwuebuka')
    track = request.GET.get('track', '')

    
    current_day = datetime.now().strftime("%A")
    utc_time = datetime.now(pytz.utc)


    # github urls
    github_repo_url = 'https://github.com/Hogbunike/endpoint.git'
    github_file_url = 'https://github.com/Hogbunike/endpoint/blob/e186f0666d78a265991bb278ec16bb9c2f379ec7/my_endpoint/views.py'


    # json response
    response_data = {
        'slack_name': slack_name,
        'track': track,
        'current_day': current_day,
        'time': utc_time,
        'github_repo_url': github_repo_url,
        'github_file_url': github_file_url,
        'status_coode': 200,
    }

    return JsonResponse(response_data)