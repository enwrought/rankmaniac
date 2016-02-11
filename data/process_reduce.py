#!/usr/bin/env python

import sys
import re

find_tabs = re.compile('\t')
find_commas = re.compile(',')
find_colons = re.compile(':')

def format_line(line):
    """
        Returns (is_done, node, pagerank, remainder_of_line)
    """
    tmp_key, tmp_values = find_tabs.split(line.strip())
    key = tmp_key == 'done'
    values = find_commas.split(tmp_values)
    return (key, values[0], float(values[1]), ','.join(values[2:]))

done = []
all_lines = []
process_incomplete = False
for line in sys.stdin:
    is_done, node, pagerank, remainder = format_line(line)

    if process_incomplete:
        sys.stdout.write('NodeId:%s\t%f,%s\n' % (node, pagerank, remainder))
    else:
        all_lines.append('NodeId:%s\t%f,%s\n' % (node, pagerank, remainder))
        if is_done:
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



