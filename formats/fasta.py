#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
The fasta file parse libraries.
"""


import os
import sys

from Bio import SeqIO
from bioway.apps.base import ActionDispatcher

def main():
    actions = (
            ('test','test print 124')
            )
    p = ActionDispatcher(actions)
    p.dispatch(globals())


def parsefasta(infasta,item='record'):
    """
    
    """
    f = SeqIO.parse(open(infasta),'fasta')
    return f
def info(infasta):
    """
    Stat the fasta.
    """
    print(212)

def gen_fasize(infasta):
    """
    Generate a tuple of the fasta chromosome size.
    >>>gen_fasize('reference.fasta')
        ('Chr1','3232323')
        ...
        ...
        ('Chr12',3423424)
    """
    f = SeqIO.parse(open(infasta),'fasta')
    for record in f:
        yield (record.id,len(record.seq))


def fasize(infasta):
    """
    Return a dictionary of the fasta chromosome size.
    >>>fasize('reference.fasta')
    {'Chr1':1231231,...}
    """
    fasize_dict = {}
    f = parsefasta(infasta)
    for record in f:
        fasize_dict[record.id] = len(record.seq)
   # for i in gen_fasize(infasta):
    #    fasize_dict[i[0]] = i[1]
    return fasize_dict


class OutPut:
    pass

def test():
    print(123)


if __name__ == "__main__":
    main()