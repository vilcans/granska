#!/usr/bin/env python

import sys
import re
from jinja2 import Template

template = Template(open('view.html').read())

comment_re = re.compile(r'(REVIEW)\s*:\s*(.*)')

files = sys.argv[1:]
files.sort()

items = []

for file in files:
    stream = open(file, 'r')
    for line_number, line in enumerate(stream):
        match = comment_re.search(line)
        if match:
            items.append({
                'file': file,
                'line': line_number + 1,
                'type': match.group(1),
                'comment': match.group(2),
            })

    stream.close()

print template.render(items=items)
