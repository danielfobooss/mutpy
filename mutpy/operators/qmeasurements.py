import ast
from inspect import getmembers, isfunction, signature
from mutpy.operators.base import MutationResign, MutationOperator
from qiskit import QuantumCircuit

class QuantumMeasurementDeletion(MutationOperator):

    def should_mutate_Attribute(self, node):
        return isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute) and node.value.func.attr == "measure"

    def should_mutate_Name(self, node):
        return isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "measure"

    def mutate_Expr(self, node):
        if self.should_mutate_Name(node):
            return ast.Pass()
        if self.should_mutate_Attribute(node):
            return ast.Pass()
        raise MutationResign()

class QuantumMeasurementInsertion(MutationOperator):

    def should_mutate_Attribute(self, node):
        return isinstance(node.func, ast.Attribute) and node.func.attr in gates_set

    def mutate_Call(self, node):

        global gates_set 
        gates_set = self.equivalent_gates()

        if self.should_mutate_Attribute(node):

            new_node = ast.Call(
                func=ast.Name(
                    id='my_func', ctx=ast.Load()), 
                    args=[node.func.value,
                        node.args[0]],
                    keywords=[])

            self.append_new_func(node)

            return new_node

        raise MutationResign()

    def append_new_func(self, node):

        function = ast.FunctionDef(
            name='my_func',
            args=ast.arguments(
                args=[
                    ast.arg( arg='circ', annotation=None),
                    ast.arg(arg='qubit', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr='x',
                            ctx=ast.Load(),
                        ),
                        args=[ast.Name(id='qubit', ctx=ast.Load())],
                        keywords=[],
                    ),
                ),
                ast.Assign(
                    targets=[ast.Name(id='measur_cr', ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='ClassicalRegister', ctx=ast.Load()),
                        args=[
                            ast.Attribute(
                                value=ast.Name(id='circ', ctx=ast.Load()),
                                attr='num_qubits',
                                ctx=ast.Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr='add_register',
                            ctx=ast.Load(),
                        ),
                        args=[ast.Name(id='measur_cr', ctx=ast.Load())],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr='measure',
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='qubit', ctx=ast.Load()),
                            ast.Name(id='measur_cr', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        )

        ast.fix_missing_locations(function)

        while hasattr(node, 'parent') and node.parent is not None:
            node = node.parent

        node.body.append(function)

    def compare_gate_functions(self, f1, f2, discard_named_args=True):
        if not discard_named_args:
            return signature(f1) == signature(f2)
        return len([arg for arg in signature(f1).parameters.values() if arg.default is arg.empty]) == \
            len([arg for arg in signature(f2).parameters.values() if arg.default is arg.empty])

    def equivalent_gates(self, discard_named_args=True):
        existing_gate_names = ['ch', 'cp', 'cx', 'cy', 'cz', 'crx', 'cry', 'crz', 'ccx', 'cswap',
                                'csx', 'cu', 'cu1', 'cu3', 'dcx', 'h', 'i', 'id', 'iden', 'iswap',
                                'ms', 'p', 'r', 'rx', 'rxx', 'ry', 'ryy', 'rz', 'rzx', 'rzz', 's',
                                'sdg', 'swap', 'sx', 'x', 'y', 'z', 't', 'tdg', 'u', 'u1', 'u2',
                                'u3']
        gate_functions = [o for o in getmembers(QuantumCircuit) if isfunction(o[1]) and o[0] in existing_gate_names]
        gate_to_gate = { g: set() for g in existing_gate_names }
        done = set()
        for gate, func in gate_functions:
            for gate_, func_ in gate_functions:
                if gate == gate_:
                    continue
                if self.compare_gate_functions(func, func_, discard_named_args):
                    gate_to_gate[gate].add(gate_)
                    gate_to_gate[gate_].add(gate_)
                    done.add(gate)
                    done.add(gate_)
        return gate_to_gate
