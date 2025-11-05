from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .interpretar import ejecutar_interprete # Importación relativa
import json

# Vista principal (GET)
def interprete_view(request):
    """Carga la plantilla HTML inicial."""
    # Código de ejemplo para cargar el textarea por defecto
    codigo_ejemplo = "i = 0;\nx = 1;\nfor (i = 1; i < 5; i++) {\n    x = x * 2;\n}\nfinal = x;" 
    
    context = {
        'resultado': None,
        'codigo_previo': codigo_ejemplo
    }
    return render(request, 'index.html', context)

# Vista AJAX (POST)
@csrf_exempt 
def ejecutar_codigo_ajax(request):
    """Maneja la petición JSON de ejecución y devuelve la traza."""
    if request.method == 'POST':
        try:
            # 1. Obtener el cuerpo de la petición JSON
            data = json.loads(request.body)
            codigo_usuario = data.get('codigo', '')
            
            # 2. Ejecutar el intérprete
            resultado = ejecutar_interprete(codigo_usuario)
            
            # 3. Formatear la respuesta JSON para el frontend
            if resultado["estado"] == "OK":
                return JsonResponse({
                    "success": True,
                    "trace": resultado["traza"], # Traza
                    "final_variables": resultado["memoria"] # Resultado final
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": resultado["mensaje"]
                })
                
        except Exception as e:
            return JsonResponse({"success": False, "error": f"Error interno del servidor: {str(e)}"}, status=500)
    
    return JsonResponse({"success": False, "error": "Método no permitido."}, status=404)