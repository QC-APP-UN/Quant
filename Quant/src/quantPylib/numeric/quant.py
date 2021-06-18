#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import angular_momentum as a_m
import normalization as norm
import wave_animation as w_a
import orthogonality as ortho
import particle_box as p_b
import black_body as b_b
import hidrogenlike_atom as h_a
import perturbation_theory as pert
import numerov_method_pot2 as nmpot2
import numerov_method_potn as nmpotn

def angular_momentum(l, m):
    a_m.angular_momentum(l, m)

def normalization():

def wave_animation():

def orthogonality():

def particle_box():

def cn():

def hid():

def pertur():

def pot2():

def potn():



def function(argument):
    switcher = {
        angular_momentum: angular_momentum(sys.argv[2], sys.argv[3])
    }
    func = switcher.get(argument, lambda: "Undefined Function")
    func()


if __name__ == "__main__": quant potn arg .....
    function(sys.argv[1])
