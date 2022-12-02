n = []     #numbers list
while (True):
    a = input("Please enter a number : ")
    try:
        b = float(a)
        print(b)
    except:
        if a == 'e':
            break
        else:
            print("not float") 
        
    else:
        n.append(b)
        print(n)
        
if  n != [ ]:
    print("---------------------------------------------")
    c    = len(n)     #number of members of n list (numbers numbers)
    d    = sum(n)     #nembers sum
    n_a  = d / c      #numbers average
    print(n)
    print("the number of numbers you entered.....: ", c)
    print("sum of the number you entered.........: ", d)
    print("The average of the entered numbers....: ", d, " / ",c, " = ",n_a)
    print("---------------------------------------------")
