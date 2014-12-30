#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find keywords that do not have a synonym defined. This is limited in this example to the
top level keyword "Animals". I use this because Animals should have a scientific and
common name defined.
"""

import argparse
import sys

from  LRKeywords import LRKeywords

if __name__ == "__main__":

    """
    Find keywords that do not have a synonym defined. This is limited in this example to the
    top level keyword "Animals"
    """

    input_file = "Lightroom Keywords - Possible.txt"

    input = open(input_file, 'r')

    lrk = LRKeywords(handle=input)

    def print_kw(kw):
        """
        Only print leaves of the tree (no children) that don't have synonyms
        """
        if kw.children:
            return
        if kw.synonyms:
            return
        print "%3d  %s" % (kw.depth, kw.name)

    for kw in lrk.keywords:
        if kw.name != 'Animals':
            continue
        kw.traverse_keywords(print_kw)
