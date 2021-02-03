m=[]
name=[]
total=0
high=0
low=100
n=int(input('How many people in this class?'))

for i in range(n):
    stuname=input('Please input the name:')
    score=int(input('Please input the score:'))
    total=total+score
    name.append(stuname)
    m.append(score)
    if high< m[i]:
        high=m[i]
        highname=name[i]
    if low>m[i]:
        low=m[i]
        lowname=name[i]
    
average=total/n
print(m)
print('average',average)
print('high:',high,highname)
print('low:',low,lowname)