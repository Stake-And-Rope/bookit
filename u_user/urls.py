from django.urls import path
from u_user import views

urlpatterns = (
    path('', views.test_react_view),
)