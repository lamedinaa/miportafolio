from django.conf.urls import url
from apps.miperfil.views import index

urlpatterns = [
    url(r'^$',index)
]