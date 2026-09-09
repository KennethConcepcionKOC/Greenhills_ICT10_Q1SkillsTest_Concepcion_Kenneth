# price calculation
from pyscript import document

NuttellaCrepe = document.getElementById('NuttellaCrepe')
MatchaMilleCrepe = document.getElementById('MatchaMilleCrepe')
SpinachCheeseCrepe = document.getElementById('SpinachCheeseCrepe')
HamEggCheeseCrepe = document.getElementById('HamEggCheeseCrepe')



def calculate(e):
	document.getElementById('result').style.display = 'block'


# checked is used so that if the box is checked it will return so that it'll be incliuded in the calculation and if not it will return nothing meaning that it wont be included in the calculation
	nutella_price = NuttellaCrepe.checked * 125
	
	matcha_price = MatchaMilleCrepe.checked * 200
	
	spinach_price = SpinachCheeseCrepe.checked * 150
	
	ham_egg_cheese_price = HamEggCheeseCrepe.checked * 165


	subtotal = nutella_price + matcha_price + spinach_price + ham_egg_cheese_price
	
	vat = subtotal * 0.12
	total = subtotal + vat


	document.getElementById('Subtotal').innerHTML = f'Subtotal: ₱{subtotal:.2f}'
	
	document.getElementById('VAT').innerHTML = f'VAT (12% Tax): ₱{vat:.2f}'
	
	document.getElementById('Total').innerHTML = f'Total: ₱{total:.2f}'

