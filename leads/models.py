from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Usuario(AbstractUser):
    # ROLES ACTUALIZADOS A INGLÉS (Standard Industry Terms)
    ROLES = (
        ('data_entry', 'Data Entry (Admin)'),  # Antes digitalizador
        ('sales', 'Sales Agent'),              # Antes vendedor
        ('investor', 'Investor'),              # Antes dueño
    )
    # Cambiamos el default a 'sales'
    rol = models.CharField(max_length=20, choices=ROLES, default='sales')

class Prospecto(models.Model):
    # Opciones de Presupuesto
    INTERES_OPCIONES = [
        ('10M', '10 Millones (Alto)'),
        ('6M', '6 Millones (Medio)'),
        ('4M', '4 Millones (Bajo)'),
    ]

    # Opciones de Estado
    ESTADO_OPCIONES = [
        ('no_contactado', '🔴 No Contactado'),
        ('pendiente', '🟡 Contactado - Pendiente'),
        ('interesado', '🟢 Contactado - Interesado'),
        ('no_interesado', '⚫ Contactado - No Interesado'),
    ]

    # Datos Personales (Solo Data Entry edita)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50, verbose_name="País")
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    # Datos de Negocio (Editables por Sales)
    presupuesto = models.CharField(max_length=3, choices=INTERES_OPCIONES, default='10M')
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='no_contactado')
    
    # Bitácora
    notas = models.TextField(blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_contacto = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Lógica automática: Si sale de 'no_contactado', guarda fecha
        if self.estado != 'no_contactado' and not self.fecha_contacto:
            self.fecha_contacto = timezone.now()
        # Si vuelve a 'no_contactado', borra fecha
        elif self.estado == 'no_contactado':
            self.fecha_contacto = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"