from person import Person
from metode import print_contacts
from metode import add_contact
from metode import edit_contact
from metode import delte_contact

def main():
    print("Dobrodosli v programu Contact Book")

    john = Person(first_name="John", last_name="Clark", phone_number="89348239429", email="john@clark.com", birth_date=1978)
    marissa = Person(first_name="Marissa", last_name="Mayer", phone_number="83483204032", email="marissa@yahoo.com", birth_date=1975)
    bruce = Person(first_name="Bruce", last_name="Wayne", phone_number="902432309443", email="bruce@batman.com", birth_date=1989)

    contacts = [john, marissa, bruce]

    while True:
        print ""
        print "Proim izberi eno od naslednjih moznosti:"
        print "a) Izpisi vse svoje stike"
        print "b) Dodaj nov stik"
        print "c) Uredi stik"
        print "d) Izbrisi stik"
        print "e) Izhod iz programa."
        print ""

        selection = raw_input("Vnesi svojo izbiro (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            print_contacts(contacts)
        elif selection.lower() == "b":
            add_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            delte_contact(contacts)
        elif selection.lower() == "e":
            print "Hvala za uporabo programa! "
            break
        else:
            print "Ne razumem tvoje izbire. Prosim poskusi ponovno."
            continue



if __name__ == "__main__":
    main()
