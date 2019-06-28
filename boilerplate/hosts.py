from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'help', 'help.urls', name='help'),
    host(r'blog', 'blog.urls', name='blog'),
)
