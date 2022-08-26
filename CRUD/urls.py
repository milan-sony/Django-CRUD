from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('viewlist/', views.viewlist),
    path('valueinsert',views.valueinsert, name='valueinsert'),
]