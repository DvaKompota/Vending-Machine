# Vending-Machine

For launching Vending Machine with UI — run app.py
You will need to install PyQt5: pip install PyQt5

For launching text version of Vending Machine — run VendingMachine.py


Problem Statement
You need to design a Vending Machine which
Accepts coins of 1,5,10,25 Cents i.e. penny, nickel, dime, and quarter.
Allow user to select products Coke(25), Pepsi(35), Soda(45)
Allow user to take refund by canceling the request.
Return selected product and remaining change if any.
While a UI would be awesome, the expectation is that this is a program
run on the command-line, which will accept input via keyboard.
Choose what language you want, extra credit for Python 3.

Expected results:
> python3 VendingMachine.py
Vending Machine> What would you like to drink?
Keyboard Entry> Coke,1Q
Vending Machine> Here you go, enjoy!

Vending Machine> What would you like to drink?
Keyboard Entry> Coke,1D
Vending Machine> Sorry, you need more money for that.

Vending Machine> What would you like to drink?
Keyboard Entry> Coke,3D
Vending Machine> Here you go, enjoy! Your change is 1N

Q=quarter, D=dime, N=nickel, P=penny
