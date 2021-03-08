#python 3.7.1
import time
a = int(input('enter the range(square): '))
n = 1
for i in range(0,a+1):
    print (n,'^',2,'=',n*n)
    n = n + 1
    time.sleep(0.5)
    if n == a + 1:
        print('thank u')
        break
    else:
        pass
        
print ('made by Ro706')
print("PLEASE GIVE ME A ⭐ FOR MY MOTIVATION")
