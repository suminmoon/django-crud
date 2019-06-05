# Django - DB CRUD

#### models.py

``` bash
- DB 관련한 작업을 수행
- class 생성하기

# 클래스 변수 = DB의 필드를 나타냄
- title = models.CharField(max_length=10)
- content = models.TextField() # text 가 길 때 사용
- created_at = models.DateTimeField(auto_now_add=True)  
                                # auto_new_add : 객체 최초 1회 생성 시점의 시간을 담겠다.
- updated_at = models.DateTimeField(auto_now=True)  
                                 # auto_new : 지금 작업을 할 때 시점
```



- settings.py

```bash
USE_TZ = False  # True : templates 나 form 에서만 위에서 정의한 타임존이 적용/ False 는 DB 등 모든 작업에 적용이 됨
```



#### models.py 만들고 반드시 해야할 것!

```bash
- migrations : DB의 '설계도' 가 저장이 되는 곳
=> 설계도 : models.py가 작성이 되었고 이걸 토대로 DB를 만들라 하는 것 

$ python manage.py makemigrations 
=> models.py 작성이 끝났으면 이 모델들을 사용할 것이고 이 모델을 DB에 저장할거니 설계도를 그려줘!

$ python manage.py migrate
=> 설계도를 기반으로 테이블 만들어라


```



---

### ORM 문법(Object Relational Mapping) / CRUD

```bash
<Create>

$ python manage.py shell (python shell 열기) (DB에 데이터 생성 후 저장)
>>> from boards.models import Board  (우리가 만든 Board 객체)
>>> Board.objects.all()  # 불러오기 (실제 값이 아닌???)
<QuerySet []> (전달받은 모델 객체의 목록)
# 데이터 베이스 정렬/수정 등의 작업이 가능
# Query 관련된 문법은 objects를 통해 

# 방법 1
>>> board = Board() # board 라는 인스턴스 생성
>>> board.title = 'new board'
>>> board.content = 'Hello World'
>>> board.save()  # 데이터 저장
>>> board
<Board: Board object (1)>
>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>]>

# 방법 2
>>> board = Board(title="Second Board", content = "Django!")
# 인스턴스 생성할 때 바로 값을 넣을 수 있음
>>> board.save()
>>> board
<Board: Board object (2)>

# 방법 3
>>> Board.objects.create(title = "Third board", content = "Happy moon!")
<Board: Board object (3)>
# 바로 생성

---
>>> board = Board()
>>> board.title = "New board"

# 필드는 기본적으로 Not null이 설정된다.
>>> board.full_clean() # 유효성 검사 
 {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
 # not null인데 content 입력 안 했을 때 


```



```bash
Board.objects.~ 했을 때 출력되는 형태 지정
<models.py>
def __str__(self):
        return f'{self.id}번째 글 - {self.title} : {self.content}'

---
>>> python manage.py shell
>>> from boards.modles import Board
>>> Board.objects.all()
<QuerySet [<Board: 1번째 글 - new board : Hello World>, <Board: 2번째 글 - Second Board :
 Django!>, <Board: 3번째 글 - Third board : Happy moon!>]

```



```bash
<admin.py>
from django.contrib import admin
from .models import Board

# Register your models here.
admin.site.register(Board)  # admin 등록

$ python manage.py createsuperuser
```



```bash
<Read>

# select * from boards;
Board.objects.all()

# select * from boards where title = "new board";
>>> Board.objects.filter(title ="new board")
<QuerySet [<Board: 1번째 글 - new board : Hello World>]>
>>> Board.objects.create(title = "new board", content =  "happy django")
<Board: 4번째 글 - new board : happy django>

>>> Board.objects.create(title = "new board", content =  "happy django")
>>> Board.objects.filter(title = "new board")
<QuerySet [<Board: 1번째 글 - new board : Hello World>, <Board: 4번째 글 - new board : happy django>]>

# select * from boards where title = "new board" limit 1; # 한 개만 
>>> Board.objects.filter(title = "new board").first()
<Board: 1번째 글 - new board : Hello World>

# select * from boards whrer id =1;
>>> Board.objects.get(id=1)
<Board: 1번째 글 - new board : Hello World>
# pk만 get으로 가져올 수 있다. get은 값이 중복이거나 일치하는 값이 없으면 오류가 나기 때문이다. 즉 pk에만 사용하자! get은 한 개의 값만 가져올 수 있다.

# select * from boards order by title asc;
>>> Board.objects.order_by('title').all()

# select * from boards order by title desc;
>>> Board.objects.order_by('-title').all()

# QuerySet은 List 처럼 index 접근 및 list methods 중 일부 사용 가능하나, 실제 list type은 아니다.
>>> board = Board.objects.all()[2]
<Board: 3번째 글 - Third board : Happy moon!>
>>> boards = Board.objects.all()[1:3]
<QuerySet [<Board: 2번째 글 - Second Board : Django!>, <Board: 3번째 글 - Third board : Happy moon!>]>

>>> type(boards)
<class 'django.db.models.query.QuerySet'>

# Like
>>> Board.objects.filter(content__contains="Happy")

# Startswith
>>> Board.objects.filter(content__startswith="Happy")

#Endswith
>>> Board.objects.filter(content__endswith="!")


```



```bash
<Update>

>>> board = Board.objects.get(pk=1)
>>> board.title = 'old board'
>>> board.save()
>>> board
<Board: 1번째 글 - old board : Hello World>

```



```bash
<Delete>

>>> board = Board.objects.get(pk=1)
>>> board.delete()
(1, {'boards.Board': 1})
>>> board = Board.objects.get(pk=1)
...
boards.models.Board.DoesNotExist: Board matching query does not exist.

```

