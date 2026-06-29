elements = {45, 12, 78, 23, 56, 9, 34}

print("Set of Elements:", elements)

print("\nChoose an option:")
print("1. Display in Ascending Order")
print("2. Display in Descending Order")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("Ascending Order:")
    print(sorted(elements))
elif choice == 2:
    print("Descending Order:")
    print(sorted(elements, reverse=True))
else:
    print("Invalid Choice!")