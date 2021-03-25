from django.shortcuts import render
import requests
import json
# Create your views here.
def frontpage(request):
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    link = "https://hacker-news.firebaseio.com/v0/"
    story_requests = []
    for i in range(10):
        id = response.json()[i]
        postlink = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
        story_request = requests.get(postlink)
        story_request = story_request.json()
        story_requests.append(story_request)
    return render(request, 'story/frontpage.html', {'stories': story_requests})