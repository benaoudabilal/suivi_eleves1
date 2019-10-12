from django.conf.urls import url
from eleve  import views

urlpatterns = [
url(r'^user/$',views.connexion,name="user"),
]