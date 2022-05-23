from django.urls import path
from myapp.views import DemoDetailView, DemoListView

app_name = "myapp"

urlpatterns = [
    path('',DemoListView.as_view(), name='list-demo'),
    path('<int:pk>/',DemoDetailView.as_view(), name='detail-demo')
]