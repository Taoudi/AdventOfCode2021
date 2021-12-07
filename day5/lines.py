import numpy as np
ocean = np.zeros(shape=(1000,1000))

def diagonal(sx,sy,ex,ey):
    bx,by = [x1>x2 for x1,x2 in zip([sx,sy],[ex,ey])]
    current_x,current_y = sx,sy
    while True:
        ocean[current_x,current_y]+=1
        if current_x == ex and current_y == ey:
            break
        current_x=current_x-1  if bx else current_x+1
        current_y=current_y-1 if by else current_y+1

def read_data():
    inputs = open('day5_input', 'r')
    for line in inputs:
        start_coords,end_coords = line.split(' -> ')
        sx,sy=start_coords.split(',')
        ex,ey=end_coords.split(',')
        sx,sy,ex,ey = int(sx),int(sy), int(ex), int(ey)

        #vertical
        if sx == ex:                
            big = max(sy,ey)
            small = min(sy,ey)
            for idx in range(small,big+1):
                ocean[sx,idx]+=1
        #horizontal
        elif sy == ey:
            big = max(sx,ex)
            small = min(sx,ex)
            for idx in range(small,big+1):
                ocean[idx,sy]+=1
        else:
            diagonal(sx,sy,ex,ey)
        
    values = ocean[ocean>=2.0]
    print(len(values))

read_data()