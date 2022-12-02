a = int(input("please enter first  triangle side size : "))
b = int(input("please enter second triangle side size : "))
c = int(input("please enter third  triangle side size : "))
print("----------------------------------------------------")
if ((a <= (b+c)) and (b <= (a+c)) and (c <= (a+b))):
    print("your entered size can be a triangle side sizes.")
    print("----------------------------------------------------")
else:
    print("your entered size can't be a triangle side sizes.")
    print("----------------------------------------------------")
