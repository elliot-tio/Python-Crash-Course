# 8-12. Sandwiches
print("8-12. Sandwiches\n")


def sandwich_ingredients(*ingredients):
    print("\nThese are the ordered ingredients for the sandwich:")
    for ingredient in ingredients:
        print("- " + ingredient)


sandwich_ingredients('salami')
sandwich_ingredients('salami', 'pastrani')
sandwich_ingredients('feta', 'pepperoni', 'lettuce')

# 8-14. Cars
print("\n8-14. Cars\n")


def car_info(manufacturer, model, **info):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in info.items():
        car_info[key] = value
    return car_info


car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
