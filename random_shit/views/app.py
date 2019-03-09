from django.http import JsonResponse
from django.shortcuts import render
from youtube_api.yapi import Yapi


def index(request):

    yapi = Yapi()

    return render(request, 'test.html', {"video_id": "JTaFn-WOprY"})


def get_id(request):
    yapi = Yapi()
    return JsonResponse({'videoId': yapi.get_video_id()})
