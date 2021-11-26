from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('index', views.index, name='index'),
    path('customtag', views.CustomTemplateTag, name='customtag'),
    path('plotly_graph', views.PlotlyGraph, name='plotly_graph'),
]