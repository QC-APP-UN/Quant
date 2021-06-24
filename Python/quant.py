#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import B_BlackB as bblack
import B_Box as bbox
import B_BoxC as bboxc
#huckel pending
import B_Norm as norm
import C_AM as am
import C_Bohr as bohr
import C_HLA as hla
import C_IAO as iao
import C_NM_A as nma
import C_NM_B as nmb
import C_PT as pt
import D_BS as bs
import D_HFC as hfc
import D_HFMP2 as hfmp2
import D_UR as ur 
import D_CBS as cbs

def B_BlackB_1():
    if len(sys.argv) == 3:
        print("B_BlackB_1")
        bblack.cn1(sys.argv[2])
    else:
        raise NameError('B_BlackB_1: Missing argument')


def B_BlackB_2():
    if len(sys.argv) == 3:
        print("B_BlackB_2")
        bblack.cn2(sys.argv[2])
    else:
        raise NameError('B_BlackB_2: Missing argument')


def B_Box():
    if len(sys.argv) == 9:
        print("B_Box")
        bbox.fCaja(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], 1)
    else:
        raise NameError('B_Box: Missing argument')


def B_BoxC():
    if len(sys.argv) == 6:
        print("B_BoxC")
        bboxc.anonda(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        raise NameError('B_BoxC: Missing argument')


def B_Huck():
    if len(sys.argv) == 4:
        print("B_Huck")
        raise NameError('B_Huck: Missing argument') #Pending
    else:
        raise NameError('B_Huck: Missing argument')


def B_Norm():
    if len(sys.argv) == 3:
        print("B_Norm")
        print(norm.gNormalize(sys.argv[2]))
    else:
        raise NameError('B_Norm: Missing argument')


def C_AM():
    if len(sys.argv) == 4:
        print("C_AM")
        print(am.angular_momentum(sys.argv[2], sys.argv[3]))
    else:
        raise NameError('C_AM: Missing argument')


def C_Bohr():
    if len(sys.argv) == 5:
        print("C_Bohr")
        bohr.BSorbit((sys.argv[2]), (sys.argv[3]), (sys.argv[4]))
    else:
        raise NameError('C_Bohr: Missing argument')


def C_HLA():
    if len(sys.argv) == 6:
        print("C_HLA")
        hla.hid(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    else:
        raise NameError('C_HLA: Missing argument')


def C_IAO():
    if len(sys.argv) == 7:
        print("C_IAO")
        iao.osar(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    else:
        raise NameError('C_IAO: Missing argument')


def C_NM_1():
    if len(sys.argv) == 5:
        print("C_NM_1")
        nma.numerovN2(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        raise NameError('C_NM_1: Missing argument')


def C_NM_2():
    if len(sys.argv) == 7:
        print("C_NM_2")
        nmb.numerovN2(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    else:
        raise NameError('C_NM_2: Missing argument')


def C_PT_1():
    if len(sys.argv) == 4:
        print("C_PT_1")
        raise NameError('C_PT_1: Missing argument')
    else:
        raise NameError('C_PT_1: Missing argument')


def C_PT_2():
    if len(sys.argv) == 4:
        print("C_PT_2")
        raise NameError('C_PT_2: Missing argument')
    else:
        raise NameError('C_PT_2: Missing argument')


def D_BS():
    if len(sys.argv) == 6:
        print("D_BS")
        bs.BS_H(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    else:
        raise NameError('D_BS: Missing argument')


def D_HFC():
    if len(sys.argv) == 5:
        print("D_HFC")
        hfc.HF_H2(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        raise NameError('D_HFC: Missing argument')


def D_HFMP2():
    if len(sys.argv) == 5:
        print("D_HFMP2")
        hfmp2.HF_MP2(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        raise NameError('D_HFMP2: Missing argument')


def D_UR():
    print(len(sys.argv))
    if len(sys.argv) == 7:
        print("D_UR")
        ur.UR(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    else:
        raise NameError('D_UR: Missing argument')
        
def D_CBS():
    print(len(sys.argv))
    if len(sys.argv) == 8:
        print("D_UR")
        cbs.CBS(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
    else:
        raise NameError('D_UR: Missing argument')

def function(argument):
    switcher = {
        'B_BlackB_1': B_BlackB_1,
        'B_BlackB_2': B_BlackB_2,
        'B_Box': B_Box,
        'B_BoxC': B_BoxC,
        'B_Huck': B_Huck,
        'B_Norm': B_Norm,
        'C_AM': C_AM,
        'C_Bohr': C_Bohr,
        'C_HLA': C_HLA,
        'C_IAO': C_IAO,
        'C_NM_1': C_NM_1,
        'C_NM_2': C_NM_2,
        'C_PT_1':  C_PT_1,
        'C_PT_2':  C_PT_2,
        'D_BS': D_BS,
        'D_HFC': D_HFC,
        'D_HFMP2': D_HFMP2,
        'D_UR': D_UR,
        'D_CBS': D_CBS
    }
    func = switcher.get(argument, lambda: "Undefined Function")
    func()


if __name__ == "__main__":
    function(sys.argv[1])
