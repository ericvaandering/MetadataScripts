#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from  LRKeywords import LRKeywords

if __name__ == "__main__":

    """
    Convert keywords to/from Lightroom Keyword Project format from/to my format
    """

    input_file = "Lightroom Keywords - Possible.txt"

    input = open(input_file, 'r')

    lrk = LRKeywords(handle=input)

    print "\n\nContents\n"

    def print_kw(kw):
        if kw.children:
            return
        if kw.synonyms:
            return
        print "%3d  %s" % (kw.depth, kw.name)

    kw_count = {}

    def count_kw(kw):

        if kw_count.get(kw.name, 0):
            kw_count[kw.name] += 1
            print kw_count[kw.name], "instances of", kw.name
        else:
            kw_count[kw.name] = 1

    for kw in lrk.keywords:
        if kw.name != 'Animals':
            continue
        kw.traverse_keywords(print_kw)

    for kw in lrk.keywords:
        kw.traverse_keywords(count_kw)
