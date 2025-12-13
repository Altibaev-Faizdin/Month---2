class Contact:
    def __init__(self, name, phone_number, id):
        self.name = name
        self.phone = phone_number
        self.id = id

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) == 10:
            return True
        return False


class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.last_id += 1
            contact = Contact(name, phone_number, cls.last_id)
            cls.all_contacts.append(contact)
            print(f"Контакт '{name}' добавлен с id={contact.id}")
        else:
            raise ValueError(f"Невозможно добавить контакт '{name}': неверный номер")

    @classmethod
    def remove_contact(cls, contact_id):
        for contact in cls.all_contacts:
            if contact.id == contact_id:
                cls.all_contacts.remove(contact)
                print(f"Контакт с id={contact_id} удалён")
                return
        print(f"Контакт с id={contact_id} не найден")


print(ContactList.all_contacts)  # []
ContactList.add_contact("Доналд Трамп", "0700100200")
ContactList.add_contact("Илон Маск", "0500123456")


print("\nСписок контактов после добавления:")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone, contact.id)

print(ContactList.last_id)

print('\n--------')
ContactList.remove_contact(1)
ContactList.remove_contact(7)

print("\nСписок контактов после удаления:")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone, contact.id)

print('\nЕсли что тут ошибка выдаёт, потому что тут цифра не содержит =! 10, если что этот коммент Алинур писал:')
ContactList.add_contact("Cristiano Ronaldo", "55512384")
