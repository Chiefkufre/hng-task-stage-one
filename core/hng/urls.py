

from django.urls import path
from .views import (
    user_detail
)



urlpatterns = [
    path('', user_detail, name='user_detail' ),
]