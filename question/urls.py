from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.check_results, name='results')
]
