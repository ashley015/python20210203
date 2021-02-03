m=[]
total=0
high=0
low=100
n=int(input('How many people in this class?'))

for i in range(n):
    stuname=input('Please input the name:')
    score=int(input('Please input the score:'))
    total=total+score
    m.append(stuname)
    m.append(score)
for i in range(1,n*2,2):
    if high<m[i]:
       high=m[i]
       highname=m[i-1]
for i in range(1,n*2,2):
    if low>m[i]:
        low=m[i]
        lowname=m[i-1]
    
average=total/n
print(m)
print('average',average)
print('high:',high,highname)
print('low:',low,lowname)