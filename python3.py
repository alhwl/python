echo_user_input = input("type something: ")
print("you typed: " + echo_user_input + "" )

a = input("pick a number:" )
b = input("pick a second number: ")

c = int(a) + int(b)
print(f"The sum of {a} + {b} is: {c} ")


d = input("pick a number:" )
e = input("pick a second number:" )
f = input("pick a third number:" )

def multiply_three_numbers(d,e,f):
    g = int(d) * int(e) * int(f)
    return(g)

h = input("pick a number:" )
i = input("pick a second number: ")

j = int(h) > int(i)
if h > i:
        print(h, "is larger.")
if i > h:
        print(i, "is larger.")
if i == h:
        print("Both arguments are equal.")
