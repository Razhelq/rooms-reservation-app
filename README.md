# rooms-reservation-app

Rooms Reservation django based web application.

This application was created to manage rooms in an office building. 
It allows to create new rooms and book them if they are available.
I also added a search function, which look for a room based on room's name, minimum capacity, date and projector presence.
I used classes instead of functions in views.

The application contains:
1. Models:
    - Room
    - Reservation with one to many relation to Room model as there can be many reservation for a particular room in different days.
2. Classes:
    - to create, modify, delete a room
    - to display one or all rooms
    - to book a room if it is available
    - to search for a room
3. Separated html templates for every action.
4. Cooperation with PostgreSQL database.
5. Separated file for local settings.


For the front-end side I used basic bootstrap css theme to have a top menu and the container below. 
In the future I will improve this part.
