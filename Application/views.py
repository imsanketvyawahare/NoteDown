from django.shortcuts import render, redirect
from .models import Notes
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

@login_required()
def application(request):
    if request.method == "GET":
        logged_user = request.user
        name = logged_user.first_name
        data = Notes.objects.filter(user=logged_user)
        return render(request, 'app.html', {"data": data, "name": name})


@login_required()
def add(request):
    if request.method == "POST":
        logged_user = request.user
        t = request.POST['title']
        n = request.POST['note']
        notes = Notes()
        notes.title = t
        notes.note = n
        notes.user = logged_user
        notes.save()
        return redirect(application)


@login_required()
def delete(request, id):
    note = Notes.objects.get(id=id)
    note.delete()
    return redirect(application)


@login_required()
def update(request, id):
    if request.method == "POST":
        note = Notes.objects.get(id=id)
        title_update = request.POST['title']
        note_update = request.POST['note']
        note.title = title_update
        note.note = note_update
        note.save()
        return redirect(application)
    return redirect(application)