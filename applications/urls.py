from django.urls import path
from .views import ApplicationsCreateApiView
urlpatterns = [
	path('create', ApplicationsCreateApiView.as_view())
]