class Email:
    def __init__(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_address(self, address):
        if "@" in address:
            self.__address = address
        else:
            print("Error: address must contain @")

    def get_domain(self):
        return self.get_address().split("@")[1]


e = Email("test@mail.ru")
print(e.get_domain())

e.set_address("new@yandex.ru")
print(e.get_domain())

e.set_address("wrongemail.com")
print(e.get_domain())
