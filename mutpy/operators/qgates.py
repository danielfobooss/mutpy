import ast

from mutpy.operators.base import MutationResign, MutationOperator
     
class QuantumGateReplacement(MutationOperator):
    def should_mutate(self, node):
        with open('results1.txt', 'a') as f:
                f.write("mutating")
        return ast.Call

    def mutate_FunctionDef(self, node):
        with open('results2.txt', 'a') as f:
                f.write("mutating")
                f.write(node.name)
        if node.name == "h":
            with open('results2.txt', 'a') as f:
                f.write(node.name)
            return node
        raise MutationResign()      
    