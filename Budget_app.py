class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:<23}{item['amount']:.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spending = [(c.category, sum(item['amount'] for item in c.ledger if item['amount'] < 0)) for c in categories]
    total_spending = sum(spending)

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for category, spent in spending:
            if spent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_len = max(len(c.category) for c in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart.strip()

# Example usage:
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
clothing.withdraw(15.89, "restaurant and more foo")
food.transfer(50, clothing)

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))
