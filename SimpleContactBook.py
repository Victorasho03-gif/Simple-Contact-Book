contacts = {}

while True: 
    print('\nContact Book')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input('Enter your choice = ')

    # 1. Create contact
    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            location = input('Enter location = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'location': location, 'email': email, 'mobile': mobile}
            print(f'Contact name {name} has been created successfully!')

    # 2. View contact
    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Location: {contact["location"]}, Mobile: {contact["mobile"]}, Email: {contact["email"]}')
        else:
            print('Contact not found')

    # 3. Update contact
    elif choice == '3':
        name = input('Enter name to update contact = ')
        if name in contacts:
            location = input('Enter updated location = ')
            email = input('Enter updated email = ')
            mobile = input('Enter updated mobile number = ')
            contacts[name] = {'location': location, 'email': email, 'mobile': mobile}
            print('Contact updated successfully!')
        else:
            print('Contact not found')

    # 4. Delete contact
    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact not found')

    # 5. Search contact
    elif choice == '5':
        search_name = input('Enter contact name to search: ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name: {name}, Location: {contact["location"]}, Mobile: {contact["mobile"]}, Email: {contact["email"]}')
                found = True
        
        if not found:
            print('No contact found with that name')

    # 6. Count contacts
    elif choice == '6':
        print(f'Total contacts in your book: {len(contacts)}')

    # 7. Exit
    elif choice == '7':
        print('Good bye... closing')
        break

    # Invalid input
    else:
        print('Invalid input')
