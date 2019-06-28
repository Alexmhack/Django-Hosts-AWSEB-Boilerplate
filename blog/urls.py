from django.urls import path

from .views import home_view

app_name = 'blog'

urlpatterns = [
	path('home/', home_view, name='home'),
	path('about/', home_view, name='about'),
	path('list/', home_view, name='list'),
	path('detail/', home_view, name='detail'),
	path('new/', home_view, name='new'),
]
