## RISE Group K: Modeling Nonlinear Dynamics of the Mammalian Respiratory Central Pattern Generator Using the Hindmarsh-Rose Neuron
Adarsh Ambekar, Krish Asija, Kailey Hua, Ishan Kar, Richard Zhang

### Abstract
The human body supports a variety of rhythmic behaviors which can autonomically sustain themselves (breathing, heartbeats, walking, etc.) through neural networks known as Central Pattern Generators (CPGs). Through a complex series of physiological interactions, these networks fire impulses at different rates to produce different modalities of behavior (e.g. walking vs running). We implement a series of differential equations using Python to simulate a modular network of inhibitory neurons based on the Hindmarsh-Rose (HR) model. Two coupled HR neurons that mutually inhibit each other form a Half-Center Oscillator (HCO), the basis of a mammalian respiratory CPG. Varying different parameters, including the magnitude of injected current, allows us to determine how neural behavior changes under different conditions. At most levels of injected current, the neural networks exhibit periodic firing behavior, but in certain ranges, the firing behavior is aperiodic. We observe the system dynamics to be nonlinear; the changes in current, stimulation, and conductance support the notion that CPG behavior can be altered via extrinsic modulation. Furthermore, using three coupled HR neurons representing oscillator kernels (representations of specific CPG complexes), we model the mammalian respiratory CPG and its chaotic states. We propose the addition of a differential equation modeling the synaptic gating variable to stabilize the oscillations around a certain frequencies for 2 coupled neurons. The implications of our work suggest that controlled stimulation of CPG networks holds merit as a potential therapeutic for those with rhythmic pathologies. 


### Repository Structure
The main files implementing the Hindmarsh-Rose (HR) Neuron Model are ``HRneuron.py`` and ``HRneuronseg.py`` and ``synapseseg.py`` for creating modular networks of HR neurons. 

The file ``HRneuron_sim.py`` implements the base HRneuron model to simulate the effect of a neuron under changes in injected current and stimulation, and produce matplotlib figures. 

``sim.py`` is the general simulation file for the modular HR neuron system. 

The file ``firing_rate.py`` uses the HRneuron model and allows us to analyze the chaotic / aperiodic region. 

``bifurcation.py`` allows us to produce bifurcation graphs relating firing rate with ISIs (interspike intervals). 

``poincare_data_gen.py`` creates poincare sections of the membrane potential-ion transport rate phase portrait in relevance to injected current. 

``phase_change_plotting.py`` uses a `.npy` file generated using ``sim.py`` to plot the neuron's spiking phase change resulting from a 2ms stimulation.

All interesting result images can be viewed in ``/images``.
