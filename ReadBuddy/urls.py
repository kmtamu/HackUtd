from django.conf.urls import url
from ReadBuddy import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page2/$',views.hitPage2, name='page2')
]