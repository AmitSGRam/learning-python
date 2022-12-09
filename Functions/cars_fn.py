def store_car_info(make, model, **car_info):
    car_info['manufacturer'] = make
    car_info['model'] = model
    return car_info

my_car = store_car_info('tesla', 'model s',
                        color='blue', tow_package=True)
print(my_car)