def solution(x, y):
    Max, Min = max(int(x), int(y)), min(int(x), int(y))
    generationCount = 0
    while Min > 0:
        generationCount += Max//Min
        Max, Min = Min, Max%Min
    if Max != 1:
        return "impossible"
    return str(generationCount - 1)