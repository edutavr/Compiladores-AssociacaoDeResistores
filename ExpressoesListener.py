# Generated from Expressoes.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressoesParser import ExpressoesParser
else:
    from ExpressoesParser import ExpressoesParser

# This class defines a complete listener for a parse tree produced by ExpressoesParser.
class ExpressoesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressoesParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:ExpressoesParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:ExpressoesParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#Number.
    def enterNumber(self, ctx:ExpressoesParser.NumberContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#Number.
    def exitNumber(self, ctx:ExpressoesParser.NumberContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#ParallelOperation.
    def enterParallelOperation(self, ctx:ExpressoesParser.ParallelOperationContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#ParallelOperation.
    def exitParallelOperation(self, ctx:ExpressoesParser.ParallelOperationContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#SeriesOperation.
    def enterSeriesOperation(self, ctx:ExpressoesParser.SeriesOperationContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#SeriesOperation.
    def exitSeriesOperation(self, ctx:ExpressoesParser.SeriesOperationContext):
        pass



del ExpressoesParser