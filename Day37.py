contacts = [
    ["Анна", "+7-912-345-67-89"],
    ["Борис", "+7-921-234-56-78"],
    ["Виктор", "+7-931-123-45-67"]
]

def show_all(contacts): 
    for cont in contacts:
        print(f"Имя: {cont[0]}, телефон: {cont[1]}")

show_all(contacts)

def find_by_name(contacts, name):
    for cont in contacts:
        if cont[0] == name:
            return cont[1]
        
    return None

        
find_by_name(contacts, 'Виктор')
        
def add_contact(contacts, name, phone):
    add = [name, phone]
    contacts.append(add)

add_contact(contacts, 'Art', '89677108699')


contacts = [
    {"name": "Анна", "phone": "+7-912-345-67-89", "favorite": True},
    {"name": "Борис", "phone": "+7-921-234-56-78", "favorite": False},
    {"name": "Виктор", "phone": "+7-931-123-45-67", "favorite": True}
]

def show_favorites(contacts):
    for contact in contacts:
        if contact["favorite"] == True:
            print(contact)


show_favorites(contacts)

def add_contact_dict(contacts, name, phone, favorite):
    cont_dict = {
        "name": name,
        "phone": phone,
        "favorite": favorite
    }
    contacts.append(cont_dict)

add_contact_dict(contacts, 'Art', '89677108699', True)

def toggle_favorite(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            if contact['favorite'] == True:
                contact['favorite'] = False
            else: contact['favorite'] = True

toggle_favorite(contacts, "Виктор")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
             contacts.remove(contact)

delete_contact(contacts, 'Art')