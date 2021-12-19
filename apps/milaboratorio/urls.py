from django.conf.urls import url
from apps.milaboratorio.views import challenges


urlpatterns = [
    url(r'^programmingchallenges$',challenges)
]