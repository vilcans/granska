#!/usr/bin/env python

import sys
import re
import os.path
from jinja2 import Template

my_dir = os.path.dirname(__file__)
template = Template(open(my_dir + '/view.html').read())

types = (
    'REVIEW',
    'TODO',
    'FIXME',
)
type_to_items = {}

comment_re = re.compile('(' + '|'.join(types) + r')\s*:?\s*(.*)')

items = []

def scan_file(directory, file):
    stream = open(os.path.join(directory, file), 'r')
    for line_number, line in enumerate(stream):
        match = comment_re.search(line)
        if match:
            item = {
                'file': file,
                'line': line_number + 1,
                'type': match.group(1),
                'comment': match.group(2),
            }
            type_to_items.setdefault(item['type'], []).append(item)
    stream.close()

args = sys.argv
dir = '.'
i = 1
while i < len(args):
    arg = sys.argv[i]
    if arg == '-C':
        dir = args[i + 1]
        i += 2
    else:
        scan_file(dir, args[i])
    i += 1

print template.render(type_to_items=type_to_items, types=types)
