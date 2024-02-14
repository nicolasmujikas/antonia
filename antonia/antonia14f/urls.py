from django.urls import path
from .views import antonia14f, redireccionar_antonia

urlpatterns = [
    path('antonia14f/', antonia14f, name='antonia14f'),
    # Puedes cambiar 'antonia14f/' a la URL que prefieras
     path('flores/', redireccionar_antonia, name='flores'),
]