from django.shortcuts import render, redirect
from .models import tareas
from .forms import tareaForm

def home(request):
    tarea = tareas.objects.all()
    context = {'tarea': tarea}
    return render(request, 'crud/index.html', context)

def agregar(request):
    if request.method == "POST":
        form = tareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = tareaForm()

    conext = {'form': form}
    return render(request, 'crud/agregar.html', conext)

def eliminar(request, id_t):
    tarea = tareas.objects.get(id=id_t)
    tarea.delete()
    return redirect("home")

def editar(request, id_t):
    tarea = tareas.objects.get(id=id_t)
    if request.method == "POST":
        form = tareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = tareaForm(instance=tarea)

    context = {'form': form}
    return render(request, "crud/editar.html", context)