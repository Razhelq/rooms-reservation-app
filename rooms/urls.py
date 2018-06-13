from django.contrib import admin
from django.urls import path
from reservations.views import index, new_room, modify_room, delete_room, room, rooms, reservation, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('room/new/', new_room, name='new-room'),
    path('room/modify/<id>', modify_room, name='modify-room'),
    path('room/delete/<id>', delete_room, name='delete-room'),
    path('room/<id>', room, name='room'),
    path('', rooms, name='rooms'),
    path('reservation/<id>', reservation, name='reservation'),
    path('search/', search, name='search')
]


