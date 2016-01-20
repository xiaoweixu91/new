#This code resolves the problem Pizza Delivery.Since the brutal way takes too much time so I tried to reduce the running time by using 
#the property of Manhattan distance and figure out the pattern behind the computation.
import sys
import time
#input of case number

line= sys.stdin.readline() 
num = int(line)
#initialization the list of result
result_l=[]

for case_num in range(num):
    #input the size of street
    line= sys.stdin.readline()
    size=line.split()
    cols=int(size[0])
    rows=int(size[1])
#   street = [map(int, row.split()) for row in sys.stdin]
#   input the street with delivery time
    street=[]
    for i in range(0,rows):
		line = sys.stdin.readline()
		params = line.split()
		street0 = []
		for param in params:
			street0.append(int(param))
		street.append(street0)
    
    #smallest in col
    temp=0
    dp=[0 for col in range(cols)]
    sum_col=map(sum,zip(*street))
    for col_target in range(cols):
        for col_move in range(cols):
            temp=abs(col_move-col_target)*sum_col[col_move]
            dp[col_target]+=temp
    
    #smallest in row
    sum_row=map(sum,street)
    cost=[0 for row in range(rows)]
    for r in range(rows):
        for row in range(rows):
            #cost[row][col]+=dp[col]/float(rows)+abs(row-r)*sum_row[r]
            cost[row]+=abs(row-r)*sum_row[r]
                
    result=min(cost)+min(dp)
    
    result_l.append(result)
  
for i in range(num):
	print str(result_l[i])+' blocks'
# start=time.clock()
# end=time.clock()
# timeee=start-end
# print timeee



