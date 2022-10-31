

from django.urls import path
from .views import (
    user_detail,
    User_views
)



urlpatterns = [
    path('', user_detail, name='user_detail' ),
    path('new/', User_views.as_view(), name='user_views'),
]