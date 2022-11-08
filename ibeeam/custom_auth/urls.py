from django.urls import path

from custom_auth import views


urlpatterns = [
    path('register/', views.RegisterViewSet.as_view({'post': 'create'}))
]