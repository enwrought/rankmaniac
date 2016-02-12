#!/usr/bin/env python

import sys
import re

ALPHA = 0.85
find_tabs = re.compile('\t')
find_colons = re.compile(':')

def format_line(line):
    key, tmp_values = find_tabs.split(line.strip())
    value_type, value = find_colons.split(tmp_values)
    if value_type == 'Adjacencies':
        return (key, value_type, value)
    elif value_type == 'PrevPageRank':
        return (key, value_type, float(value))
    elif value_type == 'Value':
        return (key, value_type, float(value))
    elif value_type == 'Iteration':
        return (key, value_type, value)
    else:
        raise Exception('Not a valid type.')


def is_final_rank(line):
    ''' Checks whether line starts with 'FinalRank:'. '''
    return len(line) > 10 and line[0:10] == 'FinalRank:'

def print_output(node, rank, prev, adjacencies):
    comma = ','
    if adjacencies == '':
        comma = ''
    sys.stdout.write('NodeId:%s\t%f,%f%s%s\n' %
            (node, rank, prev, comma, adjacencies))

curr_node = ''
curr_sum = 0
curr_count = 0
curr_prev = 0
curr_adjacencies = ''
# To ensure that every node is on the same iteration (since some nodes may be
# generated after the first iteration, such as if a node with no adjencies is
# not explicitly defined in the input), the iteration value should not be
# reset as the other values are
curr_iteration = '0'

for line in sys.stdin:
    if is_final_rank(line):
        sys.stdout.write(line)
        continue

    node, value_type, value = format_line(line)
    if node != curr_node:
        # print out info on previous node
        if curr_node != '':
            print_output(curr_node + ',' + curr_iteration, 
                         ALPHA * curr_sum + 1-ALPHA,
                         curr_prev, curr_adjacencies)
        # reset values
        curr_node = node
        curr_sum = 0
        curr_count = 0
        curr_prev = 0
        curr_adjacencies = ''

    if value_type == 'Adjacencies':
        curr_adjacencies = value
    elif value_type == 'PrevPageRank':
        curr_prev = value
    elif value_type == 'Value':
        curr_sum += value
        curr_count += 1
    elif value_type == 'Iteration':
        if int(value) > int(curr_iteration):
            curr_iteration = value

if curr_node != '':
    print_output(curr_node + ',' + curr_iteration, ALPHA * curr_sum + 1-ALPHA,
            curr_prev, curr_adjacencies)
