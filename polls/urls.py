from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    #path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('videokart/', views.videokart, name='videokart'),
    path('videokart/<int:question_id>/', views.videokart_detail, name='videokart_detail'),
    path('videokart/<int:question_id>/edit', views.videokart_edit, name='videokart_edit'),
    path('videokart/add', views.videokart_add, name='videokart_add'),
    path('gpu/', views.gpu, name='gpu'),
    path('gpu/<int:question_id>/', views.gpu_detail, name='gpu_detail'),
    path('gpu/<int:question_id>/edit', views.gpu_edit, name='gpu_edit'),
    path('gpu/add', views.gpu_add, name='gpu_add'),
    path('manufacturer/', views.manufacturer, name='manufacturer'),
    path('manufacturer/<int:question_id>/', views.manufacturer_detail, name='manufacturer_detail'),
    path('manufacturer/<int:question_id>/edit', views.manufacturer_edit, name='manufacturer_edit'),
    path('manufacturer/add', views.manufacturer_add, name='manufacturer_add'),
]