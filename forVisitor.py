# forVisitor.py: Implementación del Intérprete con Registro de Traza

from forParser import forParser
from forBaseVisitor import forBaseVisitor

class forVisitor(forBaseVisitor):
    def __init__(self):
        self.memoria = {} 
        self.trace = [] # <-- AÑADIDO: Lista para almacenar cada paso de ejecución

    def _registrar_paso(self, ctx, descripcion):
        """Función auxiliar para añadir un paso a la traza."""
        self.trace.append({
            "line": ctx.start.line,
            "description": descripcion,
            "state": self.memoria.copy() # Usar .copy() para capturar el estado en ese momento
        })

    # --- 1. Control y Asignación ---
    
    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None 

    def visitAsignacion(self, ctx):
        valor = self.visit(ctx.expresion())
        nombre_variable = ctx.ID().getText()
        self.memoria[nombre_variable] = valor
        
        self._registrar_paso(ctx, f"Asigna {valor} a la variable '{nombre_variable}'.")
        return valor

    def visitAsignacionSimple(self, ctx):
        valor = self.visit(ctx.expresion())
        nombre_variable = ctx.ID().getText()
        self.memoria[nombre_variable] = valor
        
        self._registrar_paso(ctx, f"Reasigna {valor} a la variable '{nombre_variable}'.")
        return valor
    
    # --- 2. Bucle FOR ---

    def visitCicloFor(self, ctx):
        self.visit(ctx.inicializacion())
        
        while True:
            condicion_resultado = self.visit(ctx.condicion())
            
            # Registro de Condición (antes de entrar o salir)
            descripcion_cond = f"Evalúa la condición: ({ctx.condicion().getText()}). Resultado: {'True' if condicion_resultado else 'False'}."
            self._registrar_paso(ctx.condicion(), descripcion_cond)
            
            if not condicion_resultado:
                break
                
            self.visit(ctx.programa())
            self.visit(ctx.paso())
        
        return None

    def visitPaso(self, ctx):
        # ... (Lógica de visitPaso omitida por brevedad, asume que registra el paso internamente)
        # Aquí también deberías llamar a _registrar_paso() después de la modificación de la variable.
        # Por ejemplo: self._registrar_paso(ctx, f"Incrementa la variable '{nombre_variable}'.")
        
        try:
            nombre_variable = ctx.ID().getText()
        except AttributeError:
            return self.visit(ctx.asignacionSimple())

        if nombre_variable not in self.memoria:
             raise Exception(f"Error: Variable '{nombre_variable}' no inicializada.")
             
        if ctx.INCREMENTO():
            self.memoria[nombre_variable] += 1
            self._registrar_paso(ctx, f"Incrementa '{nombre_variable}' a {self.memoria[nombre_variable]}.")
        elif ctx.DECREMENTO():
            self.memoria[nombre_variable] -= 1
            self._registrar_paso(ctx, f"Decrementa '{nombre_variable}' a {self.memoria[nombre_variable]}.")

        return None
        
    # --- 3 & 4. Condicionales y Aritméticas (Sin Registro de Traza Detallada) ---
    # *NOTA: Para una traza aún más detallada, agregar registro a todas las operaciones.*

    def visitMayorQue(self, ctx): return self.visit(ctx.expresion(0)) > self.visit(ctx.expresion(1))
    def visitMenorQue(self, ctx): return self.visit(ctx.expresion(0)) < self.visit(ctx.expresion(1))
    def visitIgualA(self, ctx): return self.visit(ctx.expresion(0)) == self.visit(ctx.expresion(1))
    def visitMultiplicacion(self, ctx): return self.visit(ctx.expresion(0)) * self.visit(ctx.expresion(1))
    def visitDivision(self, ctx): return self.visit(ctx.expresion(0)) // self.visit(ctx.expresion(1))
    def visitSuma(self, ctx): return self.visit(ctx.expresion(0)) + self.visit(ctx.expresion(1))
    def visitResta(self, ctx): return self.visit(ctx.expresion(0)) - self.visit(ctx.expresion(1))
    def visitParentesis(self, ctx): return self.visit(ctx.expresion())

    def visitIdentificador(self, ctx):
        nombre_variable = ctx.ID().getText()
        if nombre_variable in self.memoria:
            return self.memoria[nombre_variable]
        else:
            raise Exception(f"Error de ejecución: Variable '{nombre_variable}' no definida.")

    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())