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

    # Get the current process iteration number and emit it.
    iteration=0
    keys = find_commas.split(node)
    if len(keys) == 1:
        # There is no iterator value
        iteration=1
    else:
        # Increment the iterator
        iteration = int(keys[1]) + 1
        node = keys[0]

    # Print out the iteration data
    sys.stdout.write('%s\tIteration:%s\n' % (node, str(iteration)))

    # Also print out curr (for new value of prev) and adjacencies
    sys.stdout.write('%s\tAdjacencies:%s\n' % (node, ','.join(adjacencies)))
    sys.stdout.write('%s\tPrevPageRank:%f\n' % (node, curr))

    # Contribution from node to adj_node
    for adj_node in adjacencies:
        sys.stdout.write('%s\tValue:%f\n' % (adj_node, curr/n))
    if len(adjacencies) == 0:
        sys.stdout.write('%s\tValue:1.0\n' % node)
