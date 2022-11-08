from django.urls import path

from main import views

urlpatterns = [
    path('send_feedback_by_user/', views.FeedbackViewSet.as_view({'post': 'send_feedback_by_user'})),
    path('send_feedback_by_anon/', views.FeedbackViewSet.as_view({'post': 'send_feedback_by_anon'}))
]
