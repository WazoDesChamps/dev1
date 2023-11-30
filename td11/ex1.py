
def ya_max(tuples):
    max = tuples[0]

    for i in tuples[1:]:
        if i > max:
            max = i
        
    return max


tuple = (-4, 12, -71, 33, 20, 32, 96, -22, -7, 70, 82, 62, 11, 72, -36, -16, 84)

result = ya_max(tuple)
result_max = max(tuple)

print(result)
print(result_max)

