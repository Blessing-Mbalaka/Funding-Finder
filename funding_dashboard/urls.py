from django.contrib import admin
from django.urls import path
from opportunities import views
urlpatterns = [path('',views.dashboard,name='dashboard'),path('opportunities/<int:pk>/',views.detail,name='detail'),path('admin/',admin.site.urls)]
