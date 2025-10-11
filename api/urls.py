from django.urls import path
from .views import TaskView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
    path("auth/token/verify/", TokenVerifyView.as_view()),
    path("task/", TaskView.as_view()),
    path("user/", UserView.as_view()),
    path("user/details/", UserView.as_view()),
    path("user/modify/", UserView.as_view()),

]
