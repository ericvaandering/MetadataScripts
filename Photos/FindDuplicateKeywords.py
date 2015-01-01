#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find all the keywords that appear twice in the hierarchy.
Sometimes these are duplicates, sometimes not
(e.g. Fruits/Orange and Colors/Orange)
"""

import argparse
import sys

from  LRKeywords import LRKeywords

if __name__ == "__main__":

    """
    Find all the keywords that appear twice in the hierarchy.
    Sometimes these are duplicates, sometimes not
    (e.g. Fruits/Orange and Colors/Orange)
    """

    input_file = "Lightroom Keywords - Possible.txt"

    input = open(input_file, 'r')

    lrk = LRKeywords(handle=input)


    kw_count = {}

    def count_kw(kw):
        """
        Count the keywords and only print out ones already found
        """

        if kw_count.get(kw.name, 0):
            kw_count[kw.name] += 1
            print kw_count[kw.name], "instances of", kw.name
        else:
            kw_count[kw.name] = 1

    for kw in lrk.keywords:
        kw.traverse_keywords(count_kw)
