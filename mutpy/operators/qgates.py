import ast
from inspect import getmembers, isfunction, signature
from mutpy.operators.base import MutationResign, MutationOperator
# https://qiskit.org/documentation/apidoc/circuit_library.html
# https://github.com/Qiskit/qiskit-terra/blob/master/qiskit/circuit/quantumcircuit.py
# https://quantumai.google/cirq/gates     


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


    def compare_gate_functions(self, f1, f2, discard_named_args=True):
        if not discard_named_args:
            return signature(f1) == signature(f2)
        return [arg for arg in signature(f1).parameters.values() if arg.default is arg.empty] == \
            [arg for arg in signature(f2).parameters.values() if arg.default is arg.empty]

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
    
        