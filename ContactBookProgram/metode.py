from person import Person

def print_contacts(contacts):
    for i, person in enumerate(contacts):
        print (str(i+1)+". ")
        print person.first_name
        print person.last_name
        print person.email
        print person.birth_date
        print person.phone_number

        if not contacts:
            print("Naseznamu nimas stikov.")


def add_contact(contacts):
    first_name=raw_input("Vnesi ime: ")
    last_name=raw_input("Vnesi priimek: ")
    email=raw_input("Vnesi email naslov: ")
    birth_date=raw_input("Vnesi rojstni datum: ")
    phone_number=raw_input("Vnesi telefonsko stevilko: ")

    newContact=Person(first_name=first_name, last_name=last_name, email=email, birth_date=birth_date, phone_number=phone_number)
    contacts.append(newContact)

    print ("")
    print(newContact.full_name() +" si uspesno dodal na seznam.")


def edit_contact(contacts):
    print ("Izberi stevilko stika, ki ga zelis urediti: ")

    for i, person in enumerate(contacts):
        print (str(i)+" "+person.full_name())
        print ("")

    index=raw_input("Izberi zaporedno stevilko kontakta, ki ga zelis psremeniti: ")
    selected_contact = contacts[int(index)]



    pogoj=raw_input("Ali zelis spremeniti ime? da/ne")
    if pogoj.lower()=="da":
        new_name= raw_input("Vnesi novo ime za: " + selected_contact.full_name())
        selected_contact.first_name=new_name
        print""
        print ("Ime posodobljeno")

    pogoj = raw_input("Ali zelis spremeniti priimek? da/ne")
    if pogoj.lower() == "da":
        new_name = raw_input("Vnesi nov priimek za: " + selected_contact.full_name())
        selected_contact.last_name = new_name
        print""
        print ("Priimek posodobljen")

    pogoj = raw_input("Ali zelis spremeniti email? da/ne")
    if pogoj.lower() == "da":
        new_name = raw_input("Vnesi nov email naslov za: " + selected_contact.full_name())
        selected_contact.email = new_name
        print""
        print ("Email naslov posodobljen")

    pogoj = raw_input("Ali zelis spremeniti rojstni datum? da/ne")
    if pogoj.lower() == "da":
        new_name = raw_input("Vnesi nov rojstni datum za: " + selected_contact.full_name())
        selected_contact.birth_date = new_name
        print""
        print ("Rojstni datum posodobljen")

    pogoj = raw_input("Ali zelis spremeniti telefonsko stevilko? da/ne")
    if pogoj.lower() == "da":
        new_name = raw_input("Vnesi novo telefonsko stevilko za: " + selected_contact.full_name())
        selected_contact.phone_number = new_name
        print""
        print ("Telefonska stevilka posodobljena")

def delte_contact(contacts):
    print ("Izberi stevilko stika, ki ga zelis izbrisati: ")

    for i, person in enumerate(contacts):
        print (str(i) + " " + person.full_name())
        print ("")

    index = raw_input("Izberi zaporedno stevilko kontakta, ki ga zelis izbrisati: ")
    selected_contact = contacts[int(index)]

    contacts.remove(selected_contact)
    print ""
    print("Kontakt je bil uspesno odstranjen")












