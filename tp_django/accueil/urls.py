from accueil.views import *
from django.urls import path, re_path


urlpatterns = [
    path('helloWorld/', helloWorld, name="Hello World"),
    path('sum/<num1>/<num2>', sum, name="somme"),
    #re_path(r'sum/(?P<num1>\d+)/(?P<num2>\d+)$', sum, name="sum" )
]