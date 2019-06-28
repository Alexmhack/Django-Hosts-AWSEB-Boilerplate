from django.urls import path

from .views import home_view

app_name = 'blog'

urlpatterns = [
	path('home/', home_view, name='home'),
]
