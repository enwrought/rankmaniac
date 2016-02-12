#!/usr/bin/env python

import sys
import re
import math

find_tabs = re.compile('\t')
find_commas = re.compile(',')
find_colons = re.compile(':')

def format_line(line):
    """
        Returns (pagerank, node, iteration, prev_pagerank, remainder_of_line)
    """
    str_pagerank, tmp_values = find_tabs.split(line.strip())
    values = find_commas.split(tmp_values)
    return (1000000-float(str_pagerank), values[0], values[1], float(values[2]), ','.join(values[3:]))

def is_in_stopping_criteria(curr, prev):
    ''' Checks whether the stopping criteria is satisfies given current
        and previous PageRank values.'''
    return (curr - prev) ** 2 < 0.001


done = []
first_20_lines = []
process_incomplete = False
final_iteration = False

might_finish = True
count = 0
'''
copy = []
for line in sys.stdin:
    copy.append(line)

copy.reverse()
for line in copy:
    '''
for line in sys.stdin:
    pagerank, node, iteration, prev, remainder = format_line(line)

    # If max iter, we just print it out
    if int(iteration) >= 48 and count < 20:
        sys.stdout.write('FinalRank:%f\t%s\n' % (pagerank, node))
    if int(iteration) >= 48 and count >= 20:
        break

    # Check if we meet stopping criteria
    if count < 20 and might_finish:
        comma = ',' if len(remainder) > 0 else ''
        first_20_lines.append('NodeId:%s,%s\t%f,%f%s%s\n' % (node, iteration,
            pagerank, prev, comma, remainder))
        done.append((node, pagerank))
        might_finish = is_in_stopping_criteria(pagerank, prev)
    elif count >= 20 and might_finish:
        # print out and done
        for i in xrange(len(done)):
            sys.stdout.write('FinalRank:%f\t%s\n' % (done[i][1], done[i][0]))
        break
    else:
        # count >= 20 and not might_finish: or
        # count < 20 and not might_finish
        comma = ',' if len(remainder) > 0 else ''
        sys.stdout.write('NodeId:%s,%s\t%f,%f%s%s\n' % (node, iteration, pagerank, prev,
            comma, remainder))
    count += 1

if not might_finish:
    for line in first_20_lines:
        sys.stdout.write(line)



