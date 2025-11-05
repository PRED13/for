# Generated from for.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,3,4,48,8,4,1,5,1,5,1,5,3,5,53,8,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,71,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,80,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,94,8,8,10,8,12,8,97,9,8,1,8,0,1,16,9,0,2,4,
        6,8,10,12,14,16,0,1,1,0,12,13,101,0,21,1,0,0,0,2,26,1,0,0,0,4,28,
        1,0,0,0,6,33,1,0,0,0,8,47,1,0,0,0,10,52,1,0,0,0,12,54,1,0,0,0,14,
        70,1,0,0,0,16,79,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,
        0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,21,1,0,0,0,24,27,3,
        4,2,0,25,27,3,6,3,0,26,24,1,0,0,0,26,25,1,0,0,0,27,3,1,0,0,0,28,
        29,5,2,0,0,29,30,5,4,0,0,30,31,3,16,8,0,31,32,5,18,0,0,32,5,1,0,
        0,0,33,34,5,1,0,0,34,35,5,14,0,0,35,36,3,8,4,0,36,37,5,18,0,0,37,
        38,3,14,7,0,38,39,5,18,0,0,39,40,3,10,5,0,40,41,5,15,0,0,41,42,5,
        16,0,0,42,43,3,0,0,0,43,44,5,17,0,0,44,7,1,0,0,0,45,48,3,12,6,0,
        46,48,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,9,1,0,0,0,49,50,5,2,
        0,0,50,53,7,0,0,0,51,53,3,12,6,0,52,49,1,0,0,0,52,51,1,0,0,0,53,
        11,1,0,0,0,54,55,5,2,0,0,55,56,5,4,0,0,56,57,3,16,8,0,57,13,1,0,
        0,0,58,59,3,16,8,0,59,60,5,5,0,0,60,61,3,16,8,0,61,71,1,0,0,0,62,
        63,3,16,8,0,63,64,5,6,0,0,64,65,3,16,8,0,65,71,1,0,0,0,66,67,3,16,
        8,0,67,68,5,7,0,0,68,69,3,16,8,0,69,71,1,0,0,0,70,58,1,0,0,0,70,
        62,1,0,0,0,70,66,1,0,0,0,71,15,1,0,0,0,72,73,6,8,-1,0,73,74,5,14,
        0,0,74,75,3,16,8,0,75,76,5,15,0,0,76,80,1,0,0,0,77,80,5,2,0,0,78,
        80,5,3,0,0,79,72,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,95,1,0,0,
        0,81,82,10,7,0,0,82,83,5,10,0,0,83,94,3,16,8,8,84,85,10,6,0,0,85,
        86,5,11,0,0,86,94,3,16,8,7,87,88,10,5,0,0,88,89,5,8,0,0,89,94,3,
        16,8,6,90,91,10,4,0,0,91,92,5,9,0,0,92,94,3,16,8,5,93,81,1,0,0,0,
        93,84,1,0,0,0,93,87,1,0,0,0,93,90,1,0,0,0,94,97,1,0,0,0,95,93,1,
        0,0,0,95,96,1,0,0,0,96,17,1,0,0,0,97,95,1,0,0,0,8,21,26,47,52,70,
        79,93,95
    ]

