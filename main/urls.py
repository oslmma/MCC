from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add-people/', views.add_people, name="add_people"),
    path('add-todo/', views.add_todo, name="add_todo"),
    path('todos-page/', views.todos_page, name="todos_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

