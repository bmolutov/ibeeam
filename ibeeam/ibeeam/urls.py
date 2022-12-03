"""ibeeam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

import custom_auth.views
from main.admin import ibeeam_site


swagger_urls = [
    # YOUR PATTERNS
    path('main/api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('main/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('main/api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),

    # path('main/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('main/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('main/login/', custom_auth.views.LoginViewSet.as_view({'post': 'login'})),

    path('main/ibeeam_admin/', ibeeam_site.urls),

    path('main/', include('main.urls')),
    path('main/integration/', include('custom_auth.urls')),
    path('main/comments/', include('comments.urls')),
    path('main/posts/', include('posts.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += swagger_urls


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('main/__debug__/', include('debug_toolbar.urls')),]
