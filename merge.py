#http://www.codeskulptor.org/#user40_DCdcICjiTO_2.py
"""
    Merge function for 2048 game.
    """

def merge(line):
    """
        Function that merges a single row or column in 2048.
        """
    # replace with your code
    # put the non-zero first and zero second,eg.2204 ->2240
    len_line = len(line)
    non_zero = []
    zero = []
    for idx in range(len_line):
        if line[idx] != 0:
            non_zero.append(line[idx])
        else:
            zero.append(line[idx])
    non_zero.extend(zero)
    #print non_zero
    try_to_merge = []
    zero = []

    #merging part
    for idx in range(len_line):
        if idx > len_line-2:
            break
        #print idx
        if non_zero[idx] == non_zero[idx+1] and non_zero[idx] != 0:
            new=non_zero[idx]*2
            try_to_merge.append(new)
            non_zero[idx+1]=-1
            zero.append(0)
        
        elif non_zero[idx] >= 0:
            try_to_merge.append(non_zero[idx])

if non_zero[-1] >=0 :
    try_to_merge.append(non_zero[-1])
    try_to_merge.extend(zero)
    #print zero
    
    return try_to_merge

#test=[8,16,16,8]
#print merge(test)
#[2, 0, 2, 4] should return [4, 4, 0, 0]
#[0, 0, 2, 2] should return [4, 0, 0, 0]
#[2, 2, 0, 0] should return [4, 0, 0, 0]
#[2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0]
#[8, 16, 16, 8] should return [8, 32, 8, 0]

