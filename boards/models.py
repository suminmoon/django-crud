from django.db import models

# Create your models here.
class Board(models.Model):
    # id 는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True) 자동 생성되기 때문에 굳이 구현하지 않아도 된다.

    # 클래스 변수 => DB 의 필드를 나타냄
    title = models.CharField(max_length=10)
    content = models.TextField() # text 가 길 때 사용
    created_at = models.DateTimeField(auto_now_add=True)  # auto_new_add : 객체 최초 1회 생성 시점의 시간을 담겠다.
    updated_at = models.DateTimeField(auto_now=True)  # auto_new : 지금 작업을 할 때 시점
