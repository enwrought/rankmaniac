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

def is_final_rank(line):
    ''' Checks whether line starts with 'FinalRank:'. '''
    return len(line) > 10 and line[0:10] == 'FinalRank:'

def is_in_stopping_criteria(curr, prev):
    ''' Checks whether the stopping criteria is satisfies given current
        and previous PageRank values.'''
    return (curr - prev) ** 2 < 0.01


done = []
all_lines = []
not_done_count = 0
for line in sys.stdin:
    is_done, node, pagerank, remainder = format_line(line)

    all_lines.append('NodeId:%s\t%f,%s\n' % (node, pagerank, remainder))
    if is_done:
        done.append((node, pagerank))
    else:
        not_done_count += 1

if not_done_count > 0:
    for line in all_lines:
        sys.stdout.write(line)
else:
    ranked = sorted(done, key = lambda item: item[1], reverse=True)
    for i in xrange(min(20, len(ranked))):
        sys.stdout.write('FinalRank:%f\t%s\n' % (ranked[i][1], ranked[i][0]))



