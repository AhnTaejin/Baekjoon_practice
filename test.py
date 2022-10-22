dct = {201:[160, 47], 193:[172, 65], 23:[182, 97], 53:[166, 58], 127:[177, 75], 252:[193, 84]}

def result():
    for i,j in dct.items():
        print(f'Student ID {i}, Height {j[0]}, Weight {j[1]}')
result()