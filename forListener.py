# Generated from for.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

# This class defines a complete listener for a parse tree produced by forParser.
class forListener(ParseTreeListener):

    # Enter a parse tree produced by forParser#programa.
    def enterPrograma(self, ctx:forParser.ProgramaContext):
        pass

    # Exit a parse tree produced by forParser#programa.
    def exitPrograma(self, ctx:forParser.ProgramaContext):
        pass


    # Enter a parse tree produced by forParser#sentencia.
    def enterSentencia(self, ctx:forParser.SentenciaContext):
        pass

    # Exit a parse tree produced by forParser#sentencia.
    def exitSentencia(self, ctx:forParser.SentenciaContext):
        pass


    # Enter a parse tree produced by forParser#asignacion.
    def enterAsignacion(self, ctx:forParser.AsignacionContext):
        pass

    # Exit a parse tree produced by forParser#asignacion.
    def exitAsignacion(self, ctx:forParser.AsignacionContext):
        pass


    # Enter a parse tree produced by forParser#cicloFor.
    def enterCicloFor(self, ctx:forParser.CicloForContext):
        pass

    # Exit a parse tree produced by forParser#cicloFor.
    def exitCicloFor(self, ctx:forParser.CicloForContext):
        pass


    # Enter a parse tree produced by forParser#inicializacion.
    def enterInicializacion(self, ctx:forParser.InicializacionContext):
        pass

    # Exit a parse tree produced by forParser#inicializacion.
    def exitInicializacion(self, ctx:forParser.InicializacionContext):
        pass


    # Enter a parse tree produced by forParser#paso.
    def enterPaso(self, ctx:forParser.PasoContext):
        pass

    # Exit a parse tree produced by forParser#paso.
    def exitPaso(self, ctx:forParser.PasoContext):
        pass


    # Enter a parse tree produced by forParser#asignacionSimple.
    def enterAsignacionSimple(self, ctx:forParser.AsignacionSimpleContext):
        pass

    # Exit a parse tree produced by forParser#asignacionSimple.
    def exitAsignacionSimple(self, ctx:forParser.AsignacionSimpleContext):
        pass


    # Enter a parse tree produced by forParser#MayorQue.
    def enterMayorQue(self, ctx:forParser.MayorQueContext):
        pass

    # Exit a parse tree produced by forParser#MayorQue.
    def exitMayorQue(self, ctx:forParser.MayorQueContext):
        pass


    # Enter a parse tree produced by forParser#MenorQue.
    def enterMenorQue(self, ctx:forParser.MenorQueContext):
        pass

    # Exit a parse tree produced by forParser#MenorQue.
    def exitMenorQue(self, ctx:forParser.MenorQueContext):
        pass


    # Enter a parse tree produced by forParser#IgualA.
    def enterIgualA(self, ctx:forParser.IgualAContext):
        pass

    # Exit a parse tree produced by forParser#IgualA.
    def exitIgualA(self, ctx:forParser.IgualAContext):
        pass


    # Enter a parse tree produced by forParser#Numero.
    def enterNumero(self, ctx:forParser.NumeroContext):
        pass

    # Exit a parse tree produced by forParser#Numero.
    def exitNumero(self, ctx:forParser.NumeroContext):
        pass


    # Enter a parse tree produced by forParser#Suma.
    def enterSuma(self, ctx:forParser.SumaContext):
        pass

    # Exit a parse tree produced by forParser#Suma.
    def exitSuma(self, ctx:forParser.SumaContext):
        pass


    # Enter a parse tree produced by forParser#Parentesis.
    def enterParentesis(self, ctx:forParser.ParentesisContext):
        pass

    # Exit a parse tree produced by forParser#Parentesis.
    def exitParentesis(self, ctx:forParser.ParentesisContext):
        pass


    # Enter a parse tree produced by forParser#Division.
    def enterDivision(self, ctx:forParser.DivisionContext):
        pass

    # Exit a parse tree produced by forParser#Division.
    def exitDivision(self, ctx:forParser.DivisionContext):
        pass


    # Enter a parse tree produced by forParser#Multiplicacion.
    def enterMultiplicacion(self, ctx:forParser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by forParser#Multiplicacion.
    def exitMultiplicacion(self, ctx:forParser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by forParser#Identificador.
    def enterIdentificador(self, ctx:forParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by forParser#Identificador.
    def exitIdentificador(self, ctx:forParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by forParser#Resta.
    def enterResta(self, ctx:forParser.RestaContext):
        pass

    # Exit a parse tree produced by forParser#Resta.
    def exitResta(self, ctx:forParser.RestaContext):
        pass



del forParser