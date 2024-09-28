from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/menus/', include('menu.urls')),
    path('api/employees/', include('employee.urls')),
    path('api/restaurants/', include('restaurant.urls')),
    path('api/votes/', include('vote.urls')),
]