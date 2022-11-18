from django.urls import path

from main import views

urlpatterns = [
    path('feedback/by_user/', views.FeedbackViewSet.as_view({'post': 'send_feedback_by_user'})),
    path('feedback/by_anon/', views.FeedbackViewSet.as_view({'post': 'send_feedback_by_anon'}))
]
