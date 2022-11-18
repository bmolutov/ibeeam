from django.urls import path

from posts import views


urlpatterns = [
    path('create/', views.PostViewSet.as_view({'post': 'create'})),
    path('list/', views.PostViewSet.as_view({'get': 'list'})),
    path('edit/<int:id>', views.PostViewSet.as_view({'put': 'edit'})),
    path('delete/<int:id>', views.PostViewSet.as_view({'delete': 'delete'})),

    path('like/', views.PostViewSet.as_view({'post': 'like'}))
]
