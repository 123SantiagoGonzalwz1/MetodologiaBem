class Bus:
    def __init__(self):
        self.position = 0

    @staticmethod
    def draw_start_track():
        print('------------------------------------------------------------------------------------------------------------------------')

    def draw_bus(self, gap, name):
        self.position += gap
        print("                                                                                                                        ")
        print(" " * self.position + name)
        print(" " * self.position + "-------------------")
        print(" " * self.position + "|__|__|__|__|__|__|__")
        print(" " * self.position + "|                    |")
        print(" " * self.position + "|----0-------------0-|")

    @staticmethod
    def draw_final_track():
        print('------------------------------------------------------------------------------------------------------------------------')
