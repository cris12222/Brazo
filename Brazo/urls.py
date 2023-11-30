from django.urls import path
from brazomove import views

urlpatterns = [
    path('', views.index, name='index'),
]
