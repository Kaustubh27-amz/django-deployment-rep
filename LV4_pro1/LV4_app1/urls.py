from django.urls import path
from LV4_app1 import views


app_name='basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
