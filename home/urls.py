# defines URL patterns in Django
from django.urls import path

# 1st argument is the URL pattern; when the root URL of the app is accessed, it will match this path
# 2nd argument is the view function that will handle the HTTP request (the index function in views.py)
# 3rd argument is the name of the URL pattern; used to uniquely identify this URL pattern and can be referenced in other parts of the project

from . import views 
urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'), # if a URL matches the /about path, the about function in views.py will be executed
]