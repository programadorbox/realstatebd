# leads/context_processors.py
from .idiomas import DICCIONARIO

def traductor(request):
    # Obtenemos el idioma de la sesión, por defecto 'es' (español)
    idioma_actual = request.session.get('lenguaje', 'en')
    
    # Retornamos el diccionario correspondiente y la clave actual para el botón
    return {
        'txt': DICCIONARIO[idioma_actual],
        'idioma_actual': idioma_actual
    }