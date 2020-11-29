"""
This script transforms an .off file with faces that have more than 3 vertices
and break these faces into multiple triangules creating new triangular faces

USAGE: python3 break-faces-into-triangules.py < cone.off > cone-tri.off
"""

import sys

from itertools import combinations

passedOFF = False
passedVertexFaceAndEdgeCount = False
passedVertices = False

numVertices = 0
numFaces = 0
numEdges = 0

lines = sys.stdin.readlines()
new_lines = [line for line in lines if len(line.strip()) != 0]
lines = new_lines
i = 0

line = lines[i].strip()
i += 1

while line[0] == '#':
    line = lines[i].strip()
    i += 1

if '#' in line:
    hastag_index = line.index('#')
    line = line[:hastag_index]

# OFF header
print(line)
line = lines[i].strip()
i += 1

while line[0] == '#':
    line = lines[i].strip()
    i += 1

if '#' in line:
    hastag_index = line.index('#')
    line = line[:hastag_index]

# Num. of vertices, faces and edges
# print(line)

lineSplit = line.split()
numVertices = int(lineSplit[0])
numFaces = int(lineSplit[1])
numEdges = int(lineSplit[2])

new_lines = []
newNumFaces = 0
newNumEdges = 0

line = lines[i].strip()
i += 1

# All vertices
for j in range(numVertices):
    while line[0] == '#':
        line = lines[i].strip()
        i += 1

    if '#' in line:
        hastag_index = line.index('#')
        line = line[:hastag_index]

    lineSplit = line.split()
    vertexXYZ = [lineSplit[0], lineSplit[1], lineSplit[2]]
    new_lines.append(' '.join(vertexXYZ))

    line = lines[i].strip()
    i += 1

# All faces
for j in range(numFaces):
    while line[0] == '#':
        line = lines[i].strip()
        i += 1

    if '#' in line:
        hastag_index = line.index('#')
        line = line[:hastag_index]

    lineSplit = line.split()
    numVerticesForTheFace = int(lineSplit[0])
    faceVertices = []

    for k in range(numVerticesForTheFace):
        faceVertices.append(lineSplit[k + 1])

    # Divide the polygon face into triangules
    triangulesVertices = combinations(faceVertices, 3)

    for trianguleVertices in triangulesVertices:
        newNumFaces += 1
        newNumEdges += 3
        new_lines.append(f'3 {" ".join(trianguleVertices)}')
    
    if j < numFaces - 1:
        line = lines[i].strip()
        i += 1

print(f'{numVertices} {newNumFaces} {newNumEdges}')
for line in new_lines:
    print(line)
