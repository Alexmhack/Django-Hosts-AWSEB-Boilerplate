from django.contrib import admin
from django.urls import path, include

from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('help/', include('help.urls', namespace='help')),
]
