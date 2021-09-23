import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, s_idx, e_idx, target):
    
    mid_idx = (s_idx + e_idx) // 2

    if s_idx > e_idx:
        return -1
    #같은 경우
    if L[mid_idx] == target:
        return mid_idx
    #mid_idx가 target보다 큰 경우
    elif  L[mid_idx] > target:
        return recbinsearch(numbers, s_idx, mid_idx - 1, target)
    #mid_idx가 target보다 작은 경우    
    else:
        return recbinsearch(numbers, mid_idx + 1, e_idx, target)
    
    
    


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)
print(numbers)
numoftargets = int(input("Enter the number of targets: "))

targets = []
for i in range(1):
    targets += [numoftargets]
print(targets)

ts = time.time()

# binary search - recursive
cnt = 0

for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
#not found가 0일 경우엔 수를 찾음, 1은 찾지 못함
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
