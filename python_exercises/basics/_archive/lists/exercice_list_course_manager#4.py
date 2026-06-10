courses = []

while True:
    print("Shopping Menu")
    print("1. Add a product")
    print("2. Remove a product")
    print("3. Show the list")
    print("4. Search for a product")
    print("5. Clear the list")
    print("6. Sort the list")
    print("7. Stop")

    choice = int(input("What do you want to do? "))

    if choice == 1:
        product = input("Which product do you want to add? ")
        courses.append(product)
        print("Product added to the shopping list.")
    elif choice == 2 :
        product = input("Which product do you want to remove from the list? ")
        if product in courses:
            courses.remove(product)
            print("Product removed.")
        else : 
            print("Product not in the list.")
    elif choice == 3 : 
        print("Actual list :",courses)
    elif choice == 4 :
        recherche = input("What product are you looking for ?:")
        if product in courses : 
            print(f"{recherche} is in the list.")
        else : 
            print(f"{recherche} isn't in the list.")
    elif choice == 5 : 
        courses.clear()
        print("List cleared")
    elif choice == 6 : 
        courses.sort()
        print("Over.")
        break