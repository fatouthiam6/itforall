from django.urls import path
from . import views

app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.show_exercise, name='show_exercise'),
    path('answer/<int:id>', views.correct_exercise, name='correct_exercise'),
    path('answer/<int:id>/<str:correct>', views.corrected_exercise, name='corrected_exercise')
]
