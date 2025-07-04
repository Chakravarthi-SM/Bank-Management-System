import json
import random
import string
from pathlib import Path

class Bank:
    def __init__(self):
        self.database = 'data.json'
        self.data = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            with open(self.database, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_data(self):
        with open(self.database, 'w') as f:
            json.dump(self.data, f, indent=4)

    def account_generate(self):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%&*", k=1)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return "".join(acc_id)

    def create_account(self, name, age, email, pin):
        self.data = self.load_data()
        if age < 18:
            return {"error": "Must be 18+ to create an account"}
        if len(str(pin)) != 4:
            return {"error": "PIN must be 4 digits"}

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.account_generate(),
            "balance": 0
        }

        self.data.append(account)
        self.save_data()
        return {"success": "Account created", "account": account}

    def authenticate(self, acc_no, pin):
        self.data = self.load_data()
        for user in self.data:
            if user["accountNo"] == acc_no and user["pin"] == pin:
                return user
        return None

    def deposit(self, acc_no, pin, amount):
        user = self.authenticate(acc_no, pin)
        if not user:
            return {"error": "Invalid credentials"}
        if amount <= 0 or amount > 10000:
            return {"error": "Amount must be between 1 and 10000"}

        user["balance"] += amount
        self.save_data()
        return {"success": f"Deposited ₹{amount}", "balance": user["balance"]}

    def withdraw(self, acc_no, pin, amount):
        user = self.authenticate(acc_no, pin)
        if not user:
            return {"error": "Invalid credentials"}
        if user["balance"] < amount:
            return {"error": "Insufficient balance"}

        user["balance"] -= amount
        self.save_data()
        return {"success": f"Withdrew ₹{amount}", "balance": user["balance"]}

    def show_details(self, acc_no, pin):
        user = self.authenticate(acc_no, pin)
        if not user:
            return {"error": "Invalid credentials"}
        return user

    def update_details(self, acc_no, pin, name=None, email=None, new_pin=None):
        user = self.authenticate(acc_no, pin)
        if not user:
            return {"error": "Invalid credentials"}

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin and len(str(new_pin)) == 4:
            user["pin"] = int(new_pin)

        self.save_data()
        return {"success": "Details updated", "user": user}

    def delete_account(self, acc_no, pin):
        user = self.authenticate(acc_no, pin)
        if not user:
            return {"error": "Invalid credentials"}

        self.data = [u for u in self.data if not (u["accountNo"] == acc_no and u["pin"] == pin)]
        self.save_data()
        return {"success": "Account deleted"}
