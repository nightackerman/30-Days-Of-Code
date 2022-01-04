def add(p,q):
    return p+q

def subtract(p,q):
    return p-q

def multiply(p,q):
    return p*q

def divide(p,q):
    return p/q

print("Please select the operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

choice = input("Please enter choice (a/b/c/d)")
p = int(input("Enter a number: "))
q = int(input("Enter another number: "))

if choice=='a':
    print(f"Addition of {p} and {q} is,", p+q)
elif choice=='b':
    print(f"Subtraction of {p} and {q} is, ", p-q)
elif choice=='c':
    print(f"Multiplication of {p} and {q} is, ", p*q)
elif choice=='d':
    print(f"Division of {p} and {q} is, ",p/q)

else:
    print("This is an Invalid input")