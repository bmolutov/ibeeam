from django.urls import path

from posts import views


urlpatterns = [
    path('create/', views.PostViewSet.as_view({'post': 'create'})),
    path('list/', views.PostViewSet.as_view({'get': 'list'})),
    path('update/', views.PostViewSet.as_view({'put': 'update'})),
    path('delete/', views.PostViewSet.as_view({'delete': 'destroy'}))
]
