from django.urls import path
from .views import *

urlpatterns=[
    path("hv/",hview),
    path("cv/",carview),
    path("sv/",sview),
    path("uv/<int:pk>/",upview),
    path("dv/<int:x>/",dview)
]