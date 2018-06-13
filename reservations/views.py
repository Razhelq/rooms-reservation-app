from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Reservation
from datetime import datetime


class Index(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'index.html', {
            'rooms': rooms
        })


class NewRoom(View):
    def get(self, request):
        return render(request, 'new_room.html')

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')
        if projector == "yes":
            projector = True
        elif projector == "no":
            projector = False
        if name and capacity and projector:
            r = Room(
                name=name,
                capacity=capacity,
                projector_availability=projector
            )
            r.save()
        return render(request, 'new_room.html', {
            'added': 'Room has been added'
        })


class ModifyRoom(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'modify_room.html', {
            'room': room
        })

    def post(self, request, id):
        room = Room.objects.get(id=id)
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')
        if projector == "yes":
            projector = True
        elif projector == "no":
            projector = False
        if name and capacity and projector:
            room.name = name
            room.capacity = capacity
            room.projector_availability = project
            room.save()
        return render(request, 'modify_room.html', {
            'room': room,
            'added': 'Room has been modified'
        })


class DeleteRoom(View):
    def get(self, request, id):
        room = Room.objects.get(id=id).delete()
        return render(request, 'rooms.html', {
            'deleted': 'The room has been removed'
        })


class RoomView(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'room.html', {
            'room': room
        })


class Rooms(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'rooms.html', {
            'rooms': rooms
        })


class ReservationView(View):
    def post(self, request, id):
        room = Room.objects.get(id=id)
        date = request.POST.get('date')
        comment = request.POST.get('comment')
        if Reservation.objects.filter(rooms=room).filter(date=date):
            return render(request, 'reservation.html', {
                'room': room,
                'response': 'This room is already booked'
            })
        elif date < str(datetime.now()):
            return render(request, 'reservation.html', {
                'room': room,
                'response': 'Wrong date'
            })
        else:
            r = Reservation(
                date=date,
                comment=comment,
                rooms=room
            )
            r.save()
            return redirect('../index')


class Search(View):
    def get(self, request):
        name = request.GET.get('name')
        date = request.GET.get('date')
        capacity = request.GET.get('capacity')
        projector = request.GET.get('projector')
        rooms = Room.objects.all()
        if name:
            rooms = rooms.filter(name=name)
        if date:
            rooms = rooms.exclude(reservation__date=date)
        if capacity:
            rooms = rooms.filter(capacity__gte=capacity)
        if projector:
            rooms = rooms.filter(projector_availability=projector)
        if rooms:
            return render(request, 'search.html', {
                'rooms': rooms
            })
        else:
            return render(request, 'search.html', {
                'empty': 'There are no rooms available for the given search criteria'
            })
