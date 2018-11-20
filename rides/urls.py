from django.urls import path
from .views import RideView

app_name = "rides"

urlpatterns = [
    path('rides/', RideView.as_view()),
    path('rides/<int:pk>', RideView.as_view())
]
