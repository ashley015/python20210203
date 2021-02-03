m=[]
total=0
high=0
low=100
n=int(input('How many people in this class?'))

for i in range(n):
    score=int(input('Plase input the score:'))
    total=total+score
    if high< score:
        high=score
    if low>score:
        low=score
    m.append(score)
    
average=total/n
print(m)
print('average',average)
print('high',high)
print('low',low)
