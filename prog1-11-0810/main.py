import json

def load_data():
    file = open("prog1-11-0810/organizations.json","r")
    data = json.load(file)
    file.close()    
    global organizations
    organizations = data['organizations']


def add_organization():
    organization_name = input('Organization name: ')
    organization_address = input('Organization address: ')
    organization_id = input('Organization id: ')

    organization = {
        'name': organization_name,
        'address': organization_address,
        'id': organization_id,
        'contacts': []
    }        
    
    while(True):
        response = input('Do you want to add a contact (y/n)? ')
        if response == 'y':
            contact_name = input('Contact name: ')
            contact_position = input('Contact position: ')
            contact_id = input('Contact id: ')

            contact = {
                'name': contact_name,
                'position': contact_position,
                'id': contact_id
            }

            organization['contacts'].append(contact)              

        elif response == 'n':
            break 

    organizations.append(organization)


def print_organizations():
    for organization in organizations:
        print("---ORGANIZĀCIJA---")
        print(f"{organization['name']} ({organization['id']})")
        print(f"Adrese: {organization['address']}")
        print(f"Kontaktu skaits: {len(organization['contacts'])}")


def save_data():
    print('Saving your data...')

    dictionary = {
        'organizations': organizations
    }

    with open("prog1-11-0810/organizations.json", "w") as file:
        json.dump(dictionary, file, indent = 4)

    file.close()

    print('You data is saved.')


def main():
    load_data()

    while(True):
        response = input('(1)Add organization (2)Print organizations (3)Exit: ')
        if response == '1':
            add_organization()
        elif response == '2':
            print_organizations()
        elif response == '3':
            save_data()
            exit()

main()