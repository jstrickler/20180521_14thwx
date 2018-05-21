import sys
import re
from glob import glob
import fileinput

raw_pattern = sys.argv[1]
pattern = re.compile(raw_pattern)
del sys.argv[1]
files = [ glob(f) for f in sys.argv[1:] ]
for line in fileinput.input(*files):
    if pattern.search(line):
        print('{}: {}'.format(fileinput.filename(), line), end='')