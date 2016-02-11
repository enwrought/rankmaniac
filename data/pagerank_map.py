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

    '''
    if is_in_stopping_criteria(curr, prev):
        sys.stdout.write('FinalRank:%f\t%s\n' % (curr, node))
        continue
    '''

    # Otherwise, we need to continue iterating for node

    # Also print out curr (for new value of prev) and adjacencies
    sys.stdout.write('%s\tAdjacencies:%s\n' % (node, ','.join(adjacencies)))
    sys.stdout.write('%s\tPrevPageRank:%f\n' % (node, curr))

    # Contribution from node to adj_node
    for adj_node in adjacencies:
        sys.stdout.write('%s\tValue:%f\n' % (adj_node, curr/n))
