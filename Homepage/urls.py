from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home,name="index"),
    url(r'^Investor/', views.investor,name="investor"),
    url(r'^Investor/$', views.investor,name="investor"),
    
]
