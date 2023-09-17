lw=int(input('enter lwr number: '))
up=int(input('enter upr number: '))
for num in range(lw,up+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            
