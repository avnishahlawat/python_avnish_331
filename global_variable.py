# Sample program using Global variable 
count = 0  

def increment():
    global count   # declaring count as global
    count += 1
    print("Inside function, count =", count)

# Main program
print("Initial count =", count)
increment()
increment() 
print("Final count =", count) 