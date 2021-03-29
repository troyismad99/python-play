
class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not number[2:].isdigit():
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

        '''
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

        A list of dictionaries
        List is each seat row, each row is a dictionary of seat letters

        rows, seats = self._aircraft.seating_plan() # tuple unpacking

        
        3. Discard the row numbers, we will use the list index (now 1 based) (_ is discard)-------------
                                                                                                        |
        self._seating =          [None] +                [        {letter:None for letter in seats} for _ in rows]
                                   ^                      ^        ^
                                   |                      |        |
        1. Throw away for 1 based -|                      |        |
        2. One entry for each row with list comprehension |        |
        4. Item expresion of list comp is Dictionary comprehension |
           creates a mapping of each single char seat to none to indicate empty seat
        '''


    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model        

    def seating_plan(self):
        return (range(1, self._num_rows + 1)
               , "ABCDEFGHJ"[:self._num_seats_per_row])




# f = Flight('UA2084')
# print(f.number())
# self comes into play with this format which is rarely seen
# print(Flight.number(f))

a = Aircraft("A-ABC", "Airbus A320", num_rows=22, num_seats_per_row=6)

print(a.registration()) # A-ABC
print(a.seating_plan()) # (range(1, 23), 'ABCDEF')


f = Flight("UA0284", Aircraft("A-ABC", "Airbus A320", 22, 6))

print(f.aircraft_model()) # Airbus A320

print(f._seating)
'''
[None, 
{'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}, 
{'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}, 
....

'''