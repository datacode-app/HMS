from django.urls import path
from . import views
urlpatterns = [
    path("unpaid",views.get_unpaid)
]
