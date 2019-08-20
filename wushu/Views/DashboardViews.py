from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def return_admin_dashboard(request):
    return render(request, 'anasayfa/admin.html')
