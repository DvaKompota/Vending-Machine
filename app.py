from VendingMachine import VendingMachine
from vendingui import Ui_MainWindow
from PyQt5 import QtWidgets
from style import style


class VendingMachineUI(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.screen.setText("Welcome to the Vending Machine!")
        self.products = {"Coke": 25, "Pepsi": 35, "Soda": 45}
        self.coins = {"P": 1, "N": 5, "D": 10, "Q": 25}
        self.coins_received = {"Q": 0, "D": 0, "N": 0, "P": 0}
        self.coins_names = {"Q": "Quarter(s)", "D": "Dime(s)", "N": "Nickel(s)", "P": "Penny(ies)"}
        self.amount = 0
        self.coins_str = ""
        self.coins_short_str = ""

        self.ven_ma = VendingMachine(self.products, self.coins)

        self.qCoin.pressed.connect(self.add_q)
        self.dCoin.pressed.connect(self.add_d)
        self.nCoin.pressed.connect(self.add_n)
        self.pCoin.pressed.connect(self.add_p)

        self.coke.pressed.connect(self.order_coke)
        self.pepsi.pressed.connect(self.order_pepsi)
        self.soda.pressed.connect(self.order_soda)
        self.refund.pressed.connect(self.order_refund)

    def add_q(self):
        self.add_coin("Q")

    def add_d(self):
        self.add_coin("D")

    def add_n(self):
        self.add_coin("N")

    def add_p(self):
        self.add_coin("P")

    def add_coin(self, coin):
        self.coins_received[coin] += 1
        self.coins_str = "You've inserted: "
        self.coins_short_str = ""
        self.amount += self.coins[coin]
        self.coins_str = f"You've inserted {self.amount} cents"
        for coin in self.coins_received:
             self.coins_short_str += f"{self.coins_received[coin]}{coin[0]}"
        return self.screen.setText(self.coins_str)

    def order_coke(self):
        order_str = f"Coke,{self.coins_short_str}"
        self.order_drink(order_str)

    def order_pepsi(self):
        order_str = f"Pepsi,{self.coins_short_str}"
        self.order_drink(order_str)

    def order_soda(self):
        order_str = f"Soda,{self.coins_short_str}"
        self.order_drink(order_str)

    def order_drink(self, order_str):
        drink, money = self.ven_ma.input_converter(order_str)
        response = self.ven_ma.execute_order(drink, money)
        self.order_response(response)

    def order_response(self, response):
        if "Sorry" in response:
            self.screen.setText(response)
        elif "Here you go" in response:
            for coin in self.coins_names:
                response = response.replace(coin, f" {self.coins_names[coin]} ")
            self.screen.setText(response)
            for coin in self.coins_received:
                self.coins_received[coin] = 0
            self.amount = 0
            self.coins_str = ""
            self.coins_short_str = ""
        else:
            self.screen.setText("Sorry, something went wrong")

    def order_refund(self):
        if not self.coins_short_str:
            response = f"Sorry, you've inserted no coins to refund"
        else:
            response = f"Your refund is {self.ven_ma.amount_to_coins_converter(self.amount)}"
            for coin in self.coins_names:
                response = response.replace(coin, f" {self.coins_names[coin]} ")
        self.screen.setText(response)
        for coin in self.coins_received:
            self.coins_received[coin] = 0
        self.amount = 0
        self.coins_str = ""
        self.coins_short_str = ""


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setStyleSheet(style)
    window = VendingMachineUI()
    window.show()
    app.exec_()
