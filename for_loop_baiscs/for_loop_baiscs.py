#task 1
for i in range(151):
    print(i)

#task 2
for i in range(5,100,5):
    print(i)

#task 3
for i in range(1,101):
    if i%5==0 and i%10==0:
        print(i,' ','Coding', ' ', 'Coding dojo')
    elif i%5==0 and i%10!=0:
        print(i,'Coding')
    elif i%5!=0 and i%10==0:
        print(i,'Coding Dojo')
    elif i%5!=0 and i%10!=0:
        print(i)

#task 4
sum=0
for i in range(0,500000):
    if i%2!=0:
        sum+=i
print(sum)

#task 5
for i in range(2018,-1, -4):
    print(i)

#task 6
low_num=4
high_num=50
mult=4
for i in range(low_num,high_num,mult):
    if i%mult==0:
        print(i)
        