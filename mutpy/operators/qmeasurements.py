import ast
from inspect import getmembers, isfunction, signature
from mutpy.operators.base import MutationResign, MutationOperator


class QuantumMeasurementRemove(MutationOperator):

    def mutate_