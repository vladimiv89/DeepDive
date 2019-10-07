from datetime import datetime, timezone, timedelta

class Account:

    def __init__(self, account_numer: str, first_name: str, last_name: str, tz_offset: int, balance: float=0):
        self._account_number = account_numer
        self._first_name = first_name
        self._last_name = last_name
        self.tz_offset = tz_offset
        self._balance = balance
        self._transaction_counter = 0

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, f_name: str):
        if isinstance(str, f_name) and f_name.strip():
            self._first_name = f_name.strip()
        else:
            raise ValueError("First name should be composed of letters only and cannot be ")
    
    @property
    def last_name(self):
        return self._first_name

    @last_name.setter
    def last_name(self, l_name: str):
        if l_name.isalpha() and l_name.strip():
            self._last_name = l_name.strip()
        else:
            raise ValueError("Last name should be composed of letters only and cannot be ")
    
    
    @property
    def balance(self):
        return self._balance



a = Account("A214124E", "Ivan", "Vladimirov", +2)

print(datetime.utcnow() - timedelta(hours=2))
print(datetime.now().strftime("%Y%M%D %H%M%S"))


