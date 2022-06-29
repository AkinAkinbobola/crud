import re
from django.shortcuts import redirect, render
from .models import Students
from .forms import StudentsForm


# Create your views here.

def index(request):
    data = Students.objects.all()
    return render(request, 'index.html', {'data': data})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact-us.html')


def add(request):
    if request.method == 'POST' and request.FILES['photo']:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        photo = request.FILES["photo"]

        form = Students(first_name=first_name, last_name=last_name, email=email, gender=gender, phone=phone,
                        photo=photo)

        form.save()
        return redirect("/")

    return render(request, 'add.html')


def delete(request, id):
    data = Students.objects.get(id=id)
    data.delete()
    return redirect("/")


def detail(request, id):
    data = Students.objects.get(id=id)
    return render(request, 'detail.html', {'data': data})


def edit(request, id):
    info = Students.objects.get(id=id)
    form = StudentsForm(instance=info)

    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES, instance=info)

        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'edit.html', {"form": form})

