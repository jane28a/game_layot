from django.urls import path

from . import views

urlpatterns = [
    path('<str:game_id>/', views.game_view, name='index'),
]