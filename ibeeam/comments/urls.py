from django.urls import path

from comments import views


urlpatterns = [
    path('create/', views.PostCommentViewSet.as_view({'post': 'create'})),
    path('list/', views.PostCommentViewSet.as_view({'get': 'list'})),
    path('change/', views.PostCommentViewSet.as_view({'put': 'update'})),
    path('delete/', views.PostCommentViewSet.as_view({'delete': 'destroy'}))
]