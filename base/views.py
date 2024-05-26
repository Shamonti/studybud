from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Let\'s learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

# Create your views here.
def home(request):

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk): 
    room = None
    for item in rooms:
        if item['id'] == int(pk):
          room = item

    context = {'room': room}
    return render(request, 'base/room.html', context)