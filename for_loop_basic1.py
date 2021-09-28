for x in range(151):
    print(x)

for y in range(5,1001,5):
    print(y)

for z in range(1,101):
    if(z%10 == 0):
        print("Coding Dojo")
    elif(z%5 == 0):
        print("Coding")
    else:
        print(z)

sum = 0
for a in range(1,500000,2):
    sum += a
print(sum)

count = 2018
while count >= 0:
    print(count)
    count -=4

def multiple(lowNum=2,highNum=9,mult=3):
    for b in range(lowNum, highNum + 1):
        if(b%mult == 0):
            print(b)
multiple()