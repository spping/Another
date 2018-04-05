from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .froms import UserForm
from .models import Bloger, Blog, Gath, Comment

# Create your views here.
class blogListView(ListView):
    model = Blog
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(blogListView, self).get_context_data(**kwargs)
        return context

class blogDetialView(DetailView):
    model = Gath
    template_name = 'blog_detail.html'

    def get_object(self):
        object = super(blogDetialView, self).get_object()
        object = Blog.objects.get(tid = object.tid)
        return object

    def get_context_data(self, **kwargs):
        context = super(blogDetialView, self).get_context_data(**kwargs)
        context['Comment'] = Comment.objects.all()
        return context
class blogerDetailView(DetailView):
    model = Bloger
    template_name = 'bloger_detail.html'

def index(request):

    return render(request, 'index.html')

def registe(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            uf.save()
            return HttpResponse('registe successfuly')
    uf = UserForm()
    return render(request, 'registe.html', {'form':uf, 'action':'Registe'})

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            bloger = uf.save(commit=False)
            try:
                dbloger = Bloger.objects.get(uname=bloger.uname)
                if dbloger.upass == bloger.upass:
                    request.session['id'] = dbloger.uid
                    return HttpResponse("OK")
                else:
                    return HttpResponse(bloger.upass)
            except:
                return HttpResponse("FAILER")
        else:
            return HttpResponse("404")

    uf = UserForm()
    return render(request, 'registe.html', {'form':uf, 'action':'Login'})

def logout(request):
    request.session.pop('id')
    return HttpResponse('Logout Ok')

def pblog(request):
    if request.method == 'POST':
        blog = Blog()
        blog.content = request.POST['content']
        blog.title = request.POST['title']
        blog.uid = Bloger.objects.get(uid = request.session['id'])
        blog.date = timezone.now()
        blog.save()
        return HttpResponse("Post Successfully")
    try:
        request.session['id']
        return render(request, 'pblog.html')
    except:
        return HttpResponse('Login First')

def comment(request, **tid):
    if request.method == 'POST':
        bid = request.META['HTTP_REFERER'].split('/')[-1]
        comment = Comment()
        comment.comment = request.POST['comment']
        comment.cid = Gath.objects.get(tid = bid)
        comment.date = timezone.now()
        comment.uid = Bloger.objects.get(uid = request.session['id'])
        comment.save()
        return HttpResponse("Comment OK")
    return HttpResponse(tid['tid'])