hrs=input('enter hours:')
h=float(hrs)
rph=input('rate per hour:')
y=float(rph)
if h<=40:
    print(h*y)
else:
    print((40*y)+((h-40)*1.5*y))