x = 0
row = 0
tri = (' '*(row-x-1) + '*'*(2*x+1))

x = x + 1
row = row + 1

print( '%s' % tri)