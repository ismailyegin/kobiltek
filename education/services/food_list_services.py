from education.models.Food import Food


def get_food_list():
    food_lists = reversed(Food.objects.all().order_by('-id')[:30])
    return food_lists
