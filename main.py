import numpy as np

def min_max(low, up, max_NumberX, min_NumberX, lisX):
    if low == up:
        if max_NumberX < lisX[up]:
            max_NumberX = lisX[up]

        if min_NumberX > lisX[up]:
            min_NumberX = lisX[up]
    else:
        mid = (low + up) // 2
        min_max(low, mid, max_NumberX, min_NumberX, lisX)
        min_max(mid + 1, up, max_NumberX, min_NumberX, lisX)

    return (
        max_NumberX,
        min_NumberX
    )

data = np.random.randint(1, 100, 30)
lis = data.tolist()

max_Number = 0
min_Number = 1000
lowS = 0
upS = len(lis) - 1

min_max(lowS, upS, max_Number, min_Number, lis)

print(min_Number, max_Number)
print(lis)



