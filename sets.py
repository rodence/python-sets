friuts = {"Apple", "Grape"}

while True:
    print("CHOOSE")
    print("[1] Add Item")
    print("[2] Delete Item")
    print("[3] Display Item")
    print("[4] Exit")
    choice = int(input("Choose a number:"))
    if choice == 1:
        add = input("Enter Item: ")
        friuts.add(add)
    elif choice == 2:
        delete = input("Enter Item to delete: ")
        if delete in friuts:
            friuts.remove(delete)
    elif choice == 3:
        print(friuts)
    elif choice == 4:
        print("Thank You!")
        break
    else:
        print("Wrong Input!!")
