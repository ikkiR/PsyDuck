from django.urls import path
from psyPage import views

app_name = 'psyPage'

#aqui definimos a url e informamos view e template que irão ser renderizados
urlpatterns = [
    path('', views.index, name='index'),
]