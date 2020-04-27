from django.conf.urls import url
from first import views


urlpatterns = [
    url('',views.index,name='index'),
]
