from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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

            messages.success(request, 'Başarıyla kaydedildi')
            return redirect('education:yemek-listesi')
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')
            #messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'food_list.html', {'food_list': food_lists, 'form_food': form_food})


@login_required
def food_delete(request, pk):

    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Food.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Food.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def food_update(request,pk):
    food = Food.objects.get(id=pk)
    form_food = FoodForm(request.POST or None, instance=food)

    if form_food.is_valid():
        form_food.save()
        messages.warning(request, 'Başarıyla Güncellendi')
        redirect('education:yemek-listesi')
    else:
        messages.warning(request, 'Alanları Kontrol Ediniz')
    #messages.add_message(request, messages.INFO, 'Hello world.')

    food_lists = food_list_services.get_food_list()

    return render(request, 'food_list.html', {'food_list': food_lists, 'form_food': form_food})
