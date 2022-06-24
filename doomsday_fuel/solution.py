from fractions import Fraction
import numpy as np

def AB(m,absorbing_state, non_absorbing_state):
    A, B = [], []
    for i in non_absorbing_state:
        temp_A = []
        temp_B = []
        for j in non_absorbing_state:
            temp_B.append(m[i][j])
        for j in absorbing_state:
            temp_A.append(m[i][j])
        
        A.append(temp_A)
        B.append(temp_B)
    
    return A,B

def solution_matrix(m,absorbing_state,non_absorbing_state):
    A = AB(m,absorbing_state,non_absorbing_state)[0]
    B = AB(m,absorbing_state,non_absorbing_state)[1]
    I = np.identity(len(B))
    F = I - B
    F_inverse = np.linalg.inv(F)
    sol_matrix = np.dot(F_inverse, A)

    return sol_matrix

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)   

def clean(m):
    needed = m[0]
    to_fraction = [Fraction(i).limit_denominator() for i in needed]
    lcm = 1
    for i in to_fraction:
        if i.denominator != 1:
            lcm = i.denominator
    for i in to_fraction:
        if i.denominator != 1:
            lcm = lcm*i.denominator/gcd(lcm, i.denominator)
    to_fraction = [Fraction(i*lcm).numerator for i in to_fraction]
    to_fraction.append(int(lcm))
    return to_fraction

def into_probabilities(m):
    for i in range(len(m)):
        total = sum(m[i])
        for j in range(len(m[i])):
            if sum(m[i]):
                m[i][j] /= float(total)
    return m

def solution(m):
    n = len(m)
    if n==1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    absorbing_state = []
    non_absorbing_state = []

    for row in range(len(m)):
        count = 0
        for item in range(len(m[row])):
            if m[row][item] == 0:
                count += 1
        if count == n:
            absorbing_state.append(row)
        else:
            non_absorbing_state.append(row)
    probabilities = into_probabilities(m)
    final_output = solution_matrix(m,absorbing_state,non_absorbing_state)

    return clean(final_output)
