#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

def shell(cmd, no_wait_rtn=False, quiet=True):
    if not quiet:
        print cmd
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    if no_wait_rtn:
        return
    out, err = p.communicate()
    if p.returncode:
        print err
    if not quiet:
        print out
    return p.returncode,out,err
