#a-aas b hurtelh 5-d huvaagdah toonuudin niilberiig ol
a = int(input("a: "))
b = int(input("b: "))
niit = 0
for i in range(a, b+1):
    if i // 5 !=0:
       niit = niit + i
print("niilber: ", niit)