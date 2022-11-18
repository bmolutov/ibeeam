from django.urls import path

from comments import views


urlpatterns = [
    path('leave/', views.CommentViewSet.as_view({'post': 'leave'})),
    path('list/', views.CommentViewSet.as_view({'get': 'list'})),
    path('update/<int:id>', views.CommentViewSet.as_view({'put': 'update'})),
    path('delete/<int:id>', views.CommentViewSet.as_view({'delete': 'delete'})),

    path('like/', views.CommentViewSet.as_view({'post': 'like'}))
]
