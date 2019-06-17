from django.shortcuts import render
from registration.models import Registration
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.
def land_redirect(request):

    return render(request, 'index.html')

def create(request):

    return render(request, 'create.html')

def read(request):

    todos = Registration.objects.all().values()
    for todo in todos:
        if todo['status']==1:
            todo['status'] = "Pending"

        elif todo['status']==2:
            todo['status'] = "In Progress"

        else:
            todo['status'] = "Completed"

    args= {'data': todos}

    return render(request, 'read.html',args)

def update(request):

    return render(request, 'update.html')

def delete(request):

    return render(request, 'delete.html')

def save(request):
    if request.method == 'POST':
        feed = Registration()
        print(request.POST.get('status'))
        if request.POST.get('title') and request.POST.get('email') and request.POST.get('password'):

            feed.title = request.POST.get('title')
            feed.email = request.POST.get('email')
            feed.description = request.POST.get('description')
            feed.password = make_password(request.POST.get('password'))
            feed.status = request.POST.get('status')
            feed.time = request.POST.get('time')

            feed.save()

            messages.success(request, 'To-do created successfully')
            args = {'message': messages}

    return render(request, 'create.html',args)

