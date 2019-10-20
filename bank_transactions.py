from datetime import datetime, timezone, timedelta
from collections import namedtuple

class TimeZone:

    def __init__(self, hours_offset: int, minutes_offset: int, tz_name: str):
        self._hours_offset = hours_offset
        self._minutes_offset = minutes_offset
        self._tz_name = tz_name

    @property
    def hours(self):
        return self._hours_offset
    @property
    def minutes(self):
        return self._minutes_offset
    @property
    def tz_name(self):
        return self._tz_name
    

class Account:

    interest_rate = 0.5
    _transaction_id = 0
    _transactions = dict()
    _transaction_details = namedtuple("TransactionDetails", ["transaction_code", "account_number", "transaction_id", "time", "time_utc"])

    def __init__(self, account_numer: str, first_name: str, last_name: str, tz: TimeZone=None, balance: float=0):
        self._account_number = account_numer
        self._first_name = first_name
        self._last_name = last_name
        self._tz = tz
        self._balance = balance

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, f_name: str):
        if isinstance(str, f_name) and f_name.isalpha():
            self._first_name = f_name.strip()
        else:
            raise ValueError("First name should be composed of letters only and cannot be ")
    
    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, l_name: str):
        if isinstance(str, l_name) and l_name.isalpha():
            self._last_name = l_name.strip()
        else:
            raise ValueError("Last name should be composed of letters only and cannot be ")

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            #raise ValueError("The amount to desposit should be non-negative number")
            return self._build_transaction("X")
        self._balance += amount
        return self._build_transaction("D")

    def withdraw(self, amount: float):
        if amount > self._balance:
            return self._build_transaction("X")
        self._balance -= amount
        return self._build_transaction("W")

    def pay_interest(self):
        self._balance += (self.interest_rate * self._balance) / 100
        return self._build_transaction("I")
    
    def _build_transaction(self, t_type: str) -> str:
        self._transaction_id += 1
        if not self._tz:
            prefered_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + " (UTC)"
            utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        else:
            prefered_time = (datetime.utcnow() - timedelta(hours=self._tz.hours, \
                minutes=self._tz.minutes)).strftime("%Y-%m-%d %H:%M:%S") + f" ({self._tz.tz_name})"
            utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        display_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        trans_obj = self._transaction_details(t_type, self._account_number, self._transaction_id, prefered_time, utc_time)
        
        confirmation_number = t_type + "-" + self._account_number + "-" + \
            display_time + "-" + str(self._transaction_id)
        
        self._transactions[confirmation_number] = trans_obj
        return confirmation_number

    def get_transaction(self, confirmation_number: str):
        return self._transactions.get(confirmation_number)



ivan_acc = Account("89112", "Ivan", "Vladimirov", TimeZone(-2, 0, "EET"))

print(f"current balance: {ivan_acc.balance}")
print(f"Adding -5 to the balance:  {ivan_acc.deposit(-5)}")
print(f"Adding -5 to the balance:  {ivan_acc.deposit(100)}")
print(f"current balance: {ivan_acc.balance}")
print(f"pay interest: {ivan_acc.pay_interest()}")
print(f"current balance: {ivan_acc.balance}")
print(f"Withdraw 1000: {ivan_acc.withdraw(1000)}")
c_num = ivan_acc.withdraw(25)
print(f"Withdraw 25: {c_num}")
print(f"current balance: {ivan_acc.balance}")
print(f'get_conf_number: {ivan_acc.get_transaction(c_num)}')
result = ivan_acc.get_transaction(c_num)

print(result.account_number, result.time)
