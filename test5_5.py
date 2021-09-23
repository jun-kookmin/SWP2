import time
import random
#재귀
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
#반복
def iterfibo(nbr):
    a,b = 1,1
    if nbr==1 or nbr==2:
        return 1
        
    for i in range(1,nbr):
        a,b = b, a+b

    return a

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts_2 = time.time()
    fiboo = iterfibo(nbr)
    ts_2 = time.time() - ts_2
    print("Fibo_for(%d)=%d, time %.6f" %(nbr, fiboo, ts_2))
    print("걸린 시간 비교 재귀문 - 반복문 값 >> {}".format(ts - ts_2))
    break
