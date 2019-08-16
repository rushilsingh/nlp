from django.conf.urls import url
from newsanalysisherokuapp import views

urlpatterns = [
     url(r'^/{0,1}$', views.index)
]
