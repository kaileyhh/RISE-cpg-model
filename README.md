# rise-project

### Direction / Purpose
Explore chaos or bifurcations

Implications - 2 modalities / states in which the system can exist

#### Specific Steps:

Model the chaotic behavior in a hindmarsh-rose neuron: analyze phase-space, bifurcations, and firing rates

Develop biologically inspired CPG circuits using the hindmarsh-rose neurons (inhibitory, excitatory, complex circuits)

Model a biological mechanism by developing an original CPG circuit

### Inhibition Code Explanation :D

The ``HRneuronseg`` object is a modified HRneuron, and contains a list ``self.connections`` of the ids (``self.id``) of the neurons that it is *inhibited* by. It is possible for a neuron to be inhibited by another neuron but not inhibit it. 

The ``add_connections()`` method allows us to add inhibitory neurons to the given ``HRneuronseg``. The rest of the functions are the normal Hindmarsh Rose functions, except for ``update_x()``, which takes is called by the ``synapseseg`` object in order to change the x to include inhibition from any connected neurons.

``synapseseg`` is defined using a list of neurons that can be potentially connected to each other, and contains a dictionary ``self.neuron_dict`` of each neuron's id for easy referencing. ``add_neuron()`` adds a neuron to synapse. ``attach_neurons()`` connects 2 neurons, where the first parameter is being inhibited by the second. The only special Hindmarsh Rose function here is ``calculate_x()``, which loops through each neuron's connections to properly inhibit the initial calculated dx by the neuron object. The function ``calculate_all()`` is just called by the forward Euler loop in ``sim.py``.

The simulation file just initiates all the objects, connects the neurons to each other, performs the forward Euler, and plots the resulting graph.