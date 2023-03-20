"""num_1 = 1
num_2 = 5

sum = num_1 + num_2

print(sum)

number1 = int(input("1st number:"))
number2 = int(input("2nd number:"))

add = number1 + number2

print(add)"""


A = int(input("type 1st number:"))
B = int(input("type 2nd number:"))
choice = input("give your operator + - * / (**)")

if choice =="+":
    sum = A + B
    print("the sum is:",sum)
elif choice =="-":
    diff = A - B
    print("The difference is:",diff)
elif choice =="*":
    mul = A * B
    print("The multiplication is:",mul)
elif choice =="/":
    div = A / B
    print("The Division is:",div)
elif choice == "**":
    pow = A**B
    print("The power is:", pow)
else:
    print("Choose correct operator")