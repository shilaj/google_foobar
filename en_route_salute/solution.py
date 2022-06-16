from itertools import count

def solution(s):
    symbol1_count = s.count("<")
    symbol2_count = s.count(">")
    if symbol1_count > 0 and symbol2_count > 0:
        if '-' in s:
            x = s.replace('-', '')
        else:
            x = s
        vis_a_vis = 0
        for i in range(len(x)):
            if x[i] == ">":
                for j in range(i+1,len(x)):
                    if x[j] == "<":
                        vis_a_vis += 1
            elif x[i] == "<":
                for j in range(-len(x), -len(x)+i):
                    if x[j] == ">":
                        vis_a_vis += 1
    
        return vis_a_vis
    else:
        return 0