class Begin:
    def handle_message(self):
        return "Starting the process..."


class TwentyFive(Begin):
    def handle_message(self):
        return "TwentyFive"


class Fifty(TwentyFive):
    def handle_message(self):
        return "Fifty"


class Thirty(TwentyFive):
    def handle_message(self):
        return "Thirty"


class Five(Begin):
    def handle_message(self):
        return "Five"


class Ten(Five):
    def handle_message(self):
        return "Ten"


class Thirty_Five(Five):
    def handle_message(self):
        return "Thirty_Five"


class fifteen(Ten, Thirty):
    def handle_message(self):
        return "fifteen"


class Error(Fifty, Thirty, Thirty_Five):
    def handle_message(self):
        return "Error occurred!"


class Success(Thirty_Five, fifteen):
    def handle_message(self):
        return "Success!"


begin = Begin()
error = Error()
success = Success()
twenty_five = TwentyFive()
fifty = Fifty()
thirty = Thirty()
five = Five()
ten = Ten()
thirty_five = Thirty_Five()
fifteen = fifteen()
begin.next_step = error
error.next_step = success

print(begin.handle_message())
print(twenty_five.handle_message())
print(error.handle_message())
print(success.handle_message())
print(five.handle_message())
print(fifty.handle_message())
print(thirty.handle_message())
print(ten.handle_message())
print(thirty_five.handle_message())
print(fifteen.handle_message())
