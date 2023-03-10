from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('uploadImage/', uploadImage, name = 'uploadImage'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('viewImages/', viewImages, name = 'viewImages'),

]