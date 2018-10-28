from num2words import num2words
def closed_range(start, stop, step):
  dir = 1 if (step > 0) else -1
  num = int( (stop + 1)/step -(start + 1)/step +1)
  return range(start, stop + dir, step),num
def countEs (a,b,step):   
    ms = [num2words(i) for i in  list(closed_range(a,b,step)[0])]
    ab=[ms[i].count('e') for i in range(closed_range(a,b,step)[1])]     
    ans_dict = {}
    for i in range(len(ab)):
        ans_dict[list(closed_range(a,b,step))[0][i]] = ab[i] 
    return ans_dict
ans=countEs(500,505,3)
