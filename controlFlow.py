#Control Flow

a = "eggs"
if a:
    print("It is true")

h = 42
if h > 50:
    print("Greater than 50")
else:
    print("less than 50")

#If-else if-else case

if a:
    print("It is true")

h = 42
if h > 50:
    print("Greater than 50")
elif h<20:
    print("Less than 20")
else:
    print("less than 50")

#While Looping

c = 5
while c != 0:
    print(c)
    c-=1 #augmented operators

d = 3
while d:
    print(d)
    d-=1

# how to exit a loop

while True:
    response = input()
    #stay in loop until you get a number divisible by 7
    if int(response) % 7 == 0:
        break
    else:
        print("Enter a number 7")

