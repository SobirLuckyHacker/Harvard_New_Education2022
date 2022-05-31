from django.shortcuts import render,redirect
from .models import OnlineUser
from django.http import JsonResponse


def home_site(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        phone = request.POST.get('phone')
        user = OnlineUser.objects.create(full_name=f_name+" "+l_name,phone=phone)
        return redirect('site')
    return render(request,'Site/index.html')


def all_users(request):
    all_user = OnlineUser.objects.all().order_by("-id")
    list_user = []
    for i in all_user:
            list_user.append({'full_name':i.full_name,"phone":i.phone,'day':i.data.day,'month':i.data.month,'year':i.data.year,'hour':i.data.hour,'min':i.data.minute})
    return JsonResponse({'data':list(list_user)})