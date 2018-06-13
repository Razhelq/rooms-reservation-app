from django.contrib import admin
from django.urls import path
from reservations.views import Index, NewRoom, ModifyRoom, DeleteRoom, RoomView, Rooms, ReservationView, Search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', Index.as_view(), name='index'),
    path('room/new', NewRoom.as_view(), name='new-room'),
    path('room/modify/<id>', ModifyRoom.as_view(), name='modify-room'),
    path('room/delete/<id>', DeleteRoom.as_view(), name='delete-room'),
    path('room/<id>', RoomView.as_view(), name='room'),
    path('', Rooms.as_view(), name='rooms'),
    path('reservation/<id>', ReservationView.as_view(), name='reservation'),
    path('search/', Search.as_view(), name='search')
]


