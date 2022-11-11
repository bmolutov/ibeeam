from django.urls import path

from custom_auth import views


urlpatterns = [
    path('integration/create_user/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('integration/delete_user/<profile_id>', views.UserViewSet.as_view({'delete': 'delete_user'}))
]
