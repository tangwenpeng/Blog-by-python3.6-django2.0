# Blog-by-python3.6-django2.0
### 使用django2.0+python搭建的个人博客
效果图
http://tangwenpeng.cn/
# 使用方法

1，git clone https://github.com/tangwenpeng/Blog-by-python3.6-django2.0.git

2，新建虚拟环境然后pip install -r requirements.txt

3，mysql -uroot -p 进去创建 create databases django_blog;

4，python manage.py migrate 

5，python manage.py createsuperuser #创建超级用户

6，运行python manage.py runserver
