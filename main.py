from enum import Enum
import time


PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaTopping', 'tomato caesar')
PizzaTopping = Enum('PizzaTopping', 'mozzarella sulguni pepperoni bacon ham mushrooms onion oregano')
STEP = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {} ...'.format(self.dough.name, self))
        time.sleep(STEP)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.baking_time = 5

    def prepare_dough(self):
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_topping(self):
        print('adding the topping (mozzarella, sulguni, oregano) to your margarita')
        self.pizza.topping.append(
            [i for i in (PizzaTopping.mozzarella, PizzaTopping.sulguni, PizzaTopping.oregano)])
        time.sleep(STEP)
        print('done with the topping (mozzarella, sulguni, oregano)')

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        print('done with the tomato sauce')

    def bake(self):
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('your margarita is ready')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('cream bacon')
        self.baking_time = 5

    def prepare_dough(self):
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the caesar sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.caesar
        time.sleep(STEP)
        print('done with the caesar sauce')

    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, onion, oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                               PizzaTopping.ham, PizzaTopping.mushrooms,
                                               PizzaTopping.onion, PizzaTopping.oregano)])
        time.sleep(STEP)
        print(
            'done with the topping (mozzarella, bacon, ham, mushrooms, onion, oregano)')

    def bake(self):
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('your creamy bacon is ready')

class PepperoniBuilder:
    def __init__(self):
        self.pizza = Pizza('pepperoni')
        self.baking_time = 5

    def prepare_dough(self):
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_topping(self):
        print('adding the topping (pepperoni, mozzarella, onion) to your pepperoni')
        self.pizza.topping.append(
            [i for i in (PizzaTopping.pepperoni, PizzaTopping.mozzarella, PizzaTopping.onion)])
        time.sleep(STEP)
        print('done with the topping (pepperoni, mozzarella, onion)')

    def add_sauce(self):
        print('adding the tomato sauce to your pepperoni...')
        self.pizza.sauce = PizzaSauce.tomato
        print('done with the tomato sauce')

    def bake(self):
        print('baking your pepperoni for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        print('your pepperoni is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input(
            'What pizza would you like, [m] margarita, [c] creamy bacon, [p] pepperoni ')
        builder = builders[pizza_style]()
        valid_input = True

    except KeyError as err:
        print('Sorry, only margarita (key m), creamy bacon (key c) or pepperoni (key p) are available')
        return (False, None)

    return (True, builder)

if __name__ == '__main__':
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder, p=PepperoniBuilder)
    valid_input = False
    waiter = Waiter()

    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()

    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {} !'.format(pizza))