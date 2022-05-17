# conditional

message = "Hello"

if message.startswith('H'):
    print("condition is  true)")

else:
    print("condition is false")


num = 10

if num == 10:
    print("condition is  true)")

else:
    print("condition is false")


""" is 
!=
<
> """

l1 = [1, 2, 3, 4, 5]
l2  = l1

if 3 in l2:
    print("condition is  true)")

else:
    print("condition is false")

l1 = [1, 2, 3, 4, 5]
l2  = l1

if 3 in l2 and 6 in l2:
    print("condition is  true)")

else:
    print("condition is false")


if 0 <= num <= 10:
    print("condition is  true)")

else:
    print("condition is  false)")


time = input("Enter the time: ")

if time < "12:00":
    Print("Good Morning")

elif time > "12:00":
    print("Good Afternoon")

else time = "!2:00":
    print("Noon")


print("Good Morning" if time < "12:00" \
        else("Good afternoon" if time > "12:00" else("It is noon")))

print("Good Morning" if time < "12:00" else("Good afternoon" if time > "12:00" else("It is noon")))        