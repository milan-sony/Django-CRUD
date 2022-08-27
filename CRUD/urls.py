from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('valueinsert',views.valueinsert),
    path('viewlist/', views.viewlist),
    path('update/<int:id>',views.update),
]