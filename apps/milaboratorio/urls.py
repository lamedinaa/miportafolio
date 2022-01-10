from django.conf.urls import url
from apps.milaboratorio.views import challenges, soluciones


urlpatterns = [
    url(r'^programmingchallenges$',challenges),
    url(r'soluciones/(?P<id_problem>\d+)',soluciones)
]
