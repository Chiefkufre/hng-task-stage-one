

from django.urls import path
from .views import (
    user_detail,
    perform_calculation
)



urlpatterns = [
    path('', user_detail, name='user_detail' ),
    path('cal/', perform_calculation, name='perform_calculation' )
]