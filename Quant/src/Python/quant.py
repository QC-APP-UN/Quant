#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import C_AM as am
#import B_Norm as norm
#import wave_animation as w_a
#import orthogonality as ortho
#import B_Box as box
#import B_Boxc as boxc
#import B_BlackB as blackb
#import C_HLA as hla
#import C_PT as pert
#import C_NM_A as nmpot2
#import C_NM_B as nmpotn

def C_AM(l, m):
    am.angular_momentum(l, m)


#def C_Norm():
    

    
#def wave_animation():

#def orthogonality():

#def B_Box():

#def B_BlackB1():

#def B_BlackB2():

#def C_HLA():

#def C_PT():

#def C_NM_A():

#def C_NM_B():



def function(argument):
    switcher = {
        C_AM: C_AM(sys.argv[2], sys.argv[3])
    }
    func = switcher.get(argument, lambda: "Undefined Function")
    func()


if __name__ == "__main__":
    function(sys.argv[1])
