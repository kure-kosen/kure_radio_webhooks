from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.logging import info, error

import json
import requests
import os

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def callback(request):
    try:
        action = json.loads(request.body.decode('utf-8'))['action']
        board_name = action['data']['board']['name']
        print(board_name)
        from pprint import pprint
        pprint(action)
    except json.JSONDecoder as e:
        error(e.msg)
    except Exception as e:
        error(e.msg)           
    return HttpResponse("callback")
