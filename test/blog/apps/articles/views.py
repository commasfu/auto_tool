from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from apps.articles.models import ArticleInfo,TagInfo,Category,CommentInfo
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.contrib.auth.decorators import login_required
# import json
from django.http import JsonResponse

# Create your views here.
from blog.settings import MEDIA_ROOT
import os
def article_detail(request,art_id):
    if art_id:
        article = ArticleInfo.objects.filter(id=int(art_id))[0]
        article.click_num += 1
        article.save()

    all_articles = ArticleInfo.objects.all()
    # 在django内部orm模型查询集上可以支持排序和切片，但是切片不能是负索引
    # 浏览排行

    date_time = all_articles.datetimes('add_time', 'day', order='DESC')

    click_sort = all_articles.order_by('-click_num')[:6]
    # 站长推荐
    pro_arts = all_articles.order_by('-add_time')[:6]

    all_tags = TagInfo.objects.all()

    year = request.GET.get('year', '')
    month = request.GET.get('month', '')
    day = request.GET.get('day', '')

    tagid = request.GET.get('tagid', '')

    if year and month and day:
        all_articles = all_articles.filter(add_time__year=year, add_time__month=month, add_time__day=day)
        all_articles_set = set(all_articles)

    if tagid:
        tag = TagInfo.objects.filter(id=int(tagid))[0]
        all_articles = tag.article.all()
        all_articles_set1 = set(all_articles)
        # all_articles = [article for article in all_tag_articles if article in all_articles]
    try:
        a = list(all_articles_set & all_articles_set1)
        if a:
            all_articles = a
    except:
        pass

    pa = Paginator(all_articles, 2)
    pagenum = request.GET.get('pagenum', 1)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'article.html',{
        'article':article,
        'pages': pages,
        'click_sort': click_sort,
        'pro_arts': pro_arts,
        'all_tags': all_tags,
        'tagid': tagid,
        'date_time': date_time,
        'year': year,
        'month': month,
        'day': day
    })

# def article_add(request):
#     if request.method == "GET":
#         all_category = Category.objects.all()
#         return render(request,'article_add.html',{
#             'all_category':all_category
#         })
#     else:
#         title = request.POST.get('title')
#         desc = request.POST.get('desc')
#         image = request.FILES.get('image')
#         tag = request.POST.get('tag')
#         category = request.POST.get('category')
#         content = request.POST.get('content')
#
#         cat = Category.objects.filter(name=category)[0]
#         art = ArticleInfo()
#         art.title = title
#         art.desc = desc
#         art.content = content
#         art.image = 'article/'+image.name
#         art.author_id = request.user.id
#         art.category_id = cat.id
#         art.save()
#
#         tg = TagInfo()
#         tg.name = tag
#         tg.save()
#
#         tg.article.add(art)
#
#         file_name = os.path.join(MEDIA_ROOT,str(art.image))
#         with open(file_name,'wb') as f:
#             for c in image.chunks():
#                 f.write(c)
#         return redirect(reverse('index'))


@login_required(login_url='/users/user_login/')
def comment_add(request,art_id):
    if request.user:
        if art_id:
            content = request.POST.get('comment','')
            com = CommentInfo()
            com.comment_man_id = request.user.id
            com.comment_art_id = int(art_id)
            com.comment_content = content
            com.save()
            return redirect(reverse('articles:article_detail',args=[art_id]))


def love_add(request,art_id):
    if request.is_ajax():
        art = ArticleInfo.objects.filter(id=int(art_id))[0]
        art.love_num += 1
        art.save()
        result = {'a':'ok'}


        return JsonResponse(result)

def article_add(request):
    if request.method == "GET":
        all_category = Category.objects.all()
        return render(request,'article_add.html',{
            'all_category':all_category
        })
    else:
        arttitle = request.POST.get('arttitle','')
        artdesc = request.POST.get('artdesc','')
        artimage = request.FILES.get('artimage','')
        artcategory = request.POST.get('artcategory','')
        arttag = request.POST.get('arttag','')
        artcontent = request.POST.get('artcontent','')

        cat = Category.objects.filter(name=artcategory)[0]

        art = ArticleInfo()
        art.title = arttitle
        art.desc = artdesc
        art.image = 'article/'+artimage.name
        art.content = artcontent
        art.category_id = cat.id
        art.author_id = request.user.id
        art.save()

        tag = TagInfo()
        tag.name = arttag
        tag.save()

        tag.article.add(art)




        file_name = os.path.join(MEDIA_ROOT,str(art.image))
        with open(file_name,'wb') as f:
            for c in artimage.chunks():
                f.write(c)


        return redirect(reverse('index'))