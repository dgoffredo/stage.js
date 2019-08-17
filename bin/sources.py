import itertools
import os
import sys


def sources_under(toplevel):
    for root, dirs, files in os.walk(toplevel):
        paths = (os.path.join(root, file) for file in files)
        for path in paths:
            if path.endswith('.js') and os.path.isfile(path):
                yield path


dirs = ['ext', 'lib', 'platform']
sources = itertools.chain(*(sources_under(dir) for dir in dirs))
sys.stdout.write(' '.join(sources))
