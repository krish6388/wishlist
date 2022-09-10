from unicodedata import name
from django.shortcuts import render,HttpResponse
from pilot.models import Users,Task
from tkinter import messagebox
import string


# Create your views here.
un='guest'

def register(request):
    msg=''
    # return HttpResponse('HELLO')
    if request.method=='POST':
        name=request.POST.get('name')
        mob=request.POST.get('mob')
        uname=request.POST.get('uname')
        pas=request.POST.get('pass')
        mail=request.POST.get('email')
        c = Users.objects.filter(username=uname).count()
        if c==0:
            user = Users(name=name,mob=mob,username=uname, password = pas, email=mail)
            user.save()
            return render(request, 'login.html')
        else:
            msg='User already exists!!'
        # return HttpResponse(request, 'Krish')
    return render(request, 'register.html',{'error': msg})


def login(request):
    global un
    if request.method=='POST':
        un=request.POST.get('uname')
        p=request.POST.get('pass')
        rPass = Users.objects.raw(f'SELECT * FROM pilot_Users where username="{un}"')

        if not rPass:
            messagebox.showerror("Error", "No user exist")
            return render(request, 'login.html')
        string.ascii_uppercase

        if rPass[0].password==p:
            tasks = Task.objects.filter(name=un).order_by('-status' )
            abc={'player_name': rPass[0].name, 'tasks': tasks}

            return render(request, 'index.html', context=abc)
            # return HttpResponse(request, p)
    return render(request, 'login.html')
    

def index(request):
    # return HttpResponse('Hello')
    work = Task.objects.raw('SELECT * FROM pilot_Task')
    context={'task': work[0].do}

    return render(request,'index.html',context=context)


def add_task(request):
    global un
    if request.method=='POST':
        task=request.POST.get('task')
        c = Task.objects.filter(do=task , name=un, status='Not Started').count()
        if c==0:
            Task.objects.filter(do=task , name=un, status='Complete').delete()
            t= Task(name=un, do=task, status='Not Started')
            t.save()
        tasks = Task.objects.filter(name=un).order_by('-status' )
        return render(request, 'index.html', context={'player_name':un, 'tasks': tasks, 'All': 'selected'})

    return render(request, 'index.html', context={'player_name':un})

def delete(request):
    rm= request.POST.get('rm')
    cm= request.POST.get('done')
    tasks = Task.objects.filter(name=un)
    if rm:
        if request.method=='POST':
            task=request.POST.get('do')
            Task.objects.filter(do=task , name=un).delete()
            tasks = Task.objects.filter(name=un).order_by('-status' )
            return render(request, 'index.html', context={'player_name':un, 'tasks': tasks, 'All': 'selected'})

        return render(request, 'index.html', context={'player_name':un, 'tasks': tasks, 'All': 'selected'})
    elif cm:
        if request.method=='POST':
            task=request.POST.get('do')
            Task.objects.filter(do=task , name=un).update(status='Complete')
            tasks = Task.objects.filter(name=un).order_by('-status' )
            return render(request, 'index.html', context={'player_name':un, 'tasks': tasks})
        return render(request, 'index.html', context={'player_name':un, 'tasks': tasks, 'All': 'selected'})
    

def filter_data(request):
    cond= request.POST.get('filter')
    # com= request.POST.get('Complete')
    # ns= request.POST.get('Not Started')
    # tasks = Task.objects.filter(name=un)
    if cond == 'All':
        tasks = Task.objects.filter(name=un).order_by('-status' )
    else:
        tasks = Task.objects.filter(name=un, status=cond)
    if cond == 'Not Started':
        cond='Not_Started'
    return render(request, 'index.html', context={'player_name':un, 'tasks': tasks, cond:'selected'})
