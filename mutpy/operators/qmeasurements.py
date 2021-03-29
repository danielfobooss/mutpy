import ast
from inspect import getmembers, isfunction, signature
from mutpy.operators.base import MutationResign, MutationOperator


class QuantumMeasurementRemove(MutationOperator):

    def should_mutate_Attribute(self, node):
        return isinstance(node.value.func, ast.Attribute) and node.value.func.attr == "measure"

    def should_mutate_Name(self, node):
        return isinstance(node.value.func, ast.Name) and node.value.func.id == "measure"

    def mutate_Expr(self, node):
        if self.should_mutate_Name(node):
            return None
        if self.should_mutate_Attribute(node):
            return None
        raise MutationResign()

        