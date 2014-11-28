#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import copy
import sys
import pdb, pprint

class LRKeyword():
    def __init__(self, name = '', synonyms = []):
        self.children = []
        self.synonyms = synonyms
        self.name = name

    def add_child(self, child):
        self.children.append(child)
        return len(self.children)

    def add_synonym(self, synonym = ''):
        self.synonyms.append(child)
        return len(self.synonyms)

class LRKeywords():
    def __init__(self, handle = None):
        self.keywords = {}
        if handle:
            self.read_keywords(handle)


    def read_keywords(self, input):

        """
        Translate keyword file into a nested structure with children (recursive)
        and synonyms.
        """

        keyword_stack = []
#        empty_keyword = {'name' : '', 'children' : {}, 'synonyms' : [], }

        last_level = 0
        for raw_line in input:
            line = raw_line.rstrip()
            keyword = line.lstrip()
            level = len(line)-len(keyword)
            print "depth", len(keyword_stack), "level", level, "value", line
            if (len(keyword) == 0) :
                continue
            if level == 0:
                newKeyword = LRKeyword(name=keyword)
                self.keywords[keyword] = newKeyword # copy.deepcopy(empty_keyword)
                #self.keywords[keyword]['name'] = keyword
                print " pushing"
                keyword_stack.append(newKeyword)
                last_level = level
            elif level > last_level:
                if keyword.startswith('{'):
                    synonym = keyword.strip('{}')
                    keyword_stack[-1].add_synonym(synonym)
                else:
                    newKeyword = LRKeyword(name=keyword)
                    keyword_stack[-1].add_child(newKeyword)   #  ['children'].update({keyword : copy.deepcopy(empty_keyword)})
                    #keyword_stack[-1]['children'][keyword]['name'] = keyword
                    print " pushing"
                    keyword_stack.append(newKeyword)
                    last_level = level
            elif level <= last_level:
                for i in range(0, last_level-level+1):
                    print " popping"
                    keyword_stack.pop()
                newKeyword = LRKeyword(name=keyword)
                keyword_stack[-1].add_child(newKeyword)
                #keyword_stack[-1]['children'].update({keyword : copy.deepcopy(empty_keyword)})
                #keyword_stack[-1]['children'][keyword]['name'] = keyword

                #keyword_stack.append(keyword_stack[-1]['children'][keyword])
                last_level = level

        return

    def write_keywords(self, output):
        """
        Write a nested structure with children (recursive)
        and synonyms back out into the Adobe Lightroom formatted file.
        """

        def print_keyword(keyword, depth):
            padding = '\t' * depth
            output.write(padding + keyword['name'] + '\n')
            for synonym in sorted(keyword['synonyms']):
                padding = '\t' * (depth+1)
                output.write(padding + '{' + synonym + '}\n')

            for child in sorted(keyword['children'].iterkeys()):
                print_keyword(keyword['children'][child], depth + 1)

        for keyword in sorted(keywords.iterkeys()):
            print_keyword(keywords[keyword], 0)

    def traverse_keywords(self, keywords, function, level=0):
        for keyword in keywords:
            function(keywords[keyword], level)
            traverse_keywords(keywords[keyword]['children'], function, level+1)

        return

if __name__ == "__main__":

    """
    Convert keywords to/from Lightroom Keyword Project format from/to my format
    """

    input_file = "Lightroom Keywords - Possible.txt"

    input = open(input_file, 'r')

    lrk = LRKeywords(handle=input)

    pdb.set_trace()

