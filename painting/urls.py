from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.upload_painting, name='upload'),
    path('', views.home,name='home'),
    path('explore/', views.painting_list,name='list'),
    path('detail/<int:pk>/',views.painting_detail,name='detail'),
    path('search/',views.painting_search,name='search'),
    path('blog/',views.blog,name='blog'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('admin_list/',views.admin_list,name='admin_list'),
    path('edit_pictures/<int:pk>/',views.edit_pictures,name='edit_pictures'),
    path('update_pictures/<int:pk>/',views.update_pictures,name='update_pictures'),
    path('delete_pictures/<int:pk>/',views.delete_pictures,name='delete_pictures')
]
