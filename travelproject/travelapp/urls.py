from django.urls import path
from . import views
urlpatterns = [
    path('', views.fun, name='fun'),
 #   path('', views.blog, name='blog'),

]



