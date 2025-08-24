a = 10
b = 20
c = 30

average = (a + b + c)/3
print("The average is",average)

if average > a and average > b and average > c:
    print(average,"is greater than all")
elif average > a and average > b:
    print(average,"is greater than a and b")
elif average > a and average > c:
    print(average,"is greater than a and c")
elif average > b and average > c:
    print(average,"is greater than b and c")
elif average > a:
    print(average,"is greater than a")
elif average > b:
    print(average,"is greater than b")
elif average > c:
    print(average,"is greater than c")
else:
    print("Invalid input")