from django.db import DatabaseError, OperationalError
import time

class RegistrarVisitaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Excluir algunas URLs
        excluded_paths = ['/admin/', '/static/', '/media/', '/favicon.ico']
        current_path = request.path
        
        if not any(current_path.startswith(path) for path in excluded_paths):
            try:
                # Tu lógica actual aquí, pero con try/except
                from .models import Visita
                from django.utils import timezone
                from datetime import timedelta
                
                # Prevenir registro excesivo
                hace_un_minuto = timezone.now() - timedelta(minutes=1)
                
                visita_reciente = Visita.objects.filter(
                    pagina=current_path,
                    ip=request.META.get('REMOTE_ADDR'),
                    fecha__gte=hace_un_minuto
                ).exists()
                
                if not visita_reciente:
                    Visita.objects.create(
                        pagina=current_path,
                        usuario=request.user.username if request.user.is_authenticated else 'Anónimo',
                        ip=request.META.get('REMOTE_ADDR')
                    )
                    
            except (OperationalError, DatabaseError):
                # Si la tabla no existe aún, ignorar silenciosamente
                pass
            except Exception:
                # Cualquier otro error, ignorar para no romper el sitio
                pass
        
        response = self.get_response(request)
        return response
    
# from .models import Visita
# from django.utils import timezone
# from datetime import timedelta

# class RegistrarVisitaMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Excluir algunas URLs
#         excluded_paths = ['/admin/', '/static/', '/media/', '/favicon.ico']
#         current_path = request.path
        
#         if not any(current_path.startswith(path) for path in excluded_paths):
#             # Prevenir registro excesivo (máximo 1 visita por minuto por IP/página)
#             hace_un_minuto = timezone.now() - timedelta(minutes=1)
            
#             visita_reciente = Visita.objects.filter(
#                 pagina=current_path,
#                 ip=request.META.get('REMOTE_ADDR'),
#                 fecha__gte=hace_un_minuto
#             ).exists()
            
#             if not visita_reciente:
#                 Visita.objects.create(
#                     pagina=current_path,
#                     usuario=request.user.username if request.user.is_authenticated else 'Anónimo',
#                     ip=request.META.get('REMOTE_ADDR')
#                 )
        
#         response = self.get_response(request)
#         return response