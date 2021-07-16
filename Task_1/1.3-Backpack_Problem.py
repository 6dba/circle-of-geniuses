
# 'Название':(стоимость, вес)
THIGS = {
    'bed':(220,70), 
    'closet':(200,50), 
    'desk':(130,22), 
    'table':(300,20),
    'tv':(200,30),
    'chair':(100,5),
    'bookshelf':(200,30), 
    'cabinet':(150,20),
    'game_table':(150,12),
    'hammock':(250,45),
    'diner_table':(55,7),
    'mirror':(100,10),
    'instrument':(300,70),
    'plant':(25,10),
    'standing_lamp':(20,5), 
    'garbage_can':(30,3), 
    'laptop':(500,2), 
    'bike_stand':(75,10),
    'chest':(150,25),
    'heater':(30, 2),
    'cat':(100, 5)
}

def calculate(stuff: dict, max_weight: int) -> dict:
    """
    Жадный алгоритм
    Старается высчитать наиболее оптимальный паттерн предметов, которые не превышают max_weight
    """
    for item in stuff:
        cost, weight = stuff[item]
        stuff[item] = tuple((cost, weight, cost/weight))

    # Сортируем словарь. .items() возвращает список кортежей (ключ, (кортеж со значениями)), в значении (т.е в кортеже) сортируем по 3-ему элементу
    # По соотношению - цена/вес, выводим наибольшие значения и обратно формируем словарь
    stuff = dict(sorted(stuff.items(), key=(lambda item: item[1][2]), reverse=True))

    result = dict()
    for key, value in stuff.items():

        if max_weight - value[1] <= 0:
            continue
        
        result[key] = value
        max_weight -= value[1]

    return result