class forParser ( Parser ):

    grammarFileName = "for.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'for'", "<INVALID>", "<INVALID>", "'='", 
                     "'>'", "'<'", "'=='", "'+'", "'-'", "'*'", "'/'", "'++'", 
                     "'--'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "NUM", "ASIG", "MAYOR", 
                      "MENOR", "IGUAL_A", "SUMA", "RESTA", "MULT", "DIV", 
                      "INCREMENTO", "DECREMENTO", "P_ABRIR", "P_CERRAR", 
                      "LL_ABRIR", "LL_CERRAR", "PUNTO_COMA", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_cicloFor = 3
    RULE_inicializacion = 4
    RULE_paso = 5
    RULE_asignacionSimple = 6
    RULE_condicion = 7
    RULE_expresion = 8

    ruleNames =  [ "programa", "sentencia", "asignacion", "cicloFor", "inicializacion", 
                   "paso", "asignacionSimple", "condicion", "expresion" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    NUM=3
    ASIG=4
    MAYOR=5
    MENOR=6
    IGUAL_A=7
    SUMA=8
    RESTA=9
    MULT=10
    DIV=11
    INCREMENTO=12
    DECREMENTO=13
    P_ABRIR=14
    P_CERRAR=15
    LL_ABRIR=16
    LL_CERRAR=17
    PUNTO_COMA=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(forParser.SentenciaContext,i)


        def getRuleIndex(self):
            return forParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = forParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 18
                self.sentencia()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(forParser.AsignacionContext,0)


        def cicloFor(self):
            return self.getTypedRuleContext(forParser.CicloForContext,0)


        def getRuleIndex(self):
            return forParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = forParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.asignacion()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.cicloFor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(forParser.ID, 0)

        def ASIG(self):
            return self.getToken(forParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(forParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(forParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return forParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = forParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(forParser.ID)
            self.state = 29
            self.match(forParser.ASIG)
            self.state = 30
            self.expresion(0)
            self.state = 31
            self.match(forParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def P_ABRIR(self):
            return self.getToken(forParser.P_ABRIR, 0)

        def inicializacion(self):
            return self.getTypedRuleContext(forParser.InicializacionContext,0)


        def PUNTO_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(forParser.PUNTO_COMA)
            else:
                return self.getToken(forParser.PUNTO_COMA, i)

        def condicion(self):
            return self.getTypedRuleContext(forParser.CondicionContext,0)


        def paso(self):
            return self.getTypedRuleContext(forParser.PasoContext,0)


        def P_CERRAR(self):
            return self.getToken(forParser.P_CERRAR, 0)

        def LL_ABRIR(self):
            return self.getToken(forParser.LL_ABRIR, 0)

        def programa(self):
            return self.getTypedRuleContext(forParser.ProgramaContext,0)


        def LL_CERRAR(self):
            return self.getToken(forParser.LL_CERRAR, 0)

        def getRuleIndex(self):
            return forParser.RULE_cicloFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloFor" ):
                listener.enterCicloFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloFor" ):
                listener.exitCicloFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloFor" ):
                return visitor.visitCicloFor(self)
            else:
                return visitor.visitChildren(self)




    def cicloFor(self):

        localctx = forParser.CicloForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cicloFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(forParser.T__0)
            self.state = 34
            self.match(forParser.P_ABRIR)
            self.state = 35
            self.inicializacion()
            self.state = 36
            self.match(forParser.PUNTO_COMA)
            self.state = 37
            self.condicion()
            self.state = 38
            self.match(forParser.PUNTO_COMA)
            self.state = 39
            self.paso()
            self.state = 40
            self.match(forParser.P_CERRAR)
            self.state = 41
            self.match(forParser.LL_ABRIR)
            self.state = 42
            self.programa()
            self.state = 43
            self.match(forParser.LL_CERRAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacionSimple(self):
            return self.getTypedRuleContext(forParser.AsignacionSimpleContext,0)


        def getRuleIndex(self):
            return forParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = forParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inicializacion)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.asignacionSimple()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(forParser.ID, 0)

        def INCREMENTO(self):
            return self.getToken(forParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(forParser.DECREMENTO, 0)

        def asignacionSimple(self):
            return self.getTypedRuleContext(forParser.AsignacionSimpleContext,0)


        def getRuleIndex(self):
            return forParser.RULE_paso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaso" ):
                listener.enterPaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaso" ):
                listener.exitPaso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPaso" ):
                return visitor.visitPaso(self)
            else:
                return visitor.visitChildren(self)




    def paso(self):

        localctx = forParser.PasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paso)
        self._la = 0 # Token type
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(forParser.ID)
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.asignacionSimple()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionSimpleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(forParser.ID, 0)

        def ASIG(self):
            return self.getToken(forParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(forParser.ExpresionContext,0)


        def getRuleIndex(self):
            return forParser.RULE_asignacionSimple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionSimple" ):
                listener.enterAsignacionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionSimple" ):
                listener.exitAsignacionSimple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionSimple" ):
                return visitor.visitAsignacionSimple(self)
            else:
                return visitor.visitChildren(self)




    def asignacionSimple(self):

        localctx = forParser.AsignacionSimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacionSimple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(forParser.ID)
            self.state = 55
            self.match(forParser.ASIG)
            self.state = 56
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MayorQueContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def MAYOR(self):
            return self.getToken(forParser.MAYOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMayorQue" ):
                listener.enterMayorQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMayorQue" ):
                listener.exitMayorQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMayorQue" ):
                return visitor.visitMayorQue(self)
            else:
                return visitor.visitChildren(self)


    class IgualAContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def IGUAL_A(self):
            return self.getToken(forParser.IGUAL_A, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualA" ):
                listener.enterIgualA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualA" ):
                listener.exitIgualA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualA" ):
                return visitor.visitIgualA(self)
            else:
                return visitor.visitChildren(self)


    class MenorQueContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def MENOR(self):
            return self.getToken(forParser.MENOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenorQue" ):
                listener.enterMenorQue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenorQue" ):
                listener.exitMenorQue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenorQue" ):
                return visitor.visitMenorQue(self)
            else:
                return visitor.visitChildren(self)



    def condicion(self):

        localctx = forParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = forParser.MayorQueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.expresion(0)
                self.state = 59
                self.match(forParser.MAYOR)
                self.state = 60
                self.expresion(0)
                pass

            elif la_ == 2:
                localctx = forParser.MenorQueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.expresion(0)
                self.state = 63
                self.match(forParser.MENOR)
                self.state = 64
                self.expresion(0)
                pass

            elif la_ == 3:
                localctx = forParser.IgualAContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.expresion(0)
                self.state = 67
                self.match(forParser.IGUAL_A)
                self.state = 68
                self.expresion(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(forParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class SumaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def SUMA(self):
            return self.getToken(forParser.SUMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def P_ABRIR(self):
            return self.getToken(forParser.P_ABRIR, 0)
        def expresion(self):
            return self.getTypedRuleContext(forParser.ExpresionContext,0)

        def P_CERRAR(self):
            return self.getToken(forParser.P_CERRAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class DivisionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def DIV(self):
            return self.getToken(forParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def MULT(self):
            return self.getToken(forParser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacion" ):
                listener.enterMultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacion" ):
                listener.exitMultiplicacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacion" ):
                return visitor.visitMultiplicacion(self)
            else:
                return visitor.visitChildren(self)


    class IdentificadorContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(forParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(forParser.ExpresionContext,i)

        def RESTA(self):
            return self.getToken(forParser.RESTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = forParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = forParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 73
                self.match(forParser.P_ABRIR)
                self.state = 74
                self.expresion(0)
                self.state = 75
                self.match(forParser.P_CERRAR)
                pass
            elif token in [2]:
                localctx = forParser.IdentificadorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(forParser.ID)
                pass
            elif token in [3]:
                localctx = forParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(forParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = forParser.MultiplicacionContext(self, forParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 81
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 82
                        self.match(forParser.MULT)
                        self.state = 83
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = forParser.DivisionContext(self, forParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 84
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 85
                        self.match(forParser.DIV)
                        self.state = 86
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = forParser.SumaContext(self, forParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 87
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 88
                        self.match(forParser.SUMA)
                        self.state = 89
                        self.expresion(6)
                        pass

                    elif la_ == 4:
                        localctx = forParser.RestaContext(self, forParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 90
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 91
                        self.match(forParser.RESTA)
                        self.state = 92
                        self.expresion(5)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




