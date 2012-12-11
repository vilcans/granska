#!/usr/bin/env python

import sys
import re
from jinja2 import Template

template = Template(open('view.html').read())

comment = re.compile(r'(REVIEW)\s*:\s*(.*)')

files = sys.argv[1:]
files.sort()

items = []

for file in files:
    stream = open(file, 'r')
    content = stream.read()
    stream.close()
    for match in comment.findall(content):
        items.append({
            'file': file,
            'type': match[0],
            'comment': match[1]
        })

print template.render(items=items)
