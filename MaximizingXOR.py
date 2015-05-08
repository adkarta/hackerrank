#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
  return l ^ r;

max_xor = 0

_l = int(raw_input());


_r = int(raw_input());

_r += 1;

for i in range(_l, _r):
	for x in range(i, _r):
		res = maxXor(i, x);
		if res > max_xor:
			max_xor = res


print(max_xor)