from django.shortcuts import render
from django.http import HttpResponse

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

def callback(request):
    return HttpResponse("callback")

