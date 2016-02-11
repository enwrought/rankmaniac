#!/usr/bin/env python

import sys
import re
import math

find_tabs = re.compile('\t')
find_commas = re.compile(',')
find_colons = re.compile(':')

def format_line(line):
    """
        Returns (is_done, node, iteration, pagerank, remainder_of_line)
    """
    tmp_key, tmp_values = find_tabs.split(line.strip())
    key = tmp_key == 'done'
    values = find_commas.split(tmp_values)
    return (key, values[0], values[1], float(values[2]), ','.join(values[3:]))

done = []
all_lines = []
process_incomplete = False
final_iteration = False
for line in sys.stdin:
    is_done, node, iteration, pagerank, remainder = format_line(line)
    
    if int(iteration) >= 50:
        final_iteration = True

    if process_incomplete:
        node = str(node) + ',' + str(iteration)
        sys.stdout.write('NodeId:%s\t%f,%s\n' % (node, pagerank, remainder))
    else:
        nInterVal = str(node) + ',' + str(iteration)
        all_lines.append('NodeId:%s\t%f,%s\n' % (nInterVal, pagerank, remainder))
        if is_done or final_iteration:
            done.append((node, pagerank))
        else:
            process_incomplete = True

if process_incomplete:
    for line in all_lines:
        sys.stdout.write(line)
else:
    ranked = sorted(done, key = lambda item: item[1], reverse=True)
    for i in xrange(min(20, len(ranked))):
        sys.stdout.write('FinalRank:%f\t%s\n' % (ranked[i][1], ranked[i][0]))



