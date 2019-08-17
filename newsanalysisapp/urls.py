from django.conf.urls import url
from newsanalysisherokuapp import views

urlpatterns = [
     url(r'^$', views.index),
     url(r'^report.html$', views.report)
]
