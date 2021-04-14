from django.urls import path
from myapp import views


urlpatterns = [
    path("app1/",views.index, name="app1"),
    path('app2/',views.if_loop,name='app2'),
    path('app3/',views.for_loop,name='app3'),
]
