organizations = []

while(True):
    response = input('(1)Add organization (2)Print organizations (3)Exit: ')
    if response == '1':
        organization_name = input('Organization name: ')
        organization_address = input('Organization address: ')
        organization_id = input('Organization id: ')

        organization = {
            'name': organization_name,
            'address': organization_address,
            'id': organization_id,
            'employees': []
        }

        organizations.append(organization)

    elif response == '2':
        for organization in organizations:
            print("---ORGANIZĀCIJA---")
            print(f"{organization['name']} ({organization['id']})")
            print(f"Adrese: {organization['address']}")
            print(f"Kontaktu skaits: {len(organization['employees'])}")
    elif response == '3':
        print('Bye bye!')
        exit()