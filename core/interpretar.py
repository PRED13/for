import sys
from antlr4 import *
# Importaciones relativas dentro de la carpeta 'core'
from forLexer import forLexer
from forParser import forParser
from forVisitor import forVisitor 

def ejecutar_interprete(codigo_entrada):
    """
    Función que ejecuta el intérprete ANTLR con el código dado.
    Devuelve un diccionario con el estado (OK/ERROR), la memoria final y la traza de ejecución.
    """
    try:
        # 1. Preparar la entrada
        input_stream = InputStream(codigo_entrada)

        # 2. Lexer, Parser
        lexer = forLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = forParser(stream)
        
        # OBLIGATORIO: Remueve el listener de errores por defecto
        parser.removeErrorListeners()

        # 3. Análisis Sintáctico (Parse Tree)
        tree = parser.programa()
        
        # 4. Interpretación
        interprete = forVisitor()
        interprete.visit(tree)
        
        # 5. Devolver resultados (INCLUYENDO LA TRAZA)
        return {
            "estado": "OK",
            "memoria": interprete.memoria,
            "traza": interprete.trace  # <-- La lista de pasos registrados
        }
    
    except Exception as e:
        # Captura errores léxicos, sintácticos o de ejecución
        return {
            "estado": "ERROR",
            "mensaje": str(e),
            "memoria": {},
            "traza": []
        }