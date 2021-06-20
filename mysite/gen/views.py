# from django.shortcuts import render
from django.shortcuts import render
from gen.generator import generator


def index(request):

    nickname = generator

    context = {"nickname": nickname}
    return render(request, "gen/index.html", context)

# Create your views here.
