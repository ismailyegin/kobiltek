from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from education.Forms.FoodForm import FoodForm
from education.models.Food import Food
from education.services import food_list_services


@login_required
def food_list(request):
    food_lists = food_list_services.get_food_list()
    form_food = FoodForm()

    if request.method == 'POST':

        form_food = FoodForm(request.POST)

        if form_food.is_valid():

            food = form_food.save()

            messages.warning(request, 'Başarıyla kaydedildi')
            return redirect('education:yemek-listesi')
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
            #messages.add_message(request, messages.INFO, 'Hello world.')


    return render(request, 'food_list.html', {'food_list': food_lists, 'form_food': form_food})
