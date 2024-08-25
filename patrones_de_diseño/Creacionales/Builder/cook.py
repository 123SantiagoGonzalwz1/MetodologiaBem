from pizza_builder import PizzaBuilder

# Representación del director que
# guía el proceso de construcción de la pizza
class Cook:
    def make_pizza(self, builder):
        builder.set_dough()
        builder.set_sauce()
        builder.set_topping()

        return builder.pizza