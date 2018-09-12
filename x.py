class Driver:

    def get_first(self):
        return self._first

    def set_first(self, first):
        self._first = first

    def del_first(self):
        del self._first

    first = property(get_first, set_first, del_first)

    def get_last(self):
        return self._last

    def set_last(self, last):
        self._last = last

    def del_last(self):
        del self._last

    last = property(get_last, set_last, del_last)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        self._rating = rating

    def del_rating(self):
        del self._rating

    rating = property(get_rating, set_rating, del_rating)

    def get_miles_driven(self):
        return self._miles_driven

    def set_miles_driven(self, miles_driven):
        self._miles_driven = miles_driven

    def del_miles_driven(self):
        del self._miles_driven

    miles_driven = property(get_miles_driven, set_miles_driven, del_miles_driven)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def greet_passenger(self):
        return "Hello! I'll be your driver today. My name is {}".format(self.fullname())


class Passenger:

    def get_first(self):
        return self._first

    def set_first(self, first):
        self._first = first

    def del_first(self):
        del self._first

    first = property(get_first, set_first, del_first)

    def get_last(self):
        return self._last

    def set_last(self, last):
        self._last = last

    def del_last(self):
        del self._last

    last = property(get_last, set_last, del_last)

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def del_email(self):
        del self._email

    email = property(get_email, set_email, del_email)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def yell_name(self):
        return "{}".format(self.fullname().upper())
