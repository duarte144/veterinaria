from django.shortcuts import render
from .models import Propietario, Mascota, ConsultaMedica
from django.shortcuts import  redirect
from .forms import PropietarioForm
from .forms import MascotaForm, ConsultaMedicaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404




# Create your views here.

def inicio(request):
    return render(request, 'historialApp/inicio.html')

def lista_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'historialApp/propietarios.html', {'propietarios': propietarios})


def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'historialApp/mascotas.html', {'mascotas': mascotas})

def lista_consultas(request):
    consultas = ConsultaMedica.objects.all()
    return render(request, 'historialApp/consultas.html', {'consultas': consultas})


def crear_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'historialApp/crear_propietario.html', {'form': form})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'historialApp/crear_mascota.html', {'form': form})


def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaMedicaForm()
    return render(request, 'historialApp/crear_consulta.html', {'form': form})


@login_required
def historial_veterinario(request):
    # Código para mostrar el historial
    pass

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Aquí 'login' es el nombre de la URL de tu login


def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, pk=id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'historialApp/form_mascota.html', {'form': form})

def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, pk=id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('lista_mascotas')
    return render(request, 'historialApp/confirmar_eliminacion.html', {'mascota': mascota})

def editar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'historialApp/form_propietario.html', {'form': form, 'accion': 'Editar'})

def eliminar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        propietario.delete()
        return redirect('lista_propietarios')
    return render(request, 'historialApp/confirmar_eliminacion.html', {'objeto': propietario, 'tipo': 'propietario'})



def editar_consulta(request, id):
    consulta = get_object_or_404(ConsultaMedica, id=id)
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaMedicaForm(instance=consulta)
    return render(request, 'historialApp/crear_editar_consulta.html', {'form': form, 'accion': 'Editar'})

def eliminar_consulta(request, id):
    consulta = get_object_or_404(ConsultaMedica, id=id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('lista_consultas')
    return render(request, 'historialApp/eliminar_consulta.html', {'consulta': consulta})
