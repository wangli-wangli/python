from django.contrib import admin
from  .models import  Article
#在admin中显示数据的其他内容
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')#在admin中显示这三个属性
    list_filter = ('pub_time',)#admin过滤器，按照pub_time排序

admin.site.register(Article,ArticleAdmin)#在admin中注册Article类,在admin中显示数据的其他内容
