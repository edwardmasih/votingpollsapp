# admin-created

from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='indexLanding'),
    # path('add_question', views.addQuestion, name='add-question'),
    # path('add_choices', views.addChoice, name='add-choices'),
]

