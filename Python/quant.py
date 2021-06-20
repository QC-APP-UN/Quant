#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import C_AM as am
import B_Norm as norm
import B_BlackB as bblack

def B_Norm():
    if len(sys.argv) == 3:
        print(norm.gNormalize(sys.argv[2]))
    #else:
        #raise NameError('B_Norm: Missing argument')

def B_BlackB_1():
    if len(sys.argv) == 3:
        bblack.cn1(sys.argv[2])

def B_BlackB_2():
    if len(sys.argv) == 3:
        bblack.cn2(sys.argv[2])

def C_AM():
    if len(sys.argv) == 4:
        print(am.angular_momentum(sys.argv[2], sys.argv[3]))
    #else:
        #raise NameError('C_AM: Missing argument')


def function(argument):
    switcher = {
        C_AM: C_AM(),
        B_BlackB_1: B_BlackB_1(),
        B_Norm: B_Norm(),
        B_BlackB_2: B_BlackB_2()
    }
    func = switcher.get(argument, lambda: "Undefined Function")
    func()


if __name__ == "__main__":
    function(sys.argv[1])
