import CarClass as c 

car_1 = c.car('2023 Model X', 'Tesla')

for i in range(5):
    car_1.accelerate()
    print(car_1.get_speed())

for i in range(5):
    car_1.brake()
    print(car_1.get_speed())

