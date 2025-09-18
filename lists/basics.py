# Creating a list
fruits = ["apple", "banana", "mango", "orange"]

# Printing the list
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])

# Adding elements
fruits.append("grapes")
print("After adding grapes:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing banana:", fruits)

# Updating elements
fruits[1] = "pineapple"
print("After updating second element:", fruits)

# Iterating through the list
print("\nIterating through list:")
for fruit in fruits:
    print(fruit)
