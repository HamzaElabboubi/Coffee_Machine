Coffee Machine 🏆☕

A simple Python program that simulates a Coffee Machine. The machine can prepare espresso, latte, and cappuccino, handle coin transactions, and check resources.

Features ✨

✅ Choose between espresso, latte, or cappuccino

✅ Check remaining resources with report command

✅ Accept coins: quarters, dimes, nickels, pennies

✅ Handle insufficient resources or money

✅ Return change when needed

✅ Stop the machine with off command

Getting Started 🚀
Prerequisites

Python 3.x installed on your machine

How to Run

Clone this repository:

git clone https://github.com/your-username/coffee-machine.git


Navigate to the project folder:

cd coffee-machine


Run the program:

python coffee_machine.py

How to Use ☕

Enter the type of coffee you want:

What would you like? (espresso/latte/cappuccino):


To check the machine’s resources, type:

report


To turn off the machine, type:

off


The program will ask you to insert coins:

How many Quarters:
How many Dimes:
How many Nickles:
How many Pennies:


If enough money is inserted, the coffee will be prepared and change returned if necessary.

Code Structure 📂

MENU dictionary: contains coffee types, ingredients, and cost

resources dictionary: stores the current ingredients and money

verify(drink): checks if resources are enough for the selected drink

get_coins(cost, drink): handles payment and returns change

deduct_resources(drink): subtracts the ingredients from resources

report(resources): prints the current resources

Main loop: handles user input and runs the coffee machine

Example 📝
What would you like? (espresso/latte/cappuccino): latte
Please insert coins:
How many Quarters: 10
How many Dimes: 0
How many Nickles: 0
How many Pennies: 0
Here is $0.5 in change.
Here is your latte. Enjoy!
water : 100
milk : 50
coffee : 76
Money : 2.5