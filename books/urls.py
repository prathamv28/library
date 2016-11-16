from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns=[
    url(r'^$', views.index , name='index'),

    url(r'^register1/$', views.register1 , name='register1'),
    url(r'^login1/$', views.login1 , name='login1'),
    url(r'^add_book/$', views.add_book , name='add_book'),
    url(r'^librarian/$', views.librarian , name='librarian'),
    url(r'^edit/$', views.edit , name='edit'),

    url(r'^register2/$', views.register2 , name='register2'),
    url(r'^login2/$', views.login2 , name='login2'),
    url(r'^customer/$', views.customer , name='customer'),
    url(r'^return/$', views.return_book , name='return'),

]