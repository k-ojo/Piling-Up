from collections import deque #importing deque from collection module 

for i in range(int(input())): # going through each test
    n = int(input())
    ls = deque(map(int, input().split()))# creating a deque object to allow pop and popleft oprations
    if ls[0] >=ls[-1]:    #finding what end has the largest sidelength
        k = ls.popleft()
    else: 
        k = ls.pop()
    for _ in range(n): # arranging from bigger sidelenght to the smallest 
        if ls and k >= ls[-1] and ls[-1 ]>=ls[0] :
            ls.pop()
        elif ls and k >= ls[-1]:
            ls.popleft()
        elif not ls:
            print('Yes')
        else:
            print("No")
            break
