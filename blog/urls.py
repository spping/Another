from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogListView.as_view(), name = 'index'),
    path('detail/<int:pk>', views.blogDetialView.as_view(), name = 'detail'),
    path('registe', views.registe, name = 'registe'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('pblog', views.pblog, name = 'pblog'),
    path('comment/<int:tid>', views.comment, name = 'comment'),
    path('home/<int:pk>', views.blogerDetailView.as_view(), name = 'home'),
]