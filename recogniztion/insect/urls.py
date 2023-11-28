from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index.html"),
    path('page/<int:predictions>/',views.page,name="page.html"),
]