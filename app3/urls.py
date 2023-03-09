from app3.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('narendra/',narendra,name='narendra'),
    path('vijji/',vijji,name='vijji'),
]