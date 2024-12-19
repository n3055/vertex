from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
    path('',views.homePage,name='home'),
    path('map/',views.map_view,name="map"),
    path('add_location/',views.add_location_view,name="alert"),
    path('c_alert/', lambda request: render(request, 'create_alert.html'), name='add_location_page'),
    path('dis/',views.Display,name="Dis-list"),
    path('register/',views.new_user,name="register")
]