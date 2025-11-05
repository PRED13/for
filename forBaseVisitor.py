# forBaseVisitor.py
# Código base corregido para el Visitor (Solo reglas existentes)

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

class forBaseVisitor(ParseTreeVisitor):

    def visitPrograma(self, ctx:forParser.ProgramaContext):
        return self.visitChildren(ctx)

    def visitSentencia(self, ctx:forParser.SentenciaContext):
        return self.visitChildren(ctx)

    def visitAsignacion(self, ctx:forParser.AsignacionContext):
        return self.visitChildren(ctx)

    def visitCicloFor(self, ctx:forParser.CicloForContext):
        return self.visitChildren(ctx)

    def visitInicializacion(self, ctx:forParser.InicializacionContext):
        return self.visitChildren(ctx)

    def visitPaso(self, ctx:forParser.PasoContext):
        return self.visitChildren(ctx)

    def visitAsignacionSimple(self, ctx:forParser.AsignacionSimpleContext):
        return self.visitChildren(ctx)

    # --- Etiquetas de Condición (Los métodos visit creados por las etiquetas) ---
    def visitMayorQue(self, ctx:forParser.MayorQueContext):
        return self.visitChildren(ctx)

    def visitMenorQue(self, ctx:forParser.MenorQueContext):
        return self.visitChildren(ctx)

    def visitIgualA(self, ctx:forParser.IgualAContext):
        return self.visitChildren(ctx)
    
    # --- Etiquetas de Expresión (Los métodos visit creados por las etiquetas) ---
    def visitMultiplicacion(self, ctx:forParser.MultiplicacionContext):
        return self.visitChildren(ctx)

    def visitDivision(self, ctx:forParser.DivisionContext):
        return self.visitChildren(ctx)

    def visitSuma(self, ctx:forParser.SumaContext):
        return self.visitChildren(ctx)

    def visitResta(self, ctx:forParser.RestaContext):
        return self.visitChildren(ctx)

    def visitParentesis(self, ctx:forParser.ParentesisContext):
        return self.visitChildren(ctx)

    def visitIdentificador(self, ctx:forParser.IdentificadorContext):
        return self.visitChildren(ctx)

    def visitNumero(self, ctx:forParser.NumeroContext):
        return self.visitChildren(ctx)