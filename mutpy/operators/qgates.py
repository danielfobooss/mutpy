import ast

from mutpy.operators.base import MutationResign, MutationOperator, AbstractUnaryOperatorDeletion
     
class QuantumGateReplacement(MutationOperator):
    def should_mutate(self, node):
        return ast.FunctionDef

    def mutate_FunctionDef(self, node):
        if node.name == "h":
            print("Time to mutate functiondef ", node.name)
            return node
        raise MutationResign()      
    