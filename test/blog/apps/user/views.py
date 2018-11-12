from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.urls import reverse
from apps.user.forms import UserloginForm,UserRegisterForm
from apps.user.models import UserProfile
from django.contrib.auth import authenticate,logout,login
from apps.articles.models import ArticleInfo,TagInfo
# Create your views here.
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def index(request):
    all_articles = ArticleInfo.objects.all()
    #在django内部orm模型查询集上可以支持排序和切片，但是切片不能是负索引
    #浏览排行

    date_time = all_articles.datetimes('add_time','day',order='DESC')

    click_sort = all_articles.order_by('-click_num')[:6]
    #站长推荐
    pro_arts = all_articles.order_by('-add_time')[:6]

    all_tags = TagInfo.objects.all()

    year = request.GET.get('year','')
    month = request.GET.get('month','')
    day = request.GET.get('day','')

    tagid = request.GET.get('tagid', '')

    if year and month and day:
        all_articles = all_articles.filter(add_time__year=year,add_time__month=month,add_time__day=day)
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

    pa = Paginator(all_articles,2)
    pagenum = request.GET.get('pagenum',1)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'index.html',{
        # 'all_articles':all_articles
        'pages':pages,
        'click_sort':click_sort,
        'pro_arts':pro_arts,
        'all_tags':all_tags,
        'tagid':tagid,
        'date_time':date_time,
        'year':year,
        'month':month,
        'day':day
    })

def user_register(request):
    if request.method == 'GET':
        return render(request,'reg.html')
    else:
        #实例化form类，用来验证用户提交的数据
       user_register_form =  UserRegisterForm(request.POST)
        #一个判断方法：判断这个form验证是否通过（合法）,如果合法返回True，不合法返回False
       if user_register_form.is_valid():
           #如果验证合法，那么会把合法的干净的数据存储在form对象的一个属性cleaned_data
           #当中，这个属性是一个字典,我们可以这样去拿干净的数据
           username = user_register_form.cleaned_data['username']
           email = user_register_form.cleaned_data['email']
           url = user_register_form.cleaned_data['url']
           password = user_register_form.cleaned_data['password']
           password1 = user_register_form.cleaned_data['password1']

           user = UserProfile.objects.filter(username=username)
           if user:
               return render(request,'reg.html',{
                   'msg':'帐号已经存在'
               })
           else:
               if password == password1:
                   a = UserProfile()
                   a.username =username
                   a.email = email
                   a.url = url
                   a.password = password
                   a.set_password(password)
                   a.save()
                   return redirect(reverse('users:user_login'))
               else:
                   return render(request, 'reg.html', {
                       'msg': '密码不一致'
                   })
       else:
           return render(request, 'reg.html', {
                       'user_register_form': user_register_form
                   })


def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        user_login_form = UserloginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username = username,password = password)
            if user:
                login(request,user)
                return redirect(reverse('index'))
            else:
                return render(request,'login.html',{
                    'msg':'用户名或者密码错误'
                })
        else:
            return render(request, 'login.html', {
                'user_login_form': user_login_form
            })

def user_logout(request):
    logout(request)
    return redirect(reverse('index'))