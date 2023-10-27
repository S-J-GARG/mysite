from django.urls import path
from . import views

#! app_name="polls" is used for name spacing
app_name="polls"
urlpatterns=[
    
    # #url for index## /polls/index
    # path("",views.index,name="index"),
    # #urls for details of question***/polls/2/
    # path("<int:question_id>/",views.details,name="details"),
    # path("<int:question_id>/results/",views.results,name="results"),
    # path("<int:question_id>/vote/",views.vote,name="vote"),
    #TODO For writing Genric views 
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="details"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

]