import ast
from inspect import getmembers, isfunction, signature
from mutpy.operators.base import MutationResign, MutationOperator
from qiskit import QuantumCircuit
import random
# https://qiskit.org/documentation/apidoc/circuit_library.html
# https://github.com/Qiskit/qiskit-terra/blob/master/qiskit/circuit/quantumcircuit.py
# https://quantumai.google/cirq/gates     

class QuantumGateReplacement(MutationOperator):
    def should_mutate(self, node):   
        return ast.Call

    def mutate_Call(self, node):
        if isinstance(node.func, ast.Name):
            print("NAME")
            print(ast.dump(node))

        if isinstance(node.func, ast.Attribute):
            print("Attribute: ", ast.dump(node))  
            if node.func.attr in self.equivalent_gates():
                print('Mutating quantum gate: ', node.func.attr)
                equiv_gates = self.equivalent_gates()[node.func.attr]
                equiv_gates.remove(node.func.attr)
                if equiv_gates is None: return node

                new_gate = random.choice(list(equiv_gates)) 
                mutated_qgate = ast.Attribute(node.func.value, new_gate, node.func.ctx)
                print("Mutated: ", ast.dump(ast.Call(mutated_qgate, node.args, node.keywords)))
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
    
        