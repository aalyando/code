a = b = c = 0


class Telephone:
    description_number = 'Somebody number'
    _incoming_counter = 0

    def set_number(self, phone_number):
        self.description_number = phone_number

    def numb_calls(self):
        return self._incoming_counter

    def answer_call(self):
        self._incoming_counter +=1


telephone_first = Telephone()
telephone_second = Telephone()
telephone_third = Telephone()

telephone_first.set_number = '0663402059'
telephone_second.set_number = '0501397046'
telephone_third.set_number = '0959725269'

while a < 5:
    telephone_first.answer_call()
    a += 1
while b < 3:
    telephone_second.answer_call()
    b += 1
while c < 7:
    telephone_third.answer_call()
    c += 1


def total_amount_calls(telephones):
    total_amount = 0
    for i in telephones:
        total_amount += i.numb_calls()
    return total_amount


telephones = [telephone_first, telephone_second, telephone_third]
total_amount = total_amount_calls(telephones)
print('Total amount of calls for all three telephones:', total_amount)

