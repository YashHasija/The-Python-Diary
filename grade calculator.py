score = input("Enter Score: ")
s=float(score)
if s<0.0 or s>1.1:
    print('value out of range')
else:
    
    if s>=0.9:
        print('A')
    elif s>=0.8:
        print('B')
    elif s>=0.7:
        print('C')
    elif s>=0.6:
        print('D')
    else:
        print('F')