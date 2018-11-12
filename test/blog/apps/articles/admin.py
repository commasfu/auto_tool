from django.contrib import admin

# Register your models here.
from django.contrib import admin

from apps.articles.models import ArticleInfo,Category,TagInfo,CommentInfo
# Register your models here.


# Create your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','add_time']
    fields = ['name','add_time']



class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','desc','content','is_delete','click_num','love_num','image','add_time','category']
    fields = ['title', 'author','desc','content','is_delete','click_num','love_num','image','add_time','category']



class TagInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    fields = ['name', 'add_time','article']
    filter_horizontal = ['article']



class CommentInfoAdmin(admin.ModelAdmin):
    list_display = ['comment_man', 'add_time','comment_art','comment_content','is_delete']
    fields = ['comment_man', 'add_time','comment_art','comment_content','is_delete']

admin.site.register(Category,CategoryAdmin)
admin.site.register(ArticleInfo,ArticleInfoAdmin)
admin.site.register(TagInfo,TagInfoAdmin)
admin.site.register(CommentInfo,CommentInfoAdmin)