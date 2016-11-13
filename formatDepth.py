import sys
import os

if len(sys.argv) != 5:
    print "Usage: " + sys.argv[0] + " <list of prefixes to include><directory to depth files><summary of sequencing read depth (post-trimming)><output file>"
    sys.exit()

## Guard
if not os.path.isfile(sys.argv[1]):
    print "Error: Invalid list of prefixes!"
    sys.exit()
input_list = sys.argv[1]

if not os.path.isdir(sys.argv[2]):
    print "Error: Invalid directory to depth files!"
    sys.exit()
indir_depth = sys.argv[2]

if not os.path.isfile(sys.argv[3]):
    print "Error: Invalid summary of depth file!"
    sys.exit()
input_depth = sys.argv[3]

output_file = sys.argv[4]


## Read input
isolates = []
inH = open(input_list)
for line in inH:
    line = line.strip('\n')
    isolates.append(line)
inH.close()

depth = {}
inH = open(input_depth)
for line in inH:
    line = line.strip('\n')
    tmp = line.split()
    depth[tmp[0]] = float(tmp[1])
inH.close()


## Process
outH = open(output_file, 'w')
for iso in isolates:
    storage = [0 for i in range(4411532+1)]

    infile = indir_depth + iso + '.depth'
    inH = open(infile)
    for line in inH:
        line = line.strip('\n')
        tmp = line.split()
        storage[int(tmp[1])] = int(tmp[2])
    inH.close()
    storage[0] = depth[iso]

    outH.write('%s %.1f' % (iso, storage[0]))
    for i in range(1, 4411532+1):
        outH.write(' %d' % storage[i])
    outH.write('\n')

outH.close()
