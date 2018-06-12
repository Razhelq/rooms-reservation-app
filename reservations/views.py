from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Reservation
from datetime import datetime


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def new_room(request):
    if request.method == 'GET':
        return render(request, 'new_room.html')
    if request.method == 'POST':
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


def modify_room(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'modify_room.html', {
            'room': room
        })
    if request.method == 'POST':
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


def delete_room(request, id):
    room = Room.objects.get(id=id).delete()
    return render(request, 'rooms.html', {
        'deleted': 'The room has been removed'
    })


def room(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'room.html', {
        'room': room
    })


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {
        'rooms': rooms
    })


def reservation(request, id):
    room = Room.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'reservation.html', {
            'room': room
        })
    if request.method == "POST":
        date = request.POST.get('date')
        comment = request.POST.get('comment')
        if Reservation.objects.get(date=date):
            return render(request, 'reservation.html', {
                'room': room,
                'reserved': 'This room is already booked'
            })
        if date < datetime.now():
            return render(request, 'reservation.html', {
                'room': room,
                'reserved': 'Wrong date'
            })
        r = Reservation(
            date=date,
            comment=comment,
            room=room
        )
        r.save()
        return redirect('index/')
