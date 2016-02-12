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

for line in sys.stdin:
    node, curr, prev, adjacencies = format_line(line)
    n = len(adjacencies)
    comma = ',' if len(adjacencies) > 0 else ''

    sys.stdout.write('%f\t%s,%f%s%s\n' %
                (1000000-curr, node, prev, comma, ','.join(adjacencies)))
