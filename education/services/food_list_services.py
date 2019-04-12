from education.models.Food import Food
import datetime


def get_food_list():
    food_lists = Food.objects.all().order_by('food_date')[:30]

    days = {
        "Monday": "Pazartesi",
        "Tuesday": "Salı",
        "Wednesday": "Çarşamba",
        "Thursday": "Perşembe",
        "Friday": "Cuma",
        "Saturday": "Cumartesi",
        "Sunday":"Pazar"
    }

    food_lists_splited =[]
    for food in food_lists:
        food_split = food.menu.split(",")
        food.menu = ''

        food.food_date = food.food_date.strftime("%d/%m/%Y") + ' ' + days[food.food_date.strftime("%A")]
        for item in food_split:
            food.menu = food.menu + '<li class="list-group-item">'+item+'</li>'
        food_lists_splited.append(food)

    food_lists = reversed(food_lists_splited)
    return food_lists
