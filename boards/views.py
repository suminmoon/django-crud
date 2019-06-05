from django.shortcuts import render
from .models import Board   # 작성한 model class 가져오기
# Create your views here.


def index(request):
    return render(request, 'boards/index.html')


def new(request):
    return render(request, 'boards/new.html')


def create(request):
    title = request.GET.get('title')    # 사용자가 던진 정보 확인
    content = request.GET.get('content')
    board = Board()  # model.py 에서 만들어 놓은 Board 불러서 사용
    board.title = title
    board.content = content
    board.save()
    return render(request, 'boards/create.html')
