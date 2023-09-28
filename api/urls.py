from django.urls import path
from .views import main, RoomView, CreateRoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    path('hi', main),
    path('create-room', CreateRoomView.as_view())
]
