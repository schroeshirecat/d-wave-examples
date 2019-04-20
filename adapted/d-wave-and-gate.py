# Taken from documentation "Solving Problems on a D-Wave System"
# @ https://dwave-meta-doc.readthedocs.io/en/latest/overview/solving_problems.html

import dwavebinarycsp
import dwavebinarycsp.factories.constraint.gates as gates
from dimod.reference.samplers import ExactSolver
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(gates.and_gate(['x1', 'x2', 'y1']))  # add an AND gate
bqm = dwavebinarycsp.stitch(csp)

# ExactSovler() does not use QPU but runs locally
# it's good to test code locally
sampler = ExactSolver()
response = sampler.sample(bqm)    
for datum in response.data(['sample', 'energy']):
	print(datum.sample, datum.energy)

# Now execute same code on a D-Wave QPU
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(bqm, num_reads=1000)   
for datum in response.data(['sample', 'energy', 'num_occurrences']):
	print(datum.sample, datum.energy, "Occurrences: ", datum.num_occurrences)
