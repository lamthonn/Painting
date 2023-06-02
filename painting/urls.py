from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.upload_painting, name='upload'),
    path('', views.home,name='home'),
    path('explore/', views.painting_list,name='list'),
    path('detail/<int:pk>/',views.painting_detail,name='detail'),
    path('search/',views.painting_search,name='search'),
    path('blog/',views.blog,name='blog')
]
