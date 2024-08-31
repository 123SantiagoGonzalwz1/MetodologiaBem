import os
import random
import time
from bus import Bus

def clean_console():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    bus_1 = Bus()
    bus_2 = Bus()
    print("CARRERA DE BUSES!!")
    print("Velotax VS Copetron")

    time.sleep(2)
    while True:
        clean_console()
        Bus.draw_start_track()
        bus_1.draw_bus(random.randint(1, 2), "Velotax")
        Bus.draw_start_track()
        bus_2.draw_bus(random.randint(1, 2), "Copetron")
        Bus.draw_start_track()

        if bus_1.position >= 100 or bus_2.position >= 100:
            if bus_1.position >= 100:
                print("Velotax GANA!!")
            else:
                print("Copetron GANA!!")
                time.sleep(10)
                break
        time.sleep(0.1)

main()