import pickle
import base64
import sys
import numpy as np

print("In Demo Script")
# x = pickle.loads(base64.decodebytes((sys.stdin[1], "ascii")))

a = sys.stdin.read(1)

read_file = open(a, 'rb')
# data = read_file.read()
data = pickle.loads(a)
print(data)

