# realstate/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from leads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('idioma/<str:codigo>/', views.cambiar_idioma, name='cambiar_idioma'),
    
    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='leads/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Rutas de la App
    path('', views.home, name='home'),
    path('crear/', views.crear_prospecto, name='crear'),
    path('editar/<int:id>/', views.editar_prospecto, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_prospecto, name='eliminar'),
]