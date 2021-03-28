#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 01:06:01 2020

@author: davidarchilapena
"""

import eel
import subprocess

eel.init('src')

@eel.expose
def anonda():
    subprocess.Popen("python3 anonda.py", shell=True)

@eel.expose
def caja():
    subprocess.Popen("python3 caja.py", shell=True)

@eel.expose
def norm():
    subprocess.Popen("python3 norm.py", shell=True)

@eel.expose
def hid():
    subprocess.Popen("python3 hid.py", shell=True)

@eel.expose
def moman():
    subprocess.Popen("python3 moman.py", shell=True)

@eel.expose
def orto():
    subprocess.Popen("python3 orto.py", shell=True)

@eel.expose
def osar():
    subprocess.Popen("python3 osar.py", shell=True)


@eel.expose
def pertur():
    subprocess.Popen("python3 pertur.py", shell=True)

@eel.expose
def pot2():
    subprocess.Popen("python3 pot2.py", shell=True)

@eel.expose
def potn():
    subprocess.Popen("python3 potn.py", shell=True)

@eel.expose
def cn():
    subprocess.Popen("python3 cn.py", shell=True)



eel.start('prin1.html', port=8800)