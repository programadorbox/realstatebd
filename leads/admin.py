# leads/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Prospecto

# Configuración para que aparezca el campo "Rol" en el Admin
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('🏰 Rol en la Empresa', {'fields': ('rol',)}),
    )
    list_display = ('username', 'email', 'rol', 'is_staff') # Para ver el rol en la lista

# Registramos los modelos
admin.site.register(Usuario, CustomUserAdmin)

# Opcional: Registramos prospectos por si hay emergencias
@admin.register(Prospecto)
class ProspectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'presupuesto', 'estado')