from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    #Mostrar todos os tópicos
    path('topicos/', views.topics, name='topics'),

    #Página detalhada do tópico
    path('topicos/<int:topic_id>', views.topic, name='topic')
]