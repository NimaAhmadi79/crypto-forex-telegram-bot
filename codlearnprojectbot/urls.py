from django.urls import path
from .views import handle_bot_request, poll_updates ,test

urlpatterns = [
    path('update/', handle_bot_request),
    path('poll/', poll_updates),
    path('test/', test),

]
