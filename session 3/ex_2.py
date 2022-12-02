n = []      #numbers set
a = int(input("Please enter how many number you want to enter : "))
print(" ")
print("-----------------------------------------------------------")
i = 0
#i = int(i)
while(i <= (a-1)):
    b = int(input("Please enter a number : "))
    n.append(b)
    i += 1
c   = len(n)     #number of members of n list (numbers numbers)
d   = sum(n)     #nembers sum
n_a = d / c      #numbers average
print("---------------------------------------------")
print("The collection of number you entered..: ", n)
print("The number of numbers you entered.....: ", c)
print("Sum of the number you entered.........: ", d)
print("The average of the entered numbers....: ", d, " / ",c, " = ",n_a)
print("---------------------------------------------")
