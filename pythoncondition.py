"""
#s1 = int(input ("Enter your mark: "))
if 100 >= s1 >= 0:

    if 100 >= s1 > 85:
        print("Distinction")
    elif (85 > s1 >= 65):
        print("Pass")  
    else:
        print("Fail")
else:
    print("Enter a mark between 0 and 100")

    """

s1 = input("Enter your mark: ")

if s1.isdigit():

    s2 = int(s1) 

    if 100 >= s2 >= 0:

        if (100 >= s2 >= 85):
            print("Distinction")
        elif (85 > s2 >= 65):
            print("Pass")  
        else:
            print("Fail")
    else:
        print("Enter a mark between 0 and 100")

else:
    print("2 Enter a mark between 0 and 100")
