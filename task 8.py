contacts = []
def add_contact():
    new_contact = input("enter the contact you want to add")
    contacts.append(new_contact)
def view_contacts():
    print(contacts)
def search_contact():
    searched_contact = input("enter the contact name you want to find")
    if searched_contact in contacts:
        print(f"{searched_contact} is available in your list of contacts")
    else:
        print("the contact you are looking for is non existent")
def remove_contact():
    r_contact = input("enter the contact you want to remove")
    contacts.remove(r_contact)
while True:
    Menu = ["1. add a contact, 2. view all contacts, 3. search a contact, 4. remove a contact"]
    choice = int(input("choose the number you want"))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        remove_contact()
    else:
        print("invalid choice")
