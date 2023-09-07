from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

import pytz


# Create your views here.

def get_info(request):
    slack_name = request.GET.get('slack_name', 'Ogbunike Henry Chukwuebuka')
    track = request.GET.get('track', 'Backend')

    # get current day
    current_datetime = datetime.now()
    current_day = current_datetime.strftime('%A')
    # get utc time
    time = current_datetime.strftime('%H:%M:%S')

    # github urls
    github_repo_url = 'https//github_repo'
    github_file_url = 'https//github_repo'

    # json response
    response_data = {
        'slack_name': slack_name,
        'track': track,
        'current_day': current_day,
        'time': time,
        'github_repo_url': github_repo_url,
        'github_file_url': github_file_url,
        'status_coode': 200,
    }

    return JsonResponse(response_data)