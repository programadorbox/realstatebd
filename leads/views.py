# leads/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Prospecto
from .forms import ProspectoForm, VendedorForm

# --- Lógica Principal ---

@login_required
def home(request):
    prospectos = Prospecto.objects.all().order_by('-fecha_ingreso')
    
    # Filtro Dinámico de Países
    paises = Prospecto.objects.values_list('pais', flat=True).distinct()

    # Aplicar Filtros URL
    pais_filtro = request.GET.get('pais')
    estado_filtro = request.GET.get('estado')

    if pais_filtro:
        prospectos = prospectos.filter(pais=pais_filtro)
    if estado_filtro:
        prospectos = prospectos.filter(estado=estado_filtro)

    context = {
        'prospectos': prospectos,
        'paises': paises,
    }
    return render(request, 'leads/home.html', context)

@login_required
def crear_prospecto(request):
    # ROL: Solo 'data_entry' crea
    if request.user.rol != 'data_entry':
        return redirect('home')

    if request.method == 'POST':
        form = ProspectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProspectoForm()
    
    return render(request, 'leads/form_prospecto.html', {'form': form, 'titulo': 'Nuevo Prospecto'})

@login_required
def editar_prospecto(request, id):
    prospecto = get_object_or_404(Prospecto, id=id)
    
    # ROL: El 'investor' no edita
    if request.user.rol == 'investor':
        return redirect('home')

    # ROL: Selección de Formulario
    if request.user.rol == 'sales':
        FormClass = VendedorForm
    else:
        FormClass = ProspectoForm # Para data_entry

    if request.method == 'POST':
        form = FormClass(request.POST, instance=prospecto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FormClass(instance=prospecto)

    return render(request, 'leads/form_prospecto.html', {
        'form': form, 
        'titulo': f'Editar {prospecto.nombre}',
        'prospecto': prospecto
    })

@login_required
def eliminar_prospecto(request, id):
    # ROL: Solo 'data_entry' borra
    if request.user.rol == 'data_entry':
        prospecto = get_object_or_404(Prospecto, id=id)
        prospecto.delete()
    return redirect('home')

# --- Lógica de Idioma (ESTO FALTABA) ---

def cambiar_idioma(request, codigo):
    # codigo será 'es' o 'en'
    if codigo in ['es', 'en']:
        request.session['lenguaje'] = codigo
    # Redirige a la página de donde vino el usuario
    return redirect(request.META.get('HTTP_REFERER', 'home'))