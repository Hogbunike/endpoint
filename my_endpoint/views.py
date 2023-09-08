from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

import pytz


# Create your views here.

def get_info(request):
    slack_name = request.GET.get('slack_name', 'Ogbunike Henry Chukwuebuka')
    track = request.GET.get('track', '')

    # get current day
    current_datetime = datetime.now(pytz.utc)
    current_day = current_datetime.strftime('%A')

    # get utc time
    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    time_diff = (current_datetime - utc_time).total_seconds()
    max_time_diff = 120
    
    if abs(time_diff) <= max_time_diff:
        time = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    else:
        time = ''


    # github urls
    github_repo_url = 'https://github.com/Hogbunike/endpoint.git'
    github_file_url = 'https://github.com/Hogbunike/endpoint/blob/e186f0666d78a265991bb278ec16bb9c2f379ec7/my_endpoint/views.py'


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