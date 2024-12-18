# Generated from Expressoes.g4 by ANTLR 4.13.2
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
        4,1,6,22,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,9,8,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,0,1,0,1,0,0,0,23,0,8,1,
        0,0,0,2,3,6,0,-1,0,3,4,5,4,0,0,4,5,3,0,0,0,5,6,5,5,0,0,6,9,1,0,0,
        0,7,9,5,1,0,0,8,2,1,0,0,0,8,7,1,0,0,0,9,18,1,0,0,0,10,11,10,4,0,
        0,11,12,5,2,0,0,12,17,3,0,0,5,13,14,10,3,0,0,14,15,5,3,0,0,15,17,
        3,0,0,4,16,10,1,0,0,0,16,13,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,
        18,19,1,0,0,0,19,1,1,0,0,0,20,18,1,0,0,0,3,8,16,18
    ]

class ExpressoesParser ( Parser ):

    grammarFileName = "Expressoes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'S'", "'P'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "S", "P", "LPAREN", "RPAREN", 
                      "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    NUMBER=1
    S=2
    P=3
    LPAREN=4
    RPAREN=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressoesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesizedExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressoesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExpressoesParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExpressoesParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExpressoesParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressoesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ExpressoesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)


    class ParallelOperationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressoesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressoesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpressoesParser.ExprContext,i)

        def P(self):
            return self.getToken(ExpressoesParser.P, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelOperation" ):
                listener.enterParallelOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelOperation" ):
                listener.exitParallelOperation(self)


    class SeriesOperationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressoesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressoesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpressoesParser.ExprContext,i)

        def S(self):
            return self.getToken(ExpressoesParser.S, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeriesOperation" ):
                listener.enterSeriesOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeriesOperation" ):
                listener.exitSeriesOperation(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressoesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = ExpressoesParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(ExpressoesParser.LPAREN)
                self.state = 4
                self.expr(0)
                self.state = 5
                self.match(ExpressoesParser.RPAREN)
                pass
            elif token in [1]:
                localctx = ExpressoesParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(ExpressoesParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 16
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExpressoesParser.SeriesOperationContext(self, ExpressoesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 10
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 11
                        self.match(ExpressoesParser.S)
                        self.state = 12
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ExpressoesParser.ParallelOperationContext(self, ExpressoesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 13
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 14
                        self.match(ExpressoesParser.P)
                        self.state = 15
                        self.expr(4)
                        pass

             
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




