from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def return_add_branch(request):
    return render(request, 'brans/brans-ekle.html')


@login_required
def return_branchs(request):
    return render(request, 'brans/branslar.html')