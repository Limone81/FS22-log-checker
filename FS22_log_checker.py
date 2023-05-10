#!/usr/bin/env python
__author__ = 'limone81'
__version__ = '0.0.1'
__status__ = 'dev'

### variables
logfile = 'log.txt'
outputfile = 'log_analyzed.txt'
warnings = []
errors = []

### main
with open(logfile, 'r') as analyze:
    for line in analyze:
        if 'Warning:' in line:
            warnings.append(line)
        elif 'Error:' in line:
            errors.append(line)            
        else:
            continue
analyze.close()

with open(outputfile, 'w') as f:
    print('WARNINGS', file=f)
    for item in range(len(warnings)):
        print(warnings[item], file=f)
    print('\n', file=f)
    print('ERRORS', file=f)
    for item in range(len(errors)):
        print(errors[item], file=f)
f.close()