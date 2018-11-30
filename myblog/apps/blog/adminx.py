import xadmin
from .models import Banner, Category, Tag, Tui, Article, Link
from xadmin import views


# 导入需要管理的数据库表
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "博客后台管理系统"
    site_footer = "唐文鹏"
    menu_style = "accordion"  # 折叠菜单


class ArticleAdmin(object):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    # 后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面


class BannerAdmin(object):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


class CategoryAdmin(object):
    list_display = ('id', 'name', 'index')


class TagAdmin(object):
    list_display = ('id', 'name')


class TuiAdmin(object):
    list_display = ('id', 'name')


class LinkAdmin(object):
    list_display = ('id', 'name', 'linkurl')


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Tui, TuiAdmin)
xadmin.site.register(Link, LinkAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
