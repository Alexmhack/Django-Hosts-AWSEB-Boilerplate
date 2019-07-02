from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('help/', include('help.urls', namespace='help')),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
