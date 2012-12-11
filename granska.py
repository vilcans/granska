#!/usr/bin/env python

import sys
import re
from jinja2 import Template

template = Template(open('view.html').read())

types = (
    'REVIEW',
    'TODO',
)
type_to_items = dict((t, []) for t in types)

comment_re = re.compile('(' + '|'.join(types) + r')\s*:\s*(.*)')

files = sys.argv[1:]
files.sort()

items = []

for file in files:
    stream = open(file, 'r')
    for line_number, line in enumerate(stream):
        match = comment_re.search(line)
        if match:
            item = {
                'file': file,
                'line': line_number + 1,
                'type': match.group(1),
                'comment': match.group(2),
            }
            type_to_items[item['type']].append(item)
    stream.close()

print template.render(type_to_items=type_to_items, types=types)
