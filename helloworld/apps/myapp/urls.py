from django.conf.urls import url # Gives us access to the function url
from . import views # Explicitly imports views.py in the current folder

urlpatterns = [
    url(r'^$', views.index), # Uses the url method in a way that's very similar to the @app.route method in Flask
    url(r'^new$', views.index2)
]