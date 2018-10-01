
from django.contrib import admin
from django.urls import path

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('system/', views.system, name='system'),
    path('language/', views.language, name='language'),
    path('ide/', views.ide, name='ide'),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:number1>/<int:number2>/', views.sum, name='sum'),
    path('<str:name1>/', views.name, name='name'),
    path('<int:number1>/product/', views.timestwo, name='timestwo'),
    path('<int:number1>/loop/', views.loop, name='loop')
]