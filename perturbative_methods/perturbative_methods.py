# -*- coding: utf-8 -*-
"""
perturbative_methods.
© Leonardo Lavagna 2024
@ Nesya: https://github.com/NesyaLab

This script demonstrates the use of perturbative methods [1] in quantum mechanics
using the qmsolve library [2]. The primary focus is on solving the Schrödinger equation
for a single particle in a harmonic oscillator potential and then adding a perturbation
to the potential to observe its effect on the energy eigenstates and eigenvalues.

Key Components:
- Definition of the harmonic oscillator potential.
- Introduction of a perturbation to the harmonic oscillator potential.
- Calculation and visualization of the eigenstates and eigenvalues for both
  the unperturbed and perturbed potentials.
  
References.
[1]...
[2] https://github.com/quantum-visualizations/qmsolve
"""

# Small perturbation parameter
epsilon = 0.01

# Degree of the perturbation term
degree = 1

from qmsolve import Hamiltonian, SingleParticle, init_visualization, Å, eV

def harmonic_oscillator(particle):
    """
    Define the harmonic oscillator potential for a single particle.
    
    Parameters:
    particle (SingleParticle): The particle object.
    
    Returns:
    float: The potential energy of the harmonic oscillator.
    """
    k = 2 * eV / Å**2  # Force constant for the harmonic oscillator
    return 0.5 * k * particle.x**2

def perturbed_harmonic_oscillator(particle):
    """
    Define the perturbed harmonic oscillator potential for a single particle.
    
    Parameters:
    particle (SingleParticle): The particle object.
    
    Returns:
    float: The potential energy of the perturbed harmonic oscillator.
    """
    V = harmonic_oscillator(particle)
    return V + epsilon * particle.x ** degree

# Define the Hamiltonian for the unperturbed harmonic oscillator
H = Hamiltonian(
    particles=SingleParticle(),
    potential=harmonic_oscillator,
    spatial_ndim=1,
    N=512,
    extent=20*Å
)

# Define the Hamiltonian for the perturbed harmonic oscillator
H_p = Hamiltonian(
    particles=SingleParticle(),
    potential=perturbed_harmonic_oscillator,
    spatial_ndim=1,
    N=512,
    extent=20*Å
)

# Solve for the eigenstates of the unperturbed Hamiltonian
eigenstates = H.solve(max_states=30)
print(eigenstates.energies)

# Visualize the eigenstates of the unperturbed Hamiltonian
visualization = init_visualization(eigenstates)
visualization.slider_plot()

# Solve for the eigenstates of the perturbed Hamiltonian
eigenstates_p = H_p.solve(max_states=30)
print(eigenstates_p.energies)

# Visualize the eigenstates of the perturbed Hamiltonian
visualization = init_visualization(eigenstates_p)
visualization.slider_plot()
