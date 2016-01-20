import sys

line= sys.stdin.readline()
num = int(line)
line= sys.stdin.readline()
params = line.split()
rows = int(params[0])
cols = int(params[1])
data=[]
for i in range(0,rows):
	line = sys.stdin.readline()
	params = line.split()
	data0 = []
	for param in params:
		data0.append(int(param))
	data.append(data0)
print num
print data