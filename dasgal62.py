a = int(input("too: "))
count = 0
for i in range(1, a+1):
    if a%i == 0:
        count = count + 1
print(count)
