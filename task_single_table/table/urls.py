from django.urls import path, include
from .views import TableListView


urlpatterns = [
    path('', view=TableListView.as_view(), name='tablePage'),
]