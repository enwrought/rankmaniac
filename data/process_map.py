#!/usr/bin/env python

import sys
import re

find_tabs = re.compile('\t')
find_commas = re.compile(',')

def format_line(line):
    tmp_key, tmp_values = find_tabs.split(line.strip())
    key = tmp_key[7:]
    values = find_commas.split(tmp_values)
    return (key, float(values[0]), float(values[1]), values[2:])

def is_in_stopping_criteria(curr, prev):
    ''' Checks whether the stopping criteria is satisfies given current
        and previous PageRank values.'''
    return (curr - prev) ** 2 < 0.001

for line in sys.stdin:
    node, curr, prev, adjacencies = format_line(line)
    n = len(adjacencies)
    comma = ',' if len(adjacencies) > 0 else ''

    if is_in_stopping_criteria(curr, prev):
        sys.stdout.write('done\t%s,%f,%f%s%s\n' %
                (node, curr, prev, comma, ','.join(adjacencies)))
    else:
        sys.stdout.write('not_done\t%s,%f,%f%s%s\n' %
                (node, curr, prev, comma, ','.join(adjacencies)))
