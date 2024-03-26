from qiskit import *
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt

# Create a quantum circuit
circle = QuantumCircuit(3)
circle.h(0)
circle.cx(0,1)
circle.cx(0,2)

# Draw the circuit diagram using matplotlib backend
fig, ax = plt.subplots(1, 1)
circuit_drawer(circle, ax=ax)

# Show the circuit diagram
plt.show()