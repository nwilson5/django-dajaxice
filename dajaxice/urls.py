# try:
#     from django.conf.urls import patterns, url
# except ImportError:
#     from django.conf.urls.defaults import patterns, url
try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from .views import DajaxiceRequest

# urlpatterns = patterns('dajaxice.views',
#     url(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
#     url(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
# )
urlpatterns = [
    url(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
    url(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
]
