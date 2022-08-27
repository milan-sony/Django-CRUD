from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('valueinsert',views.valueinsert, name = 'valueinsert'),
    path('viewlist/', views.viewlist, name = 'viewlist'),
]