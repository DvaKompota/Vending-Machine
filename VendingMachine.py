import re


class VendingMachine:

    def __init__(self, products_list, coins_list):
        self.products = products_list
        self.coins = coins_list

    def input_converter(self, order_received: str):
        coma_count = re.findall("\\,", order_received)
        if len(coma_count) < 1:
            print("Please divide the product name and the coins with a coma")
            return None, None
        elif len(coma_count) > 1:
            print("Please use only one coma — to divide the product name from the coins")
            return None, None
        order_no_spaces = order_received.replace(" ", "")
        order_split = order_no_spaces.split(",")
        product = order_split[0]
        if product not in self.products:
            print("No such product available")
            return None, None
        else:
            coin_quantity = re.findall("\\d", order_split[1])
            coin_type = re.findall("\\D", order_split[1])
            if len(coin_quantity) != len(coin_type):
                print("Invalid combination of coins: each coin type should have its quantity and vice versa")
            else:
                amount = 0
                for i in range(len(coin_type)):
                    if coin_type[i] not in self.coins:
                        amount = None
                        print("Invalid type of coin — please insert only valid coins: "
                              "(Q)uarter, (D)ime, (N)ickel, (P)penny")
                    else:
                        amount += self.coins[coin_type[i]] * int(coin_quantity[i])
                return product, amount

    def amount_to_coins_converter(self, amount):
        amount_in_cents = amount
        amount_in_coins = ""
        for coin in ["Q", "D", "N", "P"]:
            if amount_in_cents >= self.coins[coin]:
                coins_quantity = int(amount_in_cents/self.coins[coin])
                amount_in_coins += f"{coins_quantity}{coin}"
                amount_in_cents -= coins_quantity * self.coins[coin]
        return amount_in_coins

    def take_order(self):
        while True:
            drink, money = self.input_converter(input("What would you like to drink [Coke, Pepsi, Soda]? "))
            if drink is not None and money is not None:
                break
        return self.execute_order(drink, money)

    def execute_order(self, drink, money):
        price = self.products[drink]
        if money < price:
            return f"Sorry, you need more money for that. {drink}'s price is {price} cents"
        elif money == price:
            return "Here you go, enjoy!"
        else:
            change = self.amount_to_coins_converter(money - price)
            return f"Here you go, enjoy!\nYour change is {change}"


if __name__ == '__main__':
    products = {"Coke": 25, "Pepsi": 35, "Soda": 45}
    coins = {"P": 1, "N": 5, "D": 10, "Q": 25}
    ven_ma = VendingMachine(products, coins)
    print(ven_ma.take_order())
