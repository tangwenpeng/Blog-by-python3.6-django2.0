from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from apps.blog.models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 导入分页插件包


class IndexView(View):
    """首页"""

    def get(self, request):
        all_category = Category.objects.all()  # 通过Category表查出所有分类
        banner = Banner.objects.filter(is_active=True)[0:4]  # 查询所有幻灯图数据，并进行切片
        tuijian = Article.objects.filter(tui__id=1)[:3]  # 查询推荐位ID为1的文章
        all_article = Article.objects.all().order_by("-id")[
                      0:10]  # .order_by('-id')为数据排序方式，[0:10]为只获取10索引切片，只获取最新的10篇文章。
        hot = Article.objects.all().order_by("views")[0:10]  # 通过浏览数进行排序
        remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门
        tags = Tag.objects.all()  # 所有标签
        links = Link.objects.all()  # 所有友情链接
        context = {
            'all_category': all_category,
            'banner': banner,
            'tuijian': tuijian,
            'all_article': all_article,
            'hot': hot,
            'remen': remen,
            'tags': tags,
            'links': links,
        }
        return render(request, "index.html", context)


class ListView(View):
    """列表页"""

    def get(self, request, lid):
        art_list = Article.objects.filter(category_id=lid).order_by('-created_time')  # 获取通过URL传进来的lid，然后筛选出对应文章
        all_category = Category.objects.all()  # 通过Category表查出所有分类
        cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名
        remen = Article.objects.filter(tui__id=2)[:6]  # 右侧的热门推荐
        allcategory = Category.objects.all()  # 导航所有分类
        tags = Tag.objects.all()  # 右侧所有文章标签
        page = request.GET.get('page')  # 在URL中获取当前页面数
        paginator = Paginator(art_list, 3)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
        try:
            art_list = paginator.page(page)  # 获取当前页码的记录
        except PageNotAnInteger:
            art_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
        except EmptyPage:
            art_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        return render(request, 'list.html', locals())  # 这个locals()代替了context，locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典


class ContentView(View):
    """内容页"""

    def get(self, request, sid):
        show = Article.objects.get(id=sid)  # 查询指定ID的文章
        all_category = Category.objects.all()  # 导航上的分类
        tags = Tag.objects.all()  # 右侧所有标签
        remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
        hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
        previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
        netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
        show.views = show.views + 1  # 文章的浏览数
        show.save()
        return render(request, 'show.html', locals())


class TagView(View):
    """标签页"""

    def get(self, request,tag):
        art_list = Article.objects.filter(tags__name=tag).order_by('-created_time')  # 通过文章标签进行查询文章
        remen = Article.objects.filter(tui__id=2)[:6]
        all_category = Category.objects.all()
        tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
        page = request.GET.get('page')
        tags = Tag.objects.all()
        paginator = Paginator(art_list, 5)
        try:
            art_list = paginator.page(page)  # 获取当前页码的记录
        except PageNotAnInteger:
            art_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
        except EmptyPage:
            art_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        return render(request, 'tags.html', locals())


class SearchView(View):
    """搜索页"""

    def get(self, request):
        ss = request.GET.get('search')  # 获取搜索的关键词
        art_list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
        remen = Article.objects.filter(tui__id=2)[:6]
        all_category = Category.objects.all()
        page = request.GET.get('page')
        tags = Tag.objects.all()
        paginator = Paginator(art_list, 10)
        try:
            art_list = paginator.page(page)  # 获取当前页码的记录
        except PageNotAnInteger:
            art_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
        except EmptyPage:
            art_list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        return render(request, 'search.html', locals())


class AboutView(View):
    """关于我们"""

    def get(self, request):
        all_category = Category.objects.all()
        return render(request, 'page.html', locals())
