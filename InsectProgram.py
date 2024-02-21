import InsectClass as i


mosquito = i.Insect()
housefly = i.Insect()

mosquito.calc_flight()
housefly.calc_flight()


print('The mosquito will fly:', mosquito.get_miles())
print('The housefly will fly', housefly.get_miles())
