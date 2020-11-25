# This program calculates the total energy and magnetization
# for a 1D Ising model with N dipoles
# Author: Nico Grisouard, University of Toronto
# Date: 24 November 2020

# import modules
import numpy as np
from random import random, randrange


def energyfunction(J_, dipoles):
    """ function to calculate energy """
    energy = -J_*np.sum(dipoles[0:-1]*dipoles[1:])
    return energy


def acceptance(ARGUMENTS):
    """ Function for acceptance probability; to be completed """
    # Do stuff here
    return result  # result is True of False


# define constants
kB = 1.0
T = 1.0
J = 1.0
num_dipoles = 100
N = 100

# generate array of dipoles and initialize diagnostic quantities
dipoles = np.ones(num_dipoles, int)  # hint: this will not work
energy = []  # empty list; to add to it, use energy.append(value)
magnet = []  # empty list; to add to it, use magnet.append(value)

E = energyfunction(J, dipoles)
energy.append(E)
magnet.append(sum(dipoles))
print(dipoles)

for i in range(N):
    picked = randrange(num_dipoles)  # choose a victim
    dipoles[picked] *= -1  # propose to flip the victim
    Enew = energyfunction(J, dipoles)  # compute Energy of proposed new state

    # calculate acceptance probability
    accepted = acceptance(Enew, E,)

    # store energy and magnetization


# plot energy, magnetization
