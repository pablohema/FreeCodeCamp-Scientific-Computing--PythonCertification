class Category:
    # Initiate class
    def __init__(self, n):
        self.category = n
        self.ledger = []

    # Deposit function
    def deposit(self, amount, description=''):
        self.ledger.append(
            {'amount': amount,
             'description': description}
        )

    # Withdraw function
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {'amount': -amount,
                 'description': description}
            )
            return True
        else:
            return False

    # Get_balance function
    def get_balance(self):
        return sum([wthdrw.get("amount") for wthdrw in self.ledger])

    # Transfer function
    def transfer(self, amount, ctgr):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {ctgr.category}")
            ctgr.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    # Check funds
    def check_funds(self, amount):
        return self.get_balance() >= amount

    # Call to class, print invoice
    def __str__(self):
        invoice = self.category.center(30, "*") + "\n"
        for trans in self.ledger:
            invoice += f'{trans.get("description")[:23]:23}' + f'{trans.get("amount"):7.2f}' + "\n"
        invoice += f"Total: {self.get_balance():.2f}"
        return invoice


def create_spend_chart(categories):
    prnt = "Percentage spent by category\n"
    # Calculate total of spending per category and total
    withdraws = [-sum([cat.get("amount") for cat in cats.ledger if cat.get("amount") < 0]) for cats in categories]
    # Calculate total percentage of spending per category and total
    withdraws_percent = [round(withdraw / sum(withdraws) * 100) for withdraw in withdraws]
    # Collect all category names in a list
    cat_names = [cat.category.lower().capitalize() for cat in categories]

    # Prepare output data
    for i in range(100, -10, -10):
        prnt += str(i).rjust(3) + "| "
        for percent in withdraws_percent:
            if percent >= i:
                prnt += "o  "
            else:
                prnt += "   "
        prnt += "\n"

    # Prepare vertical category labels
    prnt += " " * 4 + "-" * (2 * (len(categories) + 1) + 2)
    max_len_name = len(max(cat_names, key=len))
    vert_name = [name.ljust(max_len_name) for name in cat_names]
    for i in range(max_len_name):
        prnt += "\n     "
        for nm in vert_name:
            prnt += nm[i] + "  "

    return prnt