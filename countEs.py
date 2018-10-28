from num2words import num2words
def closed_range(start, stop, step=1):
  dir = 1 if (step > 0) else -1
  num = stop + dir-start
  return range(start, stop + dir, step),num
def countEs (a,b):   
    ms = [num2words(i) for i in  list(closed_range(a,b)[0])]
    ab=[ms[i].count('e') for i in range(closed_range(a,b)[1])]     
    ans_dict = {}
    for i in range(len(ab)):
        ans_dict[list(closed_range(a,b))[0][i]] = ab[i] 
    return ans_dict
ans=countEs(500,505)

