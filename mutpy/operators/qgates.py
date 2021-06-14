import ast
from inspect import getmembers, isfunction, signature
from mutpy.operators.base import MutationResign, MutationOperator
from qiskit import QuantumCircuit
from mutpy import utils

# https://qiskit.org/documentation/apidoc/circuit_library.html
# https://github.com/Qiskit/qiskit-terra/blob/master/qiskit/circuit/quantumcircuit.py
# https://quantumai.google/cirq/gates     

class QuantumGateDeletion(MutationOperator):

    def should_mutate_Attribute(self, node):
        return isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute) and node.value.func.attr in gates_set

    def should_mutate_Name(self, node):
        return isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id in gates_set

    def mutate_Expr(self, node):

        global gates_set 
        gates_set = self.equivalent_gates()
        
        if self.should_mutate_Name(node):
            return ast.Pass()
        if self.should_mutate_Attribute(node):
            return ast.Pass()
        raise MutationResign()

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

class QuantumGateInsertion(MutationOperator):

    # if Call is Attribute, a gate and if there are equivalent gates
    def should_mutate_Attribute_equivalents(self, node):
        return isinstance(node.func, ast.Attribute) and node.func.attr in gates_set and len(gates_set[node.func.attr]) > 0
    
    def should_mutate_Attribute_no_equivalents(self, node):
        return isinstance(node.func, ast.Attribute) and node.func.attr in gates_set and len(gates_set[node.func.attr]) == 0

    def mutate_Call_0(self, node):
        # create gate set
        global gates_set 
        gates_set = self.equivalent_gates()

        if self.should_mutate_Attribute_no_equivalents(node):
            # mutates gate
            new_node = self.append_new_func(node, node.func.attr)

            return new_node

        if self.should_mutate_Attribute_equivalents(node):

            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_1(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()
    
    def mutate_Call_2(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_3(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()
    
    def mutate_Call_4(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_5(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_6(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_7(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_8(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_9(self, node):
        
        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_90(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_91(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()
    
    def mutate_Call_92(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def mutate_Call_93(self, node):

        if self.should_mutate_Attribute_equivalents(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            new_node = self.append_new_func(node, new_gate)

            return new_node
        raise MutationResign()

    def append_new_func(self, node, new_gate):

        function_1_arg = ast.FunctionDef(
                name='my_func', 
                args=ast.arguments(
                    args=[ast.arg(arg='circ', annotation=None), ast.arg(arg='qubit', annotation=None)], 
                    vararg=None, 
                    kwonlyargs=[], 
                    kw_defaults=[], 
                    kwarg=None, 
                    defaults=[]
                ),
                body=[
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(
                                    id='circ',
                                    ctx=ast.Load()
                                ), 
                                attr=node.func.attr, ctx=ast.Load()
                            ), 
                            args=[ast.Name(id='qubit', ctx=ast.Load())],
                            keywords=[]
                        )
                    ),
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(
                                    id='circ',
                                    ctx=ast.Load()
                                ), 
                                attr=new_gate, ctx=ast.Load()
                            ), 
                            args=[ast.Name(id='qubit', ctx=ast.Load())],
                            keywords=[]
                        )
                    )
                ],
                decorator_list=[], 
                returns=None)

        function_2_arg = ast.FunctionDef(
            name='my_func',
            args=ast.arguments(
                args=[
                    ast.arg(arg='circ', annotation=None),
                    ast.arg(arg='arg1', annotation=None),
                    ast.arg(arg='arg2', annotation=None),
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
                            attr=node.func.attr,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr=new_gate,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        )

        function_3_arg = ast.FunctionDef(
            name='my_func',
            args=ast.arguments(
                args=[
                    ast.arg(arg='circ', annotation=None),
                    ast.arg(arg='arg1', annotation=None),
                    ast.arg(arg='arg2', annotation=None),
                    ast.arg(arg='arg3', annotation=None),
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
                            attr=node.func.attr,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr=new_gate,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        )
        
        function_4_arg = ast.FunctionDef(
            name='my_func',
            args=ast.arguments(
                args=[
                    ast.arg(arg='circ', annotation=None),
                    ast.arg(arg='arg1', annotation=None),
                    ast.arg(arg='arg2', annotation=None),
                    ast.arg(arg='arg3', annotation=None),
                    ast.arg(arg='arg4', annotation=None),
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
                            attr=node.func.attr,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                            ast.Name(id='arg4', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr=new_gate,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                            ast.Name(id='arg4', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        )

        function_5_arg = ast.FunctionDef(
            name='my_func',
            args=ast.arguments(
                args=[
                    ast.arg(arg='circ', annotation=None),
                    ast.arg(arg='arg1', annotation=None),
                    ast.arg(arg='arg2', annotation=None),
                    ast.arg(arg='arg3', annotation=None),
                    ast.arg(arg='arg4', annotation=None),
                    ast.arg(arg='arg5', annotation=None),
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
                            attr=node.func.attr,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                            ast.Name(id='arg4', ctx=ast.Load()),
                            ast.Name(id='arg5', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr=new_gate,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                            ast.Name(id='arg4', ctx=ast.Load()),
                            ast.Name(id='arg5', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        )

        function_6_arg = ast.FunctionDef(
            name='my_func',
            args=ast.arguments(
                args=[
                    ast.arg(arg='circ', annotation=None),
                    ast.arg(arg='arg1', annotation=None),
                    ast.arg(arg='arg2', annotation=None),
                    ast.arg(arg='arg3', annotation=None),
                    ast.arg(arg='arg4', annotation=None),
                    ast.arg(arg='arg5', annotation=None),
                    ast.arg(arg='arg6', annotation=None),
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
                            attr=node.func.attr,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                            ast.Name(id='arg4', ctx=ast.Load()),
                            ast.Name(id='arg5', ctx=ast.Load()),
                            ast.Name(id='arg6', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='circ', ctx=ast.Load()),
                            attr=new_gate,
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(id='arg1', ctx=ast.Load()),
                            ast.Name(id='arg2', ctx=ast.Load()),
                            ast.Name(id='arg3', ctx=ast.Load()),
                            ast.Name(id='arg4', ctx=ast.Load()),
                            ast.Name(id='arg5', ctx=ast.Load()),
                            ast.Name(id='arg6', ctx=ast.Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        )

        copy_node = node

        while hasattr(copy_node, 'parent') and copy_node.parent is not None:
            copy_node = copy_node.parent

        if len(node.args) == 1:

            ast.fix_missing_locations(function_1_arg)
            copy_node.body.append(function_1_arg)

            new_node = ast.Call(
                    func=ast.Name(
                        id='my_func', ctx=ast.Load()), 
                        args=[
                            node.func.value,
                            node.args[0]],
                        keywords=[])

        elif len(node.args) == 2:

            ast.fix_missing_locations(function_2_arg)
            copy_node.body.append(function_2_arg)

            new_node = ast.Call(
                    func=ast.Name(
                        id='my_func', ctx=ast.Load()), 
                        args=[
                            node.func.value,
                            node.args[0],
                            node.args[1]],
                        keywords=[])

        elif len(node.args) == 3:

            ast.fix_missing_locations(function_3_arg)
            copy_node.body.append(function_3_arg)

            new_node = ast.Call(
                    func=ast.Name(
                        id='my_func', ctx=ast.Load()), 
                        args=[
                            node.func.value,
                            node.args[0],
                            node.args[1],
                            node.args[2]],
                        keywords=[])
        
        elif len(node.args) == 4:

            ast.fix_missing_locations(function_4_arg)
            copy_node.body.append(function_4_arg)

            new_node = ast.Call(
                    func=ast.Name(
                        id='my_func', ctx=ast.Load()), 
                        args=[
                            node.func.value,
                            node.args[0],
                            node.args[1],
                            node.args[2],
                            node.args[3]],
                        keywords=[])

        elif len(node.args) == 5:

            ast.fix_missing_locations(function_5_arg)
            copy_node.body.append(function_5_arg)

            new_node = ast.Call(
                    func=ast.Name(
                        id='my_func', ctx=ast.Load()), 
                        args=[
                            node.func.value,
                            node.args[0],
                            node.args[1],
                            node.args[2],
                            node.args[3],
                            node.args[4]],
                        keywords=[])

        elif len(node.args) == 6:

            ast.fix_missing_locations(function_6_arg)
            copy_node.body.append(function_6_arg)

            new_node = ast.Call(
                    func=ast.Name(
                        id='my_func', ctx=ast.Load()), 
                        args=[
                            node.func.value,
                            node.args[0],
                            node.args[1],
                            node.args[2],
                            node.args[3],
                            node.args[4],
                            node.args[5]],
                        keywords=[])

        return new_node

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
    

class QuantumGateReplacement(MutationOperator):

    # if Call is Name, a gate and if there are equivalent gates
    def should_mutate_Name(self, node):
        return isinstance(node.func, ast.Name) and node.func.id in gates_set and len(gates_set[node.func.id]) > 0

    # if Call is Attribute, a gate and if there are equivalent gates
    def should_mutate_Attribute(self, node):
        return isinstance(node.func, ast.Attribute) and node.func.attr in gates_set and len(gates_set[node.func.attr]) > 0


    def mutate_Call_0(self, node):
        # create gate set
        global gates_set 
        gates_set = self.equivalent_gates()

        if self.should_mutate_Name(node):
            # remove same gate from equivalents
            gates_set[node.func.id].remove(node.func.id)

            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # remove same gate from equivalents
            gates_set[node.func.attr].remove(node.func.attr)

            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_1(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_2(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_3(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_4(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_5(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_6(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_7(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_8(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_9(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_90(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_91(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()

    def mutate_Call_92(self, node):
        
        if self.should_mutate_Name(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.id])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.id].remove(new_gate)

            # mutates gate
            mutated_qgate = ast.Name(new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)

        if self.should_mutate_Attribute(node):
            # picks gate to mutate
            gates_list = list(gates_set[node.func.attr])
            new_gate = gates_list[0]

            # removes picked gate from equivalents
            gates_set[node.func.attr].remove(new_gate)
            
            # mutates gate
            mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
            return ast.Call(mutated_qgate, node.args, node.keywords)
        raise MutationResign()


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
    
        