## RISE Group K: 

### Repository Structure
The main files implementing the Hindmarsh-Rose (HR) Neuron Model are ``HRneuron.py`` and ``HRneuronseg.py`` and ``synapseseg.py`` for creating modular networks of HR neurons. 

The file ``HRneuron_sim.py`` implements the base HRneuron model to simulate the effect of a neuron under changes in injected current and stimulation, and produce matplotlib figures. 

``sim.py`` is the general simulation file for the modular HR neuron system. 

The file ``firing_rate.py`` uses the HRneuron model and allows us to analyze the chaotic / aperiodic region. 

``bifurcation.py`` allows us to produce bifurcation graphs relating firing rate with ISIs (interspike intervals). 

``poincare_data_gen.py`` creates poincare sections of the membrane potential-ion transport rate phase portrait in relevance to injected current. 

``phase_change_plotting.py`` uses a `.npy` file generated using ``sim.py`` to plot the neuron's spiking phase change resulting from a 2ms stimulation.

All interesting result images can be viewed in ``/images``.
