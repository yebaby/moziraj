from django.urls import path
from . import  views
app_name='blogs'
urlpatterns=[
    path('',views.index,name='index'),
    path('postlist/',views.postlist,name='post_list'),
    #path('postdetail/<slug:ps>/<int:pk/',.view.postdetail,name='post_detail'),
    path('postdetail/<slug:post>/<int:pk>/',views.postdetail,name='post_detail'),
]
