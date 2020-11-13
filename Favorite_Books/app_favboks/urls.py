from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('<int:num>', views.showBook),
    path('<int:num>/favorite', views.favorite),
    path('<int:num>/unfavorite', views.unfavorite),
    path('<int:num>/delete', views.delete),
    path('add', views.add),
    path('<int:num>/edit', views.edit),
]