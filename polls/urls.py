from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('bases', views.base, name='bases'),
    path('login', views.login, name='bases'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')

    #
    #
    # path('<int:question_id>/results/', views.results, name='results'),
    #
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]