from django.urls import path, include
from . import views
from .views import greetings


urlpatterns = [
    path('', views.list_item, name='list_item'),
    path('<int:item_id>/', views.detail_item, name='detail_item'),
    path('greetings/', greetings),
]