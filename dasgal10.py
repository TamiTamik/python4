#n too hurtelh buh anhni toog ol
a = int(input("too: "))
for number in range (1,a+1):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count+=1
    if count == 2:
        print(number)
