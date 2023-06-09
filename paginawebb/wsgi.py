"""
WSGI config for paginawebb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginawebb.settings')

application = get_wsgi_application()

#control de usuario y contraseña
#nose si estara vien 
def iniciar_sesion (request):
    usuario = request.POST 'USUARIO'
    control = request.POST 'contral'
    try:
        user = user.objects.get(username = usuario)
    except user.DoesNotExist:
        messages.error(request,'El usuario o contraseña son incorrectos')
        return redirect ('about')
        

pass_valida = check_password(contral, user.password)
if not pass_valida:
    messages.error(request.get,'El usuario o la contraseña son incorrectos')
    return redirect ('about')
    user = authenticate(usuario, password=contral)
    return redirect ('formulario tienda')
    return render(request, 'inicio/about.html',contexto)