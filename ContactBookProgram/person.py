class Person(object):
    first_name=""
    last_name=""
    email=""
    birth_date=""
    phone_number=""
    contacts=[]

    def __init__(self, first_name, last_name, email, birth_date, phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.birth_date=birth_date
        self.phone_number=phone_number

    def full_name(self):
        return self.first_name+" "+self.last_name
