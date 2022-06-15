from fractions import Fraction

def solution(pegs):    
    if len(pegs) >= 2:
        if len(pegs)%2 == 0:
            even = True
            sum = (-pegs[0] + pegs[len(pegs)-1])
            for i in range(1,len(pegs) -1):
                sum += (2*((-1)**(i+1)*pegs[i]))
        else:
            even = False
            sum = (-pegs[0] - pegs[len(pegs)-1])
            for i in range(1,len(pegs) -1):
                sum += (2*(-1)**(i+1)*pegs[i])

    else:
        return [-1,-1]
        
    first_gear_radius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    radius_Check = first_gear_radius
    for i in range(len(pegs)-2):
        next_radius = pegs[i+1] - pegs[i] - radius_Check
        if (radius_Check < 1 or next_radius < 1):
            return [-1,-1]
        else:
            radius_Check = next_radius

    if first_gear_radius.numerator/first_gear_radius.denominator >= 1:
        return [first_gear_radius.numerator, first_gear_radius.denominator]
    else:
        return [-1,-1]