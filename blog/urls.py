
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog , name='blog'),
    path('noticias', views.noticias, name='noticias'),
    path('post2',views.post2, name='post2'),
    path('id', views.id, name='id'),
    path('post/', views.post_new, name= 'post'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]