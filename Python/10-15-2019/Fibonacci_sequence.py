
first  = 1
second = 1
print("Fibonacci sequence: ",end='' )
print("%d " % first ,end='' )
print("%d "% second ,end='' )
for i in range(1,19):
    sum = first + second
    first = second
    second = sum
    print(" %d " % sum ,end='' )

