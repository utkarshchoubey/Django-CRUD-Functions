from django.conf.urls import url
from basic_app import views
from django.urls import path

# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    #url(r'^relative/$' , views.relative,name='relative'),
    #url(r'^other/$',views.other,name='other'),
        path('relative/' , views.relative,name='relative'),
        path('other/',views.other,name='other'),

]
