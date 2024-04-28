# Django 学习笔记

创建项目：

```bash
django-admin startproject 项目名
```

创建完的的仓库可以看一下文件结构

```bash
tree .
.
|-- 项目名
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

做一个好习惯，每个项目都用`git`来维护

```bash
git init // 将当前文件夹设置为git仓库
```

然后要进行云端仓库的连接，这里以AcWing的GitLab为例

首先我们要创建一个空白仓库，然后选择导入自己现有的仓库，接下来开始仓库的初始化配置

```bash
git config --global user.name "Day light"
git config --global user.email "1661434401@qq.com"
```

GitHub的是

```bash
git config --global user.name "Daylight131989"
git config --global user.email "uwwo2931@gmail.com"
```

当你把项目中的文件add和commit之后，接下来就

```bash
git remote add origin git@git.acwing.com:Daylight131989/webmusic.git
```

GitHub的是

```bash
git remote add origin https://github.com/Daylight131989/WebMusic.git
```

再接下来

```bash
git push --set-upstream origin master
```

这样你的第一个初始云端仓库就创建好了。

------

接下来就可以运行一下我们的Django项目了

```bash
python3 manage.py runserver 0.0.0.0:8000 // 后面的8000可替换成你自定义的调试端口
```

此时你会遇到一个问题，那就是你不可以使用这个端口，这个问题的原因是你没有在allowhost中加入这个ip这个端口，Django不会让你打开的。

所以你需要干的是去/项目名/项目名/settings.py这个文件中的

```python
ALLOWED_HOSTS = []
```

小技巧：不知道这个东西在哪的时候可以输入指令

```bash
ag ALLOWED_HOSTS
```

就可以全文搜索这个字符串。

然后改成你的IP，用字符串写

```python
ALLOWED_HOSTS = ["182.92.82.179"]
```

然后再运行一下就可以看到下面的画面

![image-20240428185334718](image-20240428185334718.png)

当你`git status`一下后会发现，存在一个名为`__pycache__`的文件夹，这个文件夹是python预编译好的，是加速代码的，并不是我们的源代码，所以我们上传仓库的时候尽量要避免上传这样的中间文件，会污染我们源代码，所以我们接下来可以这样做。

我们可以在仓库的根目录创建一个文件叫`.gitignore`

然后在里面写上

```
*/__pycache__
```

这样做完之后再`git status`就会发现这个文件不会add到我们的工作区了。

------

这个是Django的默认界面，我们当然不能在这个页面下写自己的页面。

在Django中有一个app的概念，我们现在要创建一个app

```bash
python3 manage.py startapp 你想要创建的app的名字

musicpage
	|-- __init__.py
    |-- admin.py // 用来存储管理员页面
    |-- apps.py
    |-- migrations // 系统生成的
    |   `-- __init__.py
    |-- models.py // 用来定义我们自己网站里的各种数据库表的
    |-- tests.py
    `-- views.py // 写视图的，也就是写函数的
```

------

此时我们可以进入我们的管理员页面看一下

在浏览器中输入：你的IP:8000/admin

但大概率的你打开的页面是个报错信息，这是因为需要将数据库里的内容更新一下，当你启动Django项目的时候，你会发现出现一行红色的警告，他的意思是你有多少个数据库的修改没有同步到我们的数据库里。

![image-20240428201821306](image-20240428201821306.png)

此时你可以输入以下指令来进行同步

```bash
python3 manage.py migrate
```

![image-20240428202049202](image-20240428202049202.png)

这就意味着你已经同步成功了

此时你去打开你的admin页面就会是这样的

![image-20240428202227787](image-20240428202227787.png)

为了能够登录这个管理员页面，我们需要创建一个管理员账号。

```
python3 manage.py createsuperuser
```

![image-20240428202531546](image-20240428202531546.png)

先是输入你想要创建的管理员的名称，其次是邮箱（可以不填），然后就是密码了。

这样我们就可以进入管理员页面了。

------

那么我们如何创建自己的页面呢。

其中最关键的三个文件：`models.py` `views.py` `urls.py` 

我们需要创建一个`urls.py`和一个`templates`文件夹。

```
// 在app的文件夹下
touch urls.py
mkdir templates
```

其中如果业务量小，`models`、`views`和`urls`可以是文件，业务量多了可以变成文件夹拆分成更细的模块，但`templates`必须是文件夹。

`models`：存我们的数据结构，也就是`class`之类的。

`views`：存我们的视图，也就是函数。我们每进行一次操作都是在后端实现的，那么执行这些操作的函数都存在这里。

`urls`：其实是路由，每点一个内容的话，他传的是我们的地址。根据`urls`的格式来判断我们该调用哪个函数。

`templates`：用来存我们的html文件

------

我们可先在`views.py`里写一个最简单的函数。

**views.py**

```python
from django.http import HttpResponse

def index(request): # 每一个从前端过来的页面都会有一个request，会存我们很多的页面信息
 return HttpResponse("我的第一个网页！！！！") #返回一个字符串
```

写完这个我们需要路由一下，我们去`musicpage`文件夹下的`urls.py`中写一下路由（可以照`WebMusic`下的`urls.py`抄）

**musicpage/urls.py**

```python
from django.urls import path
from musicpage.views import index # python调包过程，在哪个文件中调用哪个函数

urlpatterns = [
    path('', index, name="index"), # path是一个解析的过程，
]
```

当写完这个之后，还需要在`WebMusic`下的`urls.py`中`include`进来

**WebMusic/urls.py**

```python
from django.contrib import admin
from django.urls import path, include # 这里include

urlpatterns = [
    path('musicpage/', include('musicpage.urls')), #这里include
    path('admin/', admin.site.urls),
]
```

一般的话，如果只有一个app的话，就不需要写第5行单引号里的地址了，直接就默认打开这个页面

整个过程相当于一个接力：

1. 用户的请求（输入当前的网址）
2. 先走到`WebMusic`下的`urls.py`
3. 从`WebMusic`里的`urls.py`走到`musicpage`里的`urls.py`
4. 从`musicpage`里的`urls.py`走到`views.py`中的`index`函数，我们在这个函数里些什么用户就会看到什么

