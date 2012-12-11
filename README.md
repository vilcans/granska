# Granska

A simple tool for keeping track of code reviews in code.

# Installation

Requires Jinja2 templating engine:

    pip install jinja2

# Usage

Example:

    ./granska.py -C ~/my-project $(cd ~/my-project; git ls-files) >result.html 